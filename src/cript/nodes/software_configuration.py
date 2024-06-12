from .main import CriptNode


class SoftwareConfiguration(CriptNode):
    _primary_key = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
