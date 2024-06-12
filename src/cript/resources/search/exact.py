# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.search import exact_child_node_params
from ...types.shared.search import Search

__all__ = ["ExactResource", "AsyncExactResource"]


class ExactResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExactResourceWithRawResponse:
        return ExactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExactResourceWithStreamingResponse:
        return ExactResourceWithStreamingResponse(self)

    def node(
        self,
        *,
        node: str,
        q: str,
        field: str | NotGiven = "name",
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
            f"/search/exact/{node}",
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
                    exact_child_node_params.ExactChildNodeParams,
                ),
            ),
            cast_to=Search,
        )

    def child_node(
        self,
        child_node: str,
        *,
        node: str,
        uuid: str,
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
        Search by child node

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if not child_node:
            raise ValueError(f"Expected a non-empty value for `child_node` but received {child_node!r}")
        return self._get(
            f"/search/exact/{node}/{uuid}/{child_node}",
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
                    exact_child_node_params.ExactChildNodeParams,
                ),
            ),
            cast_to=Search,
        )


class AsyncExactResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExactResourceWithRawResponse:
        return AsyncExactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExactResourceWithStreamingResponse:
        return AsyncExactResourceWithStreamingResponse(self)

    async def child_node(
        self,
        child_node: str,
        *,
        node: str,
        uuid: str,
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
        Search by child node

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if not child_node:
            raise ValueError(f"Expected a non-empty value for `child_node` but received {child_node!r}")
        return await self._get(
            f"/search/exact/{node}/{uuid}/{child_node}",
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
                    exact_child_node_params.ExactChildNodeParams,
                ),
            ),
            cast_to=Search,
        )


class ExactResourceWithRawResponse:
    def __init__(self, exact: ExactResource) -> None:
        self._exact = exact

        self.child_node = to_raw_response_wrapper(
            exact.child_node,
        )


class AsyncExactResourceWithRawResponse:
    def __init__(self, exact: AsyncExactResource) -> None:
        self._exact = exact

        self.child_node = async_to_raw_response_wrapper(
            exact.child_node,
        )


class ExactResourceWithStreamingResponse:
    def __init__(self, exact: ExactResource) -> None:
        self._exact = exact

        self.child_node = to_streamed_response_wrapper(
            exact.child_node,
        )


class AsyncExactResourceWithStreamingResponse:
    def __init__(self, exact: AsyncExactResource) -> None:
        self._exact = exact

        self.child_node = async_to_streamed_response_wrapper(
            exact.child_node,
        )
