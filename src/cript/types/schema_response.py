# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SchemaResponse"]


class SchemaResponse(BaseModel):
    code: Optional[float] = None

    data: Optional[object] = None

    error: Optional[str] = None

    permissions: Optional[object] = None
