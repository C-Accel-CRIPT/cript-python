# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .nodes import (
    NodesResource,
    AsyncNodesResource,
    NodesResourceWithRawResponse,
    AsyncNodesResourceWithRawResponse,
    NodesResourceWithStreamingResponse,
    AsyncNodesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .nodes.nodes import NodesResource, AsyncNodesResource

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def nodes(self) -> NodesResource:
        return NodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self)


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def nodes(self) -> AsyncNodesResource:
        return AsyncNodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self)


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def nodes(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self._search.nodes)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self._search.nodes)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def nodes(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self._search.nodes)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def nodes(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self._search.nodes)
