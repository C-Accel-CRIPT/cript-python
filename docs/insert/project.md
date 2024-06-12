### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

proj = Project(
    name="Change Project Name",
    notes="my notes",
)

print(proj)
```

### Attributes

| Attribute   | Type               | Description             | Required   | Limits  |
|------------|------------------|-----------------------|----------|--------|
| name         | string             | Unique name             | t          | MinLength: 2, MaxLength: 2,048       |
| collection   | List[[Collection](../collection)]   |           | o           | 1,000   |
| material     | List[[Material](../material)]    |           | o           | 1,000   |
| notes        | str                |                         | o           | MaxLength: 10,000 |

### Delete
[Generic Deletion](../delete.md)