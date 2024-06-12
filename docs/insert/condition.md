### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

cond1 = Condition(key="key", type="type", value="value")
process1 = Process(name="process1", type="mix", condition=[cond1])
exp1 = Experiment(name="exp1", process=[process1])
col1=Collection(name="col1", experiment=exp1)

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```


## Attributes

| attribute        | type   | example                 | description                                                                            | required | vocab |
|------------------|--------|-------------------------|----------------------------------------------------------------------------------------|----------|-------|
| key              | str    | temp                    | type of condition                                                                      | True     | [Name](https://app.criptapp.org/vocab/condition_key)  |
| type             | str    | min                     | type of value stored, 'value' is just the number, 'min', 'max', 'avg', etc. for series | True     | [Value Type](https://app.criptapp.org/vocab/condition_key)  |
| descriptor       | str    | upper temperature probe | freeform description for condition                                                     |          |       |
| value            | Number | 1.23                    | value or quantity                                                                      | True     |       |
| unit             | str    | gram                    | unit for value                                                                         |          |       |
| uncertainty      | Number | 0.1                     | uncertainty of value                                                                   |          |       |
| uncertainty_type | str    | std                     | type of uncertainty                                                                    |          | [Name](https://app.criptapp.org/vocab/uncertainty_type)  |
| set_id           | int    | 0                       | ID of set (used to link measurements in as series)                                     |          |       |
| measurement _id  | int    | 0                       | ID for a single measurement (used to link multiple condition at a single instance)     |          |       |
| data             | List[[Data](../data)] |                         | detailed data associated with the condition                                            |          |       |

### Delete
[Generic Deletion](../delete.md)