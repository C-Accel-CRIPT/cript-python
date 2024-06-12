# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cript import Cript, AsyncCript
from tests.utils import assert_matches_type
from cript.types.shared import Search

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cript) -> None:
        node = client.search.nodes.list(
            "string",
            q="string",
        )
        assert_matches_type(Search, node, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cript) -> None:
        node = client.search.nodes.list(
            "string",
            q="string",
            field="string",
        )
        assert_matches_type(Search, node, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cript) -> None:
        response = client.search.nodes.with_raw_response.list(
            "string",
            q="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(Search, node, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cript) -> None:
        with client.search.nodes.with_streaming_response.list(
            "string",
            q="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(Search, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cript) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_name` but received ''"):
            client.search.nodes.with_raw_response.list(
                "",
                q="string",
            )


class TestAsyncNodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCript) -> None:
        node = await async_client.search.nodes.list(
            "string",
            q="string",
        )
        assert_matches_type(Search, node, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCript) -> None:
        node = await async_client.search.nodes.list(
            "string",
            q="string",
            field="string",
        )
        assert_matches_type(Search, node, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCript) -> None:
        response = await async_client.search.nodes.with_raw_response.list(
            "string",
            q="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(Search, node, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCript) -> None:
        async with async_client.search.nodes.with_streaming_response.list(
            "string",
            q="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(Search, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCript) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_name` but received ''"):
            await async_client.search.nodes.with_raw_response.list(
                "",
                q="string",
            )
