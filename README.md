# Cript Python API library

[![PyPI version](https://img.shields.io/pypi/v/cript.svg)](https://pypi.org/project/cript/)

The Cript Python library provides convenient access to the Cript REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It is partially generated with [Stainless](https://www.stainlessapi.com/).

## Documentation

The full API of this library can be found in [c-accel-cript.github.io/cript-python](https://c-accel-cript.github.io/cript-python).

## Installation

```sh
# install from this staging repo
pip install git+https://github.com/c-accel-cript/cript-python.git
```

## Config

Create a `.env` file and copy your API KEYS from the CRIPT website->Account->Security Settings

```
CRIPT_API_KEY=API Token
CRIPT_STORAGE_KEY=Storage Token
CRIPT_LOG=
```

The log level can be set to DEBUG, INFO, ERROR if ommited then the logs wont show.
> [!NOTE]
> Once this package is [published to PyPI](https://app.stainlessapi.com/docs/guides/publish), this will become: `pip install --pre cript`

## Usage

The full API of this library can be found in [c-accel-cript.github.io/cript-python](https://c-accel-cript.github.io/cript-python).

```python
from cript import *

proj = Project(
    name="Change Project Name",
    notes="my notes",
)

print(proj)
```

## Advanced
### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/#client-instances) functionality

```python
from cript import Cript, DefaultHttpxClient

client = Cript(
    # Or use the `CRIPT_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

### Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `cript.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `cript.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `cript.APIError`.

```python
import cript
from cript import Cript

client = Cript()

try:
    client.schema.retrieve()
except cript.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except cript.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except cript.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from cript import Cript

# Configure the default for all requests:
client = Cript(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).schema.retrieve()
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from cript import Cript

# Configure the default for all requests:
client = Cript(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Cript(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).schema.retrieve()
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `CRIPT_LOG` to `debug`.

```shell
$ export CRIPT_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) will be respected when making this
request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).


## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/c-accel-cript/cript-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.8 or higher.
