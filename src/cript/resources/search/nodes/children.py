# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....types.search.nodes import child_list_params
from ....types.shared.search_response import SearchResponse

__all__ = ["ChildrenResource", "AsyncChildrenResource"]


class ChildrenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChildrenResourceWithRawResponse:
        return ChildrenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChildrenResourceWithStreamingResponse:
        return ChildrenResourceWithStreamingResponse(self)

    def list(
        self,
        child_node: str,
        *,
        node_name: str,
        uuid: str,
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
        Search by child node

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if not child_node:
            raise ValueError(f"Expected a non-empty value for `child_node` but received {child_node!r}")
        return self._get(
            f"/search/exact/{node_name}/{uuid}/{child_node}",
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
                    child_list_params.ChildListParams,
                ),
            ),
            cast_to=SearchResponse,
        )


class AsyncChildrenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChildrenResourceWithRawResponse:
        return AsyncChildrenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChildrenResourceWithStreamingResponse:
        return AsyncChildrenResourceWithStreamingResponse(self)

    async def list(
        self,
        child_node: str,
        *,
        node_name: str,
        uuid: str,
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
        Search by child node

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if not child_node:
            raise ValueError(f"Expected a non-empty value for `child_node` but received {child_node!r}")
        return await self._get(
            f"/search/exact/{node_name}/{uuid}/{child_node}",
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
                    child_list_params.ChildListParams,
                ),
            ),
            cast_to=SearchResponse,
        )


class ChildrenResourceWithRawResponse:
    def __init__(self, children: ChildrenResource) -> None:
        self._children = children

        self.list = to_raw_response_wrapper(
            children.list,
        )


class AsyncChildrenResourceWithRawResponse:
    def __init__(self, children: AsyncChildrenResource) -> None:
        self._children = children

        self.list = async_to_raw_response_wrapper(
            children.list,
        )


class ChildrenResourceWithStreamingResponse:
    def __init__(self, children: ChildrenResource) -> None:
        self._children = children

        self.list = to_streamed_response_wrapper(
            children.list,
        )


class AsyncChildrenResourceWithStreamingResponse:
    def __init__(self, children: AsyncChildrenResource) -> None:
        self._children = children

        self.list = async_to_streamed_response_wrapper(
            children.list,
        )
