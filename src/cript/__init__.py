# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from . import types
from ._types import NOT_GIVEN, NoneType, NotGiven, Transport, ProxiesTypes
from ._utils import file_from_path, camel_case_to_snake_case, extract_node_from_result
from ._client import Cript, Client, Stream, Timeout, Transport, AsyncCript, AsyncClient, AsyncStream, RequestOptions
from ._models import BaseModel
from ._version import __title__, __version__
from ._response import APIResponse as APIResponse, AsyncAPIResponse as AsyncAPIResponse
from ._constants import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES, DEFAULT_CONNECTION_LIMITS
from ._exceptions import (
    APIError,
    CriptError,
    ConflictError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    APIConnectionError,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
    UnprocessableEntityError,
    APIResponseValidationError,
)
from ._base_client import DefaultHttpxClient, DefaultAsyncHttpxClient
from ._utils._logs import setup_logging as _setup_logging
from dotenv import load_dotenv, find_dotenv
from .nodes import (
    Project,
    Collection,
    Experiment,
    Material,
    Algorithm,
    Citation,
    Computation,
    ComputationProcess,
    ComputationalForcefield,
    Condition,
    Data,
    Equipment,
    File,
    Ingredient,
    Inventory,
    Parameter,
    Process,
    Property,
    Quantity,
    Reference,
    Software,
    SoftwareConfiguration,
    User,
)

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "NotGiven",
    "NOT_GIVEN",
    "CriptError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "Cript",
    "AsyncCript",
    "file_from_path",
    "BaseModel",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_CONNECTION_LIMITS",
    "DefaultHttpxClient",
    "DefaultAsyncHttpxClient",
    "Project",
    "Collection",
    "Experiment",
    "Material",
    "Algorithm",
    "Citation",
    "Computation",
    "ComputationProcess",
    "ComputationalForcefield",
    "Condition",
    "Data",
    "Equipment",
    "File",
    "Ingredient",
    "Inventory",
    "Parameter",
    "Process",
    "Property",
    "Quantity",
    "Reference",
    "Software",
    "SoftwareConfiguration",
    "User",
]

load_dotenv(find_dotenv(usecwd=True), encoding="utf-8")
_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# cript._exceptions.NotFoundError -> cript.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            __locals[__name].__module__ = "cript"
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
