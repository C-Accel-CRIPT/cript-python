# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cript import Cript, AsyncCript
from cript.types import SchemaResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchema:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Cript) -> None:
        schema = client.schema.retrieve()
        assert_matches_type(SchemaResponse, schema, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Cript) -> None:
        response = client.schema.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaResponse, schema, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Cript) -> None:
        with client.schema.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSchema:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCript) -> None:
        schema = await async_client.schema.retrieve()
        assert_matches_type(SchemaResponse, schema, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCript) -> None:
        response = await async_client.schema.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaResponse, schema, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCript) -> None:
        async with async_client.schema.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True
