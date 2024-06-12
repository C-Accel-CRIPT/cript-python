from .main import CriptNode


class Reference(CriptNode):
    _primary_key = "title"
    _retrieve_on_init = True
    _post = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
