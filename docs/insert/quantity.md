### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *



mat1 = Material(name="mat1")
qnt1 = Quantity(key="mass", value=2, unit="kg")
ingredient = Ingredient(material=mat1, quantity=qnt1)
process1 = Process(name="process1", type="mix")
exp1 = Experiment(name="exp1", process=[process1])
col1 = Collection(name="col1", experiment=[exp1])

proj = Project(
    name="Change Project Name",
    collection=[col1],
    material=[mat1],
)

print(proj)
```

## Attributes

| attribute        | type    | example | description          | required | vocab |
|------------------|---------|---------|----------------------|----------|-------|
| key              | str     | mass    | type of quantity     | True     | [Name](https://app.criptapp.org/vocab/quantity_key)  |
| value            | Any     | 1.23    | amount of material   | True     | [Value_type](https://app.criptapp.org/vocab/quantity_key)      |
| unit             | str     | gram    | unit for quantity    | True     | [Si_unit](https://app.criptapp.org/vocab/quantity_key)      |
| uncertainty      | Number  | 0.1     | uncertainty of value |          |       |
| uncertainty_type | str     | std     | type of uncertainty  |          | [Name](https://app.criptapp.org/vocab/uncertainty_type)  |

### Delete
[Generic Deletion](../delete.md)