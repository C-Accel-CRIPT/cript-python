### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

equip1 = Equipment(key="burner")
process1 = Process(name="process1", type="mix", equipment=[equip1])
exp1 = Experiment(name="exp1", process=[process1])
col1=Collection(name="col1", experiment=[exp1])

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```

## Attributes

| attribute   | type            | example                                       | description                                                                    | required | vocab |
|-------------|-----------------|-----------------------------------------------|--------------------------------------------------------------------------------|----------|-------|
| key         | str             | hot plate                                     | material                                                                       | True     | [Name](https://app.criptapp.org/vocab/equipment_key)  |
| description | str             | Hot plate with silicon oil bath with stir bar | additional details about the equipment                                         |          |       |
| condition   | list[[Condition](../condition)] |                               | conditions under which the property was measured                               |          |       |
| file        | list[[File](../file)]|                                          | list of file nodes to link to calibration or equipment specification documents |          |       |
| citation    | list[[Citation](../citation)]  |                                | reference to a book, paper, or scholarly work                                  |          |       |

### Delete
[Generic Deletion](../delete.md)