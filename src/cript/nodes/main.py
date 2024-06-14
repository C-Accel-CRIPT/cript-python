import copy
import inspect
import logging
import sys
import jsonpatch
import jsonschema
from jsonschema.validators import validator_for
from jsonschema.exceptions import best_match
from uuid import uuid4

from cript import Cript, NotFoundError, camel_case_to_snake_case, extract_node_from_result
from .schema import cript_schema

logger = logging.getLogger(__name__)


class CriptNode(dict):
    _primary_key = "name"
    _retrieve_on_init = False
    _post = False

    def __init__(self, *args, **kwargs):
        self.__dict__["exists"] = self.__dict__.get("exists", False)
        self.__dict__["client"] = self.__dict__.get("client", Cript())
        self.__dict__["children"] = self.__dict__.get("children", {})
        self.__dict__["initialized"] = False
        self.__dict__["parent"] = None
        schema = copy.deepcopy(cript_schema)
        schema["$ref"] = f"#/$defs/{self.__class__.__name__}Post"
        resolver = kwargs.get("resolver", None)
        kwargs["node"] = [self.__class__.__name__]
        self.prepare_child_nodes(kwargs)
        self.__dict__["kwargs"] = copy.deepcopy(kwargs)
        self.__dict__["schema"] = schema
        self.__dict__["resolver"] = resolver
        cls = validator_for(schema)
        if resolver is not None:
            self.__dict__["validator_instance"] = cls(schema, resolver=resolver)
        else:
            self.__dict__["validator_instance"] = cls(schema)
        d = dict(*args, **kwargs)
        if self._retrieve_on_init:
            if "uuid" not in kwargs and len(kwargs) > 1:
                self.validate(d)

            if kwargs.get("uuid"):
                self.retrieve_by_uuid(kwargs["uuid"])
            else:
                self.retrieve_by_field(kwargs[self._primary_key])
        if not self.__dict__["exists"]:
            try:
                self.validate(d)
            except ValueError as exc:
                raise ValueError(str(exc)) from exc

            if self._post:
                self._create_node(d)
            for key in d:
                if key in self.__dict__["schema"]["$defs"][f"{self.node_name}Post"]["properties"]:
                    setattr(self, key, d[key])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

        # process children
        self.process_children()
        self.final_update()
        self.__dict__["initialized"] = True

    @property
    def name_url(self):
        return camel_case_to_snake_case(self.__class__.__name__)

    @property
    def node_name(self):
        return self.__class__.__name__

    def final_update(self):
        if not hasattr(self, "uuid"):
            logger.info(f"{self.node_name} {self.get(self._primary_key)} doesn't have uuid assigned yet, and cannot be final_updated.")
            return

        kwargs = self.__dict__["kwargs"]
        for key in kwargs:
            setattr(self, key, kwargs[key])
        body = {"node": self.node}
        to_patch = []
        for l in self.patch:
            if l.get("op") in ["add", "replace"]:
                prop_path = l["path"][1:]
                is_child = False
                if isinstance(l["value"], list):
                    for el in l["value"]:
                        if isinstance(el, CriptNode):
                            is_child = True
                            break
                    if not is_child:
                        body[prop_path] = l["value"]
                        # to_patch.append(l)
                elif isinstance(l["value"], dict):
                    if l["value"].get("uuid") and len(l["value"]) == 1:
                        continue
                    if l["value"].get("node"):
                        continue
                else:
                    attr = prop_path.split("/")
                    if len(attr) > 1:
                        continue
                    body[prop_path] = l["value"]
        if len(body.keys()) > 1:
            result = self.__dict__["client"].nodes.update(
                node=self.name_url,
                uuid=self.uuid,
                body=body,
            )
            return result

    def process_update(self, key, child_to_process, is_array=False):
        if not hasattr(self, "uuid"):
            logger.info(f"{self.node_name} {self.get(self._primary_key)} doesn't have uuid assigned yet, and cannot process_update.")
            return
        body = {"node": self.node}
        node_to_append = child_to_process
        if "uuid" in child_to_process:
            node_to_append = {"uuid": child_to_process.get("uuid")}
        else:
            if not "uuid" in child_to_process:
                child_to_process["uuid"] = f"{uuid4()}"
            node_to_append = child_to_process

        if is_array:
            # setattr(self, key, [node_to_append])
            body[key] = [node_to_append]
        else:
            # setattr(self, key, node_to_append)
            body[key] = node_to_append

        if len(body.keys()) > 1:
            result = self.__dict__["client"].nodes.update(
                node=self.name_url,
                uuid=self.uuid,
                body=body,
            )
            return result

    def process_children(self):
        kwargs = self.__dict__["children"]
        for k in self.__dict__["children"]:
            if isinstance(kwargs[k], CriptNode):
                if hasattr(self, "uuid"):
                    # TODO remove previous object / replace with current -> send delete that removes all
                    l = kwargs[k]
                    l.retrieve_child(self, l)
                    self.process_update(k, l, False)
                    l.retrieve_by_uuid(l.uuid)
                    l.final_update()
                    l.process_children()
            elif isinstance(kwargs[k], list):
                for l in kwargs[k]:
                    if isinstance(l, CriptNode):
                        if hasattr(self, "uuid"):
                            l.retrieve_child(self, l)
                            self.process_update(k, l, True)
                            l.retrieve_by_uuid(l.uuid)
                            l.final_update()
                            l.process_children()
                        else:
                            # print(self.name_url, "NODE DOESN't have uuid")
                            logger.info(f"{self.name_url} {self.get(self._primary_key)} doesn't have uuid assigned yet")
                            pass

    def prepare_child_nodes(self, kwargs):
        for k, v in kwargs.copy().items():
            if isinstance(v, CriptNode):
                self.__dict__["children"][k] = v
                if v.__dict__["exists"]:
                    # leave the link as a child attr
                    kwargs[k] = {"uuid": v.get("uuid")}
                    continue
                del kwargs[k]
            elif isinstance(v, list):
                links = []
                children = []
                for l in v:
                    if isinstance(l, CriptNode):
                        if l.__dict__["exists"]:
                            links.append({"uuid": l.get("uuid")})
                        else:
                            children.append(l)
                if children:
                    self.__dict__["children"][k] = children
                    del kwargs[k]
                if links:
                    kwargs[k] = links

    def __setitem__(self, key, value):
        # mutation = dict(copy.deepcopy(self.__dict__.get("__original__", {})))
        # mutation[key] = value
        # if self.__dict__["exists"]:
        #     try:
        #         self.validate(mutation)
        #     except ValueError as exc:
        #         msg = "Unable to set '%s' to %r. Reason: %s" % (key, value, str(exc))
        #         raise Exception(str(exc)) from exc

        dict.__setitem__(self, key, value)

    def __delitem__(self, key):
        if not self.__dict__.get("deleted"):
            self.__dict__["__original__"] = self.copy()
            mutation = dict(self.items())
            for m, v in mutation.copy().items():
                if (isinstance(v, dict) and v.get("node")) or (
                    isinstance(v, list) and any(isinstance(l, dict) and l.get("node") for l in v)
                ):
                    del mutation[m]
            del mutation[key]
            try:
                self.validate(mutation)
            except ValueError as exc:
                msg = "Unable to delete attribute '%s'. Reason: %s" % (key, str(exc))
                raise ValueError(str(msg)) from exc

        dict.__delitem__(self, key)

    def __getattr__(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __delattr__(self, key):
        self.__delitem__(key)

    def destroy(self):
        self.__dict__["deleted"] = True
        self.__dict__["__original__"] = {}
        self.__dict__["exists"] = False
        self.__dict__["children"] = {}
        self.__dict__["initialized"] = False
        self.__dict__["parent"] = None
        del self.__dict__["schema"]
        del self.__dict__["validator_instance"]
        for attr in dict(self):
            delattr(self, attr)

    def clear(self):
        tmp = self.__dict__.get("deleted", False)
        self.__dict__["deleted"] = True
        for attr in dict(self):
            delattr(self, attr)
        self.__dict__["deleted"] = tmp

    def pop(self, key, default=None):
        raise Exception("operation not allowed")

    def popitem(self):
        raise Exception("operation not allowed")

    def remove_item(self, key, item):
        self.__dict__["__original__"] = self.copy()
        mutation = dict(self.items())
        mutation[key].remove(item)
        try:
            self.validate(mutation)
        except ValueError as exc:
            msg = "Unable to delete attribute '%s'. Reason: %s" % (key, str(exc))
            raise Exception(str(exc))
        self[key].remove(item)

    def copy(self):
        return copy.deepcopy(dict(self))

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memo):
        # TODO consider what a deep copy means.
        # Does it mean we have new nodes with new UUIDs?
        return copy.deepcopy(dict(self), memo)

    def remove(self, key, item=None):
        if not item:
            return self.__delitem__(key)
        return self.remove_item(key, item)

    def update(self, other):
        mutation = dict(self.items())
        mutation.update(other)
        try:
            self.validate(mutation)
        except ValueError as exc:
            raise RuntimeError(str(exc)) from exc
        dict.update(self, other)

    def items(self):
        return copy.deepcopy(dict(self)).items()

    def values(self):
        return copy.deepcopy(dict(self)).values()

    @property
    def patch(self):
        """Return a jsonpatch object representing the delta"""
        original = self.__dict__["__original__"]
        return jsonpatch.make_patch(original, dict(self))

    def validate(self, obj):
        """Apply a JSON schema to an object"""
        try:
            # self.validator_instance.validate(obj)
            v = self.validator_instance
            # error = best_match(v.iter_errors(obj)).message
            errors = sorted(v.iter_errors(obj), key=lambda e: f"{e.path} for node")
            if errors:
                # logger.error(f"Node: {self.__class__.__name__}, errors: {[error.message for error in errors]}")
                sys.tracebacklimit = 0
                raise ValueError(f"Node: {self.node_name}, errors: {[error.message for error in errors]}")
        except jsonschema.ValidationError as exc:
            raise ValueError(str(exc)) from exc

    def retrieve_by_uuid(self, uuid):
        try:
            result = self.__dict__["client"].nodes.retrieve(node=self.name_url, uuid=uuid)
            data = extract_node_from_result(result.data)
            self.__dict__["exists"] = True
            allowed_data = {}
            for key in data:
                if key in self.__dict__["schema"]["$defs"][f"{self.node_name}Post"]["properties"]:
                    setattr(self, key, data[key])
                    allowed_data[key] = data[key]
            self.__dict__["__original__"] = copy.deepcopy(allowed_data)
        except NotFoundError:
            self.__dict__["exists"] = False


    def retrieve_by_field(self, query):
        try:
            result = self.__dict__["client"].search.exact.node(node=self.name_url, q=query, field=self._primary_key)
            data = extract_node_from_result(result.data.result)
            if not data:
                self.__dict__["exists"] = False
                return
            allowed_data = {}
            self.__dict__["exists"] = True
            for key in data:
                if key in self.__dict__["schema"]["$defs"][f"{self.node_name}Post"]["properties"]:
                    setattr(self, key, data[key])
                    allowed_data[key] = data[key]
            self.__dict__["__original__"] = copy.deepcopy(allowed_data)
        except NotFoundError:
            self.__dict__["exists"] = False

    def process_with_parent(self, uuid):
        self.__dict__["parent"] = uuid

    def retrieve_child(self, parent, child):
        try:
            if not self._primary_key:
                result = self.__dict__["client"].nodes.retrieve_children(
                    node=parent.name_url, uuid=parent.uuid, child_node=child.name_url
                )
            else:
                result = self.__dict__["client"].search.exact.child_node(
                    node=parent.name_url,
                    uuid=parent.uuid,
                    child_node=child.name_url,
                    q=child.get(child._primary_key),
                    field=child._primary_key,
                )

            data = extract_node_from_result(result.data.result)
            if not data:
                self.__dict__["exists"] = False
            else:
                allowed_data = {}
                child.__dict__["exists"] = True
                child.uuid = data["uuid"]
                for key in data:
                    if key in child.__dict__["schema"]["$defs"][f"{child.__class__.__name__}Post"]["properties"]:
                        setattr(child, key, data[key])
                        allowed_data[key] = data[key]
                child.__dict__["__original__"] = copy.deepcopy(allowed_data)
            child.process_with_parent(parent.uuid)
        except NotFoundError:
            self.__dict__["exists"] = False
            pass

    def _create_node(self, d):
        result = self.__dict__["client"].nodes.create(node=self.name_url, body=d)
        # TODO error handling
        data = extract_node_from_result(result.data.get("result", []))
        self.uuid = data["uuid"]
        self.__dict__["__original__"] = copy.deepcopy({"uuid": data["uuid"], **d})
        self.__dict__["exists"] = True

    def delete(self, *args, **kwargs):
        if not self.get("uuid"):
            raise ValueError(f"Node {self.node_name} {self.get(self._primary_key)} unitialized, Missing uuid.")
        if not kwargs:
            # delete the whole node
            result = self.__dict__["client"].nodes.delete(node=self.name_url, uuid=self.uuid, body={})
            self.destroy()
        else:
            # delete attributes
            kwargs = {**copy.deepcopy(kwargs), "node": self.__class__.__name__}
            for k, v in kwargs.items():
                self.convert_node_to_link(v)
                if isinstance(v, list):
                    for l in v:
                        self.convert_node_to_link(l)
            result = self.__dict__["client"].nodes.delete(node=self.name_url, uuid=self.uuid, body=kwargs)

            node_uuid = self.uuid
            self.clear()
            self.retrieve_by_uuid(node_uuid)
            d = dict(self)
            for k in d:
                if k in kwargs and not isinstance(d[k], (list, dict)):
                    del self[k]

    def convert_node_to_link(self, node):
        if isinstance(node, dict) and node.get("uuid"):
            uuid = node.get("uuid")
            node.clear()
            node["uuid"] = uuid
