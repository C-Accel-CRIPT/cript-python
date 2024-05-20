# Shared Types

```python
from cript.types import SearchResponse
```

# Schema

Methods:

- <code title="get /schema">client.schema.<a href="./src/cript/resources/schema.py">retrieve</a>() -> <a href="./src/cript/types/schema_response.py">SchemaResponse</a></code>

# Nodes

Types:

```python
from cript.types import Node
```

Methods:

- <code title="post /{node}/{uuid}">client.nodes.<a href="./src/cript/resources/nodes.py">create</a>(uuid, \*, node, \*\*<a href="src/cript/types/node_create_params.py">params</a>) -> <a href="./src/cript/types/node.py">Node</a></code>
- <code title="get /{node}/{uuid}">client.nodes.<a href="./src/cript/resources/nodes.py">retrieve</a>(uuid, \*, node) -> <a href="./src/cript/types/node.py">Node</a></code>
- <code title="patch /{node}/{uuid}">client.nodes.<a href="./src/cript/resources/nodes.py">update</a>(uuid, \*, node, \*\*<a href="src/cript/types/node_update_params.py">params</a>) -> <a href="./src/cript/types/node.py">Node</a></code>
- <code title="delete /{node}/{uuid}">client.nodes.<a href="./src/cript/resources/nodes.py">delete</a>(uuid, \*, node, \*\*<a href="src/cript/types/node_delete_params.py">params</a>) -> <a href="./src/cript/types/node.py">Node</a></code>

# Search

## Nodes

Methods:

- <code title="get /search/{node_name}">client.search.nodes.<a href="./src/cript/resources/search/nodes/nodes.py">list</a>(node_name, \*\*<a href="src/cript/types/search/node_list_params.py">params</a>) -> <a href="./src/cript/types/shared/search_response.py">SearchResponse</a></code>

### Children

Methods:

- <code title="get /search/exact/{node_name}/{uuid}/{child_node}">client.search.nodes.children.<a href="./src/cript/resources/search/nodes/children.py">list</a>(child_node, \*, node_name, uuid, \*\*<a href="src/cript/types/search/nodes/child_list_params.py">params</a>) -> <a href="./src/cript/types/shared/search_response.py">SearchResponse</a></code>

# ControlledVocabularies

Types:

```python
from cript.types import SchemaResponse
```

Methods:

- <code title="get /cv/{key}">client.controlled_vocabularies.<a href="./src/cript/resources/controlled_vocabularies.py">retrieve</a>(key) -> <a href="./src/cript/types/schema_response.py">SchemaResponse</a></code>
- <code title="get /cv">client.controlled_vocabularies.<a href="./src/cript/resources/controlled_vocabularies.py">list</a>() -> <a href="./src/cript/types/schema_response.py">SchemaResponse</a></code>
