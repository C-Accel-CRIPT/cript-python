# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NodeListParams"]


class NodeListParams(TypedDict, total=False):
    after: str
    """UUID of the last record in the previous response"""
