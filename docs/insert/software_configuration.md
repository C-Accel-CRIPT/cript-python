### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation
- Only one software configuration can be added if any modifications are made subsequently after creation the first software configuration in the computation will be updated


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

| keys                                             | type            | example | description                                                      | required | vocab |
|--------------------------------------------------|-----------------|---------|------------------------------------------------------------------|----------|-------|
| software                                         | [Software](../software)        |         | software used                                     | True     |       |
| algorithm                                        | list[[Algorithm](../algorithm)] |         | algorithms used                                  |          |       |
| notes                                            | str             |         | miscellaneous information, or custom data structure (e.g.; JSON) |          |       |
| citation                                         | list[[Citation](../citation)]  |         | reference to a book, paper, or scholarly work     |          |       |



### Delete
[Generic Deletion](../delete.md)