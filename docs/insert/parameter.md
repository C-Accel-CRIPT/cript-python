### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation
- Only one parameter with the same key can be added if any modifications are made subsequently after creation the parameter with the same key will be updated

```python
from cript import *

param1 = Parameter(key="bond_type", value="1")
algorithm1 = Algorithm(key="advanced_sampling", type="analysis", parameter=[param1])
software1 = Software(name="Test", version="1.0")
soft1 = SoftwareConfiguration(software=software1, algorithm=algorithm1)
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

| attribute | type | example | description        | required | vocab |
|-----------|------|---------|--------------------|----------|-------|
| key       | str  |         | key for identifier | True     | [Name](https://app.criptapp.org/vocab/parameter_key)  |
| value     | any  |         | value              | True     | [Value Type](https://app.criptapp.org/vocab/parameter_key)      |
| unit      | str  |         | unit for parameter | Conditional| [si_unit](https://app.criptapp.org/vocab/parameter_key)      |

### Delete
[Generic Deletion](../delete.md)