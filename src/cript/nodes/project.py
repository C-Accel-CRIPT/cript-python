from .main import CriptNode
from collections import OrderedDict


class Project(CriptNode):
    _retrieve_on_init = True
    _post = True

    def __init__(self, *args, **kwargs):

        if "material" in kwargs:
            # order the material to be processed first
            od = OrderedDict()
            for k in kwargs:
                od[k] = kwargs[k]
            od.move_to_end("material", last=False)
            kwargs = od

        super().__init__(*args, **kwargs)
