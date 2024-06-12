### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

ref1 = Reference(type="web_site", title="https://app.criptapp.org")
cit1 = Citation(type="reference", reference=ref1)
process1 = Process(name="process1", type="mix", citation=[cit1])
exp1 = Experiment(name="exp1", process=[process1])
col1=Collection(name="col1", experiment=[exp1])

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```


## Attributes
| attribute | type      | example      | description                                   | required | vocab |
|-----------|-----------|--------------|-----------------------------------------------|----------|-------|
| type      | str       | derived_from | key for identifier                            | True     | [Name](https://app.criptapp.org/vocab/citation_type)  |
| reference | [Reference](../reference) |              | reference to a book, paper, or scholarly work | True     |       |                                                                           | miscellaneous information, or custom data structure                 |          |       |

### Delete
[Generic Deletion](../delete.md)