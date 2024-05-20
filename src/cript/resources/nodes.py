# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import node_create_params, node_delete_params, node_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.node import Node
from .._base_client import (
    make_request_options,
)

__all__ = ["NodesResource", "AsyncNodesResource"]


class NodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NodesResourceWithRawResponse:
        return NodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NodesResourceWithStreamingResponse:
        return NodesResourceWithStreamingResponse(self)

    def create(
        self,
        uuid: str,
        *,
        node: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Node:
        """
        Create a Node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._post(
            f"/{node}/{uuid}",
            body=maybe_transform(body, node_create_params.NodeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Node,
        )

    def retrieve(
        self,
        uuid: str,
        *,
        node: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Node:
        """
        Get a node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/{node}/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Node,
        )

    def update(
        self,
        uuid: str,
        *,
        node: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Node:
        """
        Patch a Node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._patch(
            f"/{node}/{uuid}",
            body=maybe_transform(body, node_update_params.NodeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Node,
        )

    def delete(
        self,
        uuid: str,
        *,
        node: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Node:
        """
        Delete a Node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/{node}/{uuid}",
            body=maybe_transform(body, node_delete_params.NodeDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Node,
        )


class AsyncNodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNodesResourceWithRawResponse:
        return AsyncNodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNodesResourceWithStreamingResponse:
        return AsyncNodesResourceWithStreamingResponse(self)

    async def create(
        self,
        uuid: str,
        *,
        node: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Node:
        """
        Create a Node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._post(
            f"/{node}/{uuid}",
            body=await async_maybe_transform(body, node_create_params.NodeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Node,
        )

    async def retrieve(
        self,
        uuid: str,
        *,
        node: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Node:
        """
        Get a node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/{node}/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Node,
        )

    async def update(
        self,
        uuid: str,
        *,
        node: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Node:
        """
        Patch a Node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._patch(
            f"/{node}/{uuid}",
            body=await async_maybe_transform(body, node_update_params.NodeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Node,
        )

    async def delete(
        self,
        uuid: str,
        *,
        node: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Node:
        """
        Delete a Node

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not node:
            raise ValueError(f"Expected a non-empty value for `node` but received {node!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/{node}/{uuid}",
            body=await async_maybe_transform(body, node_delete_params.NodeDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Node,
        )


class NodesResourceWithRawResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.create = to_raw_response_wrapper(
            nodes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            nodes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            nodes.update,
        )
        self.delete = to_raw_response_wrapper(
            nodes.delete,
        )


class AsyncNodesResourceWithRawResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.create = async_to_raw_response_wrapper(
            nodes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            nodes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            nodes.update,
        )
        self.delete = async_to_raw_response_wrapper(
            nodes.delete,
        )


class NodesResourceWithStreamingResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.create = to_streamed_response_wrapper(
            nodes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            nodes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            nodes.update,
        )
        self.delete = to_streamed_response_wrapper(
            nodes.delete,
        )


class AsyncNodesResourceWithStreamingResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.create = async_to_streamed_response_wrapper(
            nodes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            nodes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            nodes.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            nodes.delete,
        )
