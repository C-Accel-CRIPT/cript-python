# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChildListParams"]


class ChildListParams(TypedDict, total=False):
    node_name: Required[str]

    uuid: Required[str]

    q: Required[str]
    """Search query"""

    field: str
    """name of the field to search"""
