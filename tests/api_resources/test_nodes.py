# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import pytest

from cript import Cript
from cript.types import Node
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cript) -> None:
        node = client.nodes.create(
            node="project",
            body={
                "node": ["Project"],
                "name": "proj1",
            },
        )
        assert_matches_type(Node, node, path=["response"])

    # @parametrize
    # def test_raw_response_create(self, client: Cript) -> None:
    #     response = client.nodes.with_raw_response.create(
    #         "string",
    #         node="string",
    #         body={
    #             "node": ["Project"],
    #             "name": "proj1",
    #         },
    #     )

    #     assert response.is_closed is True
    #     assert response.http_request.headers.get("X-Stainless-Lang") == "python"
    #     node = response.parse()
    #     assert_matches_type(Node, node, path=["response"])

    # @parametrize
    # def test_streaming_response_create(self, client: Cript) -> None:
    #     with client.nodes.with_streaming_response.create(
    #         "string",
    #         node="string",
    #         body={
    #             "node": ["Project"],
    #             "name": "proj1",
    #         },
    #     ) as response:
    #         assert not response.is_closed
    #         assert response.http_request.headers.get("X-Stainless-Lang") == "python"

    #         node = response.parse()
    #         assert_matches_type(Node, node, path=["response"])

    #     assert cast(Any, response.is_closed) is True

    # @parametrize
    # def test_path_params_create(self, client: Cript) -> None:
    #     with pytest.raises(ValueError, match=r"Expected a non-empty value for `node` but received ''"):
    #         client.nodes.with_raw_response.create(
    #             "string",
    #             node="",
    #             body={
    #                 "node": ["Project"],
    #                 "name": "proj1",
    #             },
    #         )

    #     with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
    #         client.nodes.with_raw_response.create(
    #             "",
    #             node="string",
    #             body={
    #                 "node": ["Project"],
    #                 "name": "proj1",
    #             },
    #         )

    # @parametrize
    # def test_method_retrieve(self, client: Cript) -> None:
    #     node = client.nodes.retrieve(
    #         "string",
    #         node="string",
    #     )
    #     assert_matches_type(Node, node, path=["response"])

    # @parametrize
    # def test_raw_response_retrieve(self, client: Cript) -> None:
    #     response = client.nodes.with_raw_response.retrieve(
    #         "string",
    #         node="string",
    #     )

    #     assert response.is_closed is True
    #     assert response.http_request.headers.get("X-Stainless-Lang") == "python"
    #     node = response.parse()
    #     assert_matches_type(Node, node, path=["response"])

    # @parametrize
    # def test_streaming_response_retrieve(self, client: Cript) -> None:
    #     with client.nodes.with_streaming_response.retrieve(
    #         "string",
    #         node="string",
    #     ) as response:
    #         assert not response.is_closed
    #         assert response.http_request.headers.get("X-Stainless-Lang") == "python"

    #         node = response.parse()
    #         assert_matches_type(Node, node, path=["response"])

    #     assert cast(Any, response.is_closed) is True

    # @parametrize
    # def test_path_params_retrieve(self, client: Cript) -> None:
    #     with pytest.raises(ValueError, match=r"Expected a non-empty value for `node` but received ''"):
    #         client.nodes.with_raw_response.retrieve(
    #             "string",
    #             node="",
    #         )

    #     with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
    #         client.nodes.with_raw_response.retrieve(
    #             "",
    #             node="string",
    #         )

    # @parametrize
    # def test_method_update(self, client: Cript) -> None:
    #     node = client.nodes.update(
    #         "string",
    #         node="string",
    #         body={
    #             "node": ["Project"],
    #             "name": "updated_node_name",
    #         },
    #     )
    #     assert_matches_type(Node, node, path=["response"])

    # @parametrize
    # def test_raw_response_update(self, client: Cript) -> None:
    #     response = client.nodes.with_raw_response.update(
    #         "string",
    #         node="string",
    #         body={
    #             "node": ["Project"],
    #             "name": "updated_node_name",
    #         },
    #     )

    #     assert response.is_closed is True
    #     assert response.http_request.headers.get("X-Stainless-Lang") == "python"
    #     node = response.parse()
    #     assert_matches_type(Node, node, path=["response"])

    # @parametrize
    # def test_streaming_response_update(self, client: Cript) -> None:
    #     with client.nodes.with_streaming_response.update(
    #         "string",
    #         node="string",
    #         body={
    #             "node": ["Project"],
    #             "name": "updated_node_name",
    #         },
    #     ) as response:
    #         assert not response.is_closed
    #         assert response.http_request.headers.get("X-Stainless-Lang") == "python"

    #         node = response.parse()
    #         assert_matches_type(Node, node, path=["response"])

    #     assert cast(Any, response.is_closed) is True

    # @parametrize
    # def test_path_params_update(self, client: Cript) -> None:
    #     with pytest.raises(ValueError, match=r"Expected a non-empty value for `node` but received ''"):
    #         client.nodes.with_raw_response.update(
    #             "string",
    #             node="",
    #             body={
    #                 "node": ["Project"],
    #                 "name": "updated_node_name",
    #             },
    #         )

    #     with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
    #         client.nodes.with_raw_response.update(
    #             "",
    #             node="string",
    #             body={
    #                 "node": ["Project"],
    #                 "name": "updated_node_name",
    #             },
    #         )

    # @parametrize
    # def test_method_delete(self, client: Cript) -> None:
    #     node = client.nodes.delete(
    #         "string",
    #         node="string",
    #         body={
    #             "node": ["Project"],
    #             "notes": None,
    #         },
    #     )
    #     assert_matches_type(Node, node, path=["response"])

    # @parametrize
    # def test_raw_response_delete(self, client: Cript) -> None:
    #     response = client.nodes.with_raw_response.delete(
    #         "string",
    #         node="string",
    #         body={
    #             "node": ["Project"],
    #             "notes": None,
    #         },
    #     )

    #     assert response.is_closed is True
    #     assert response.http_request.headers.get("X-Stainless-Lang") == "python"
    #     node = response.parse()
    #     assert_matches_type(Node, node, path=["response"])

    # @parametrize
    # def test_streaming_response_delete(self, client: Cript) -> None:
    #     with client.nodes.with_streaming_response.delete(
    #         "string",
    #         node="string",
    #         body={
    #             "node": ["Project"],
    #             "notes": None,
    #         },
    #     ) as response:
    #         assert not response.is_closed
    #         assert response.http_request.headers.get("X-Stainless-Lang") == "python"

    #         node = response.parse()
    #         assert_matches_type(Node, node, path=["response"])

    #     assert cast(Any, response.is_closed) is True

    # @parametrize
    # def test_path_params_delete(self, client: Cript) -> None:
    #     with pytest.raises(ValueError, match=r"Expected a non-empty value for `node` but received ''"):
    #         client.nodes.with_raw_response.delete(
    #             "string",
    #             node="",
    #             body={
    #                 "node": ["Project"],
    #                 "notes": None,
    #             },
    #         )

    #     with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
    #         client.nodes.with_raw_response.delete(
    #             "",
    #             node="string",
    #             body={
    #                 "node": ["Project"],
    #                 "notes": None,
    #             },
    #         )
