# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cript import Cript, AsyncCript
from cript.types import SchemaResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestControlledVocabularies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Cript) -> None:
        controlled_vocabulary = client.controlled_vocabularies.retrieve(
            "string",
        )
        assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Cript) -> None:
        response = client.controlled_vocabularies.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        controlled_vocabulary = response.parse()
        assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Cript) -> None:
        with client.controlled_vocabularies.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            controlled_vocabulary = response.parse()
            assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Cript) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.controlled_vocabularies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Cript) -> None:
        controlled_vocabulary = client.controlled_vocabularies.list()
        assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cript) -> None:
        response = client.controlled_vocabularies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        controlled_vocabulary = response.parse()
        assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cript) -> None:
        with client.controlled_vocabularies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            controlled_vocabulary = response.parse()
            assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncControlledVocabularies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCript) -> None:
        controlled_vocabulary = await async_client.controlled_vocabularies.retrieve(
            "string",
        )
        assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCript) -> None:
        response = await async_client.controlled_vocabularies.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        controlled_vocabulary = await response.parse()
        assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCript) -> None:
        async with async_client.controlled_vocabularies.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            controlled_vocabulary = await response.parse()
            assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCript) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.controlled_vocabularies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCript) -> None:
        controlled_vocabulary = await async_client.controlled_vocabularies.list()
        assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCript) -> None:
        response = await async_client.controlled_vocabularies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        controlled_vocabulary = await response.parse()
        assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCript) -> None:
        async with async_client.controlled_vocabularies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            controlled_vocabulary = await response.parse()
            assert_matches_type(SchemaResponse, controlled_vocabulary, path=["response"])

        assert cast(Any, response.is_closed) is True
