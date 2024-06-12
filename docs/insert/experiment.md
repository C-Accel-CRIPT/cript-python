### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

exp1 = Experiment(name="exp1")
col1=Collection(name="col1", experiment=exp1)

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
| process    | List[[Process](../process)]    | o        |
| computation| List[[Computation](../computation)]| o        |
| computation_process   | List[[ComputationProcess](../computation_process)]   | o        |
| data   | List[[Data](../data)]   | o        |
| citation   | List[[Citation](../citation)]   | o        |
| funding        | str              | o        |
| notes       | str              | o        |


### Delete
[Generic Deletion](../delete.md)