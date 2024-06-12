### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation
- Only one algorithm can be added if any modifications are made subsequently after creation the first algorithm in the software will be updated

```python
from cript import *

algorithm1 = Algorithm(key="advanced_sampling", type="analysis")
software1 = Software(name="Test", version="1.0")
soft1 = SoftwareConfiguration(software=software1, algorithm=[algorithm1])
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

| Keys      | Type            | Example                                      | Description                                            | Required | Vocab |
|-----------|-----------------|----------------------------------------------|--------------------------------------------------------|----------|-------|
| key       | str             | ensemble, thermo-barostat                    | system configuration, algorithms used in a computation | True     | [Name](https://app.criptapp.org/vocab/algorithm_key)  |
| type      | str             | NPT for ensemble, Nose-Hoover for thermostat | specific type of configuration, algorithm              | True     | [Name](https://app.criptapp.org/vocab/algorithm_type)     |
| parameter | list[[Parameter](../parameter)] |                              | setup associated parameters                            |          |       |
| citation  | Citation        |                                              | reference to a book, paper, or scholarly work          |          |       |


### Delete

[Generic Deletion](../delete.md)