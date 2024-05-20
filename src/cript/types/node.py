# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Node"]


class Node(BaseModel):
    code: Optional[float] = None

    data: Optional[List[object]] = None

    error: Optional[str] = None

    permissions: Optional[object] = None
