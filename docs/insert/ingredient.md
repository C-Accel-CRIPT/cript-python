### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *


mat1 = Material(name="mat1")
qnt1 = Quantity(key="key", value="value", unit="unit")
ingredient = Ingredient(material=mat1, quantity=[qnt1])
process1 = Process(name="process1", type="mix")
exp1 = Experiment(name="exp1", process=[process1])
col1 = Collection(name="col1", experiment=exp1)

proj = Project(
    name="Change Project Name",
    collection=[col1],
    material=[mat1],
)

print(proj)
```

## Attributes

| attribute  | type           | example  | description            | required | vocab |
|------------|----------------|----------|------------------------|----------|-------|
| material   | [Material](../material)   |          | material               | True     |       |
| quantity   | list[[Quantity](../quantity)] |          | quantities             | True     |       |
| keyword    | str      | catalyst | comma separated list of keywords |          | [Name](https://app.criptapp.org/vocab/ingredient_keyword)  |

### Delete
[Generic Deletion](../delete.md)