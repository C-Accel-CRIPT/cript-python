from .main import CriptNode


class Material(CriptNode):
    _retrieve_on_init = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
