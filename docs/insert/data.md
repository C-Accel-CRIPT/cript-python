### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

data = Data(name="mydata")
exp1 = Experiment(name="exp1")
col1=Collection(name="col1", experiment=exp1)

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```

## Attributes
| Attribute           | Type                                              | Example                    | Description                                                                                  | Required | Vocab |
|---------------------|---------------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------|----------|-------|
| name                | str                                               | `"my_data_name"`           | Name of the data node                                                                        | True     |       |
| type                | str                                               | `"nmr_h1"`                 |                                                                                              | True     |[Name](https://app.criptapp.org/vocab/data_type/)|
| file                | List[[File](../file)]         | `[file_1, file_2, file_3]` | list of file nodes                                                                                               | False    |       |
| sample_preparation  | [Process](../process)                             |                            |                                                                                              | False    |       |
| computation         | List[[Computation](../computation)]               |                            | data produced from this Computation method                                                   | False    |       |
| computation_process | [ComputationProcess](../computation_process)    |                            | data was produced from this computation process                                                | False    |       |
| material            | List[[Material](../material)]                   |                            | materials with attributes associated with the data node                                        | False    |       |
| process             | List[[Process](../process)]                     |                            | processes with attributes associated with the data node                                        | False    |       |
| citation            | [Citation](../citation)                           |                            | reference to a book, paper, or scholarly work                                                | False    |       |
| notes               | str                                               | "my awesome notes"         | miscellaneous information, or custom data structure                                          | False    |       |



### Delete
[Generic Deletion](../delete.md)