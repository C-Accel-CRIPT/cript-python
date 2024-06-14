import logging
import time

from cript import (
    nodes,
    Cript,
    Algorithm,
    Citation,
    Collection,
    ComputationProcess,
    Computation,
    ComputationalForcefield,
    Condition,
    Data,
    Equipment,
    Experiment,
    File,
    Ingredient,
    Inventory,
    Material,
    Parameter,
    Process,
    Project,
    Property,
    Quantity,
    Reference,
    SoftwareConfiguration,
    Software,
    User,
    camel_case_to_snake_case,
    APIStatusError,
)

logger = logging.getLogger(__name__)


def Search(node, q, field=None, client=None, filters={}):
    try:
        client = client or Cript()
        if not field:
            field = get_node_class(node)._primary_key
        node = node_name_url(node)
        limit = filters.get("limit", 100)
        _next = True
        after = None
        score = None
        total = 0
        while _next:
            fn = (
                handle_bigsmiles
                if (field == "bigsmiles" or field == "smiles") and node == "material"
                else handle_search
            )
            filters = {**filters, "after": after, "score": score}
            count, result = fn(node, q, client, field, filters)
            for r in result:
                total = total + 1
                if total > limit:
                    break
                yield r
            if total >= count or len(result) == 0 or total >= limit:
                _next = False
            if len(result):
                if after == result[-1].get("uuid"):
                    _next = False
                after = result[-1].get("uuid")
                score = result[-1].get("score")
    except Exception as e:
        logger.error(e)
        raise e


def handle_search(node, q, client, field, filters):
    body = {**filters, "q": q, "field": field}

    result = client.search.node(node=node, body=body)
    return get_data(result)


def handle_bigsmiles(node, q, client, field, filters):
    result = client.search.bigsmiles(q=q, field=field, after=filters.get("after"), score=filters.get("score"))
    return get_data(result)


def get_node_class(node):
    try:
        if type(node) == type and node.__name__ in nodes.__all__:
            return node
        else:
            i = next(i for i, v in enumerate(nodes.__all__) if v.lower() == node.lower())
            name = nodes.__all__[i]
        return getattr(nodes, name)
    except Exception as e:
        logger.error(e)
        raise ValueError(f"Error: node={node} is not valid")


def node_name_url(node):
    return camel_case_to_snake_case(get_node_class(node).__name__)


def get_data(result):
    if result.code == 200:
        data = result.data
        return data.count, data.result
    raise APIStatusError(f"Error: status: {result.code}, message: {result.error}")
