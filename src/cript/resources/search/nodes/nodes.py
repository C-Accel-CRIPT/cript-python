# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .children import (
    ChildrenResource,
    AsyncChildrenResource,
    ChildrenResourceWithRawResponse,
    AsyncChildrenResourceWithRawResponse,
    ChildrenResourceWithStreamingResponse,
    AsyncChildrenResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.search import node_list_params
from ....types.shared.search_response import SearchResponse

__all__ = ["NodesResource", "AsyncNodesResource"]


class NodesResource(SyncAPIResource):
    @cached_property
    def children(self) -> ChildrenResource:
        return ChildrenResource(self._client)

    @cached_property
    def with_raw_response(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self)

    def list(
        self,
        node_name: str,
        *,
        q: str,
        field: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Search by node

        Args:
          q: Search query

          field: name of the field to search

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_name:
            raise ValueError(f"Expected a non-empty value for `node_name` but received {node_name!r}")
        return self._get(
            f"/search/{node_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "field": field,
                    },
                    node_list_params.NodeListParams,
                ),
            ),
            cast_to=SearchResponse,
        )


class AsyncNodesResource(AsyncAPIResource):
    @cached_property
    def children(self) -> AsyncChildrenResource:
        return AsyncChildrenResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self)

    async def list(
        self,
        node_name: str,
        *,
        q: str,
        field: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Search by node

        Args:
          q: Search query

          field: name of the field to search

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node_name:
            raise ValueError(f"Expected a non-empty value for `node_name` but received {node_name!r}")
        return await self._get(
            f"/search/{node_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "field": field,
                    },
                    node_list_params.NodeListParams,
                ),
            ),
            cast_to=SearchResponse,
        )


class NodesResourceWithRawResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.list = to_raw_response_wrapper(
            nodes.list,
        )

    @cached_property
    def children(self) -> ChildrenResourceWithRawResponse:
        return ChildrenResourceWithRawResponse(self._nodes.children)


class AsyncNodesResourceWithRawResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.list = async_to_raw_response_wrapper(
            nodes.list,
        )

    @cached_property
    def children(self) -> AsyncChildrenResourceWithRawResponse:
        return AsyncChildrenResourceWithRawResponse(self._nodes.children)


class NodesResourceWithStreamingResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.list = to_streamed_response_wrapper(
            nodes.list,
        )

    @cached_property
    def children(self) -> ChildrenResourceWithStreamingResponse:
        return ChildrenResourceWithStreamingResponse(self._nodes.children)


class AsyncNodesResourceWithStreamingResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.list = async_to_streamed_response_wrapper(
            nodes.list,
        )

    @cached_property
    def children(self) -> AsyncChildrenResourceWithStreamingResponse:
        return AsyncChildrenResourceWithStreamingResponse(self._nodes.children)
