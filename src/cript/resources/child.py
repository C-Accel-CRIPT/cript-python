import httpx
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.shared.search import Search
from .._resource import SyncAPIResource

class ChildPaginator:
    # TODO consider writing operations
    def __init__(self, parent, child, client=None):
        if client is None:
            client = parent.client
        self._client = client
        self._parent = parent
        self._child = child

        self._current_child_list = []
        self._current_child_position = 0
        self._current_page = 0
        self._count = None

    def __iter__(self):
        self._current_child_position = 0
        return self

    def __next__(self):
        if self._current_child_position >= len(self._current_child_list):
            self._fetch_next_page()
        try:
            next_node = self._current_child_list[self._current_child_position]
        except IndexError:
            raise StopIteration

        self._current_child_position += 1

        return next_node

    def _fetch_next_page(self):
        if self._finished_fetching:
            raise StopIteration

        response = self._client._child.child(self._parent, self._child, self._current_page)
        self._current_page += 1
        if self._count is not None and self._count != int(response.data.count):
            raise RuntimeError("The number of elements for a child iteration changed during pagination. This may lead to inconsistencies. Please try again.")
        self._count = int(response.data.count)

        self._current_child_list += response.data.result

    # Make it a random access iterator, since ppl expect it to behave list a list
    def __getitem__(self, key):
        key_index = int(key)
        previous_pos = self._current_child_position
        try:
            if key_index < 0:
                while not self._finished_fetching:
                    next(self)

            while len(self._current_child_list) <= key_index:
                try:
                    next(self)
                except StopIteration:
                    break
        finally:
            self._current_child_position = previous_pos
        # We don't need explicit bounds checking, since the list access does that for us.
        return self._current_child_list[key_index]

    def __len__(self):
        previous_pos = self._current_child_position
        try:
            if self._count is None:
                try:
                    next(iter(self))
                except StopIteration:
                    self._count = 0
        finally:
            self._current_child_position = previous_pos
        return self._count

    @property
    def _finished_fetching(self):
        if self._count is None:
            return False
        return len(self._current_child_list) == self._count


class ChildResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self):
        return ChildResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self):
        return ChildResourceWithStreamingResponse(self)

    def child(
            self,
            parent,
            child: str,
            page: int,
            *,
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Search:
        """
        Obtain all children of parent node.

        Args:
          parent: parent node
          child: attribute name of the child node
        """
        return self._get(f"/{parent.name_url}/{parent.uuid}/{child}",
                         options=make_request_options(
                             extra_headers=extra_headers,
                             extra_query=extra_query,
                             extra_body=extra_body,
                             query={"page": page},
                             timeout=timeout,
                         ),
                         cast_to=Search,
                         )


class ChildResourceWithRawResponse:
    def __init__(self, child:ChildResource) -> None:
        self._child = child

        self.node = to_raw_response_wrapper(child.node)

class ChildResourceWithStreamingResponse:
    def __init__(self, child:ChildResource) -> None:
        self._child = child

        self.node = to_streamed_response_wrapper(child.node)
