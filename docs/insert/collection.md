### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

col1=Collection(name="col1")

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```

### Fields

| Attribute  | Type             | Required |
|------------|------------------|----------|
| name       | string           | t        |
| experiment | List[[Experiment](../experiment)] | o        |
| inventory  | List[[Inventory](../inventory)]  | o        |
| citation   | List[[Citation](../citation)]   | o        |
| doi        | str              | o        |
| notes      | str              | o        |

### Delete
[Generic Deletion](../delete.md)
