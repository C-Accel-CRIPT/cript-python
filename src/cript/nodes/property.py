from .main import CriptNode


class Property(CriptNode):
    _primary_key = "key"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
