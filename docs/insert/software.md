### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

software1 = Software(name="Test", version="1.0")
soft1 = SoftwareConfiguration(software=software1)
comp1 = Computation(name="comp1", type="MC", software_configuration=[soft1])
exp1 = Experiment(name="exp1", computation=[comp1])
col1=Collection(name="col1", experiment=[exp1])

proj = Project(
    name="CHANGE PROJECT NAME",
    collection=[col1]
)

print(proj)
```

## Attributes

| attribute | type | example    | description                   | required | vocab |
|-----------|------|------------|-------------------------------|----------|-------|
| name      | str  | LAMMPS     | type of literature            | True     |       |
| version   | str  | 23Jun22    | software version              | True     |       |
| source    | str  | lammps.org | source of software            |          |       |

### Delete
[Generic Deletion](../delete.md)