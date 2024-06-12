### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation
- Every material used in the other nodes needs to be added to the project

```python
from cript import *

mat1 = Material(name="unique material name")
inv1 = Inventory(name="inv1", material=[mat1])
col1 = Collection(name="col1", inventory=[inv1])
proj = Project(
    name="Change Project Name",
    collection=[col1],
    material=[mat1],
)

print(proj)
```

### Fields

| Attribute  | Type             | Required |
|------------|------------------|----------|
| name       | string           | t        |
| material   | List[[Material](../material)] | o        |
| notes      | str              | o        |

### Delete
[Generic Deletion](../delete.md)