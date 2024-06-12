# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .exact import (
    ExactResource,
    AsyncExactResource,
    ExactResourceWithRawResponse,
    AsyncExactResourceWithRawResponse,
    ExactResourceWithStreamingResponse,
    AsyncExactResourceWithStreamingResponse,
)
from ...types import search_node_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.shared.search import Search

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def exact(self) -> ExactResource:
        return ExactResource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self)

    def node(
        self,
        node: str,
        *,
        q: str,
        field: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Search:
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
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        return self._get(
            f"/search/{node}",
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
                    search_node_params.SearchNodeParams,
                ),
            ),
            cast_to=Search,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def exact(self) -> AsyncExactResource:
        return AsyncExactResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self)

    async def node(
        self,
        node: str,
        *,
        q: str,
        field: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Search:
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
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        return await self._get(
            f"/search/{node}",
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
                    search_node_params.SearchNodeParams,
                ),
            ),
            cast_to=Search,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.node = to_raw_response_wrapper(
            search.node,
        )

    @cached_property
    def exact(self) -> ExactResourceWithRawResponse:
        return ExactResourceWithRawResponse(self._search.exact)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.node = async_to_raw_response_wrapper(
            search.node,
        )

    @cached_property
    def exact(self) -> AsyncExactResourceWithRawResponse:
        return AsyncExactResourceWithRawResponse(self._search.exact)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.node = to_streamed_response_wrapper(
            search.node,
        )

    @cached_property
    def exact(self) -> ExactResourceWithStreamingResponse:
        return ExactResourceWithStreamingResponse(self._search.exact)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.node = async_to_streamed_response_wrapper(
            search.node,
        )

    @cached_property
    def exact(self) -> AsyncExactResourceWithStreamingResponse:
        return AsyncExactResourceWithStreamingResponse(self._search.exact)
