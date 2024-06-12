### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

file1 = File(type=f"logs", source="https://criptapp.org/file1.txt")
input_data1 = Data(type="nmr_h1", file=[file1])
file2=File(type=f"logs", source="https://criptapp.org/file2.txt")
output_data1 = Data(type="nmr_h1", file=[file2])
comp_process1 = ComputationProcess(name="compr1", type="reaction", input_data=[input_data1], output_data=[output_data1])

exp1 = Experiment(name="exp1", computation_process=[comp_process1])
col1=Collection(name="col1", experiment=[exp1])

proj = Project(
    name=generic_name,
    collection=[col1]
)

print(proj)
```

### Fields

## Attributes
| attribute                | type                          | example                               | description                                   | required | vocab |
|--------------------------|-------------------------------|---------------------------------------|-----------------------------------------------|----------|-------|
| type                     | str                           | general molecular dynamics simulation | category of computation                       | True     | [Name](https://app.criptapp.org/vocab/computational_process_type)  |
| input_data               | list[[Data](../data)]         |                                       | input data nodes                              | True     |       |
| output_data              | list[[Data](../data)]         |                                       | output data nodes                             |          |       |
| ingredient               | list[[Ingredient](../ingredient)]|                                    | ingredients                                   | True     |       |
| software_ configurations | list[SoftwareConfiguration](../software_configuration) |              | software and algorithms used                  |          |       |
| condition                | list[[Condition](../condition)]|                                      | setup information                             |          |       |
| property                 | list[[Property](../property)] |                                       | computation process properties                |          |       |
| citation                 | list[[Citation](../citation)] |                                       | reference to a book, paper, or scholarly work |          |       |
| notes                    | str                           |                                       | additional description of the step            |          |       |


### Delete
[Generic Deletion](../delete.md)