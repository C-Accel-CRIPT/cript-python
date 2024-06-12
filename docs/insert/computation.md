### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

comp1 = Computation(name=generic_computation, type="MC")
exp1 = Experiment(name="exp1", computation=[comp1])
col1=Collection(name="col1", experiment=exp1)

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```

### Fields

## Attributes
| attribute                | type                          | example                               | description                                   | required | vocab |
|--------------------------|-------------------------------|---------------------------------------|-----------------------------------------------|----------|-------|
| name                     | str                           |                                       |                                               | True     |       |
| type                     | str                           | general molecular dynamics simulation | category of computation                       | True     | [Name](https://app.criptapp.org/vocab/computation_type)  |
| input_data               | list[[Data](../data)]                    |                                       | input data nodes                              |          |       |
| output_data              | list[[Data](../data)]                    |                                       | output data nodes                             |          |       |
| software_configuration | list[[SoftwareConfiguration](../software_configuration)] |                                       | software and algorithms used                  |          |       |
| condition                | list[[Condition](../condition)]               |                                       | setup information                             |          |       |
| prerequisite_computation | [Computation](../computation)                   |                                       | prior computation method in chain             |          |       |
| citation                 | list[[Citation](../citation)]                |                                       | reference to a book, paper, or scholarly work |          |       |
| notes                    | str                           |                                       | additional description of the step            |          |       |



### Delete
[Generic Deletion](../delete.md)