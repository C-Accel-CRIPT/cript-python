# Delete
- This is the generic deletion workflow

## Delete Node cascade
- This operation will delete the node and all its children
- Call delete() on an initialized object

###  Delete by uuid
```python
from cript import *

proj = Project(uuid=UUID_OF_THE_NODE)
proj.delete()

```

### Delete by reference
```python
from cript import *

col1=Collection(name="col1")
proj = Project(uuid=UUID_OF_THE_NODE, collection=[col1])

col1.delete() # Deletes the collection named col1 and all its children

```

## Delete Attributes
- Call delete() on an initialized object
- Set the attribute to None to remove it
- If the attribute is a child node then setting it to None unlinks all its children

### Delete an attribute

#### By uuid

```python
from cript import *

proj = Project(uuid=UUID_OF_THE_NODE, notes="test")
proj.delete(notes=None)

```

#### By reference

```python
from cript import *

proj = Project(name="Project Name", notes="test")
proj.delete(notes=None)

```

## Unlink All child nodes

```python
from cript import *

col1=Collection(name="col1")
col2=Collection(name="col2")
proj = Project(uuid=UUID_OF_THE_NODE, collection=[col1,col2])
proj.delete(collection=None)

```

## Unlink One child node

```python
from cript import *

col1=Collection(name="col1")
col2=Collection(name="col2")
proj = Project(uuid=UUID_OF_THE_NODE, collection=[col1,col2])
proj.delete(collection=[child1]) # will unlink only child1

```