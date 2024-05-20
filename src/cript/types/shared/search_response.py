# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SearchResponse", "Data"]


class Data(BaseModel):
    count: Optional[float] = None

    limit: Optional[float] = None

    result: Optional[List[object]] = None


class SearchResponse(BaseModel):
    code: Optional[float] = None

    data: Optional[Data] = None

    error: Optional[str] = None

    permissions: Optional[object] = None
