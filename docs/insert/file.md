### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

file1 = File(type=f"data", source="myfile.txt")
data = Data(name="mydata", file=[file1])
exp1 = Experiment(name="exp1")
col1=Collection(name="col1", experiment=exp1)

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```

## Attributes

| Attribute       | Type | Example                                                                                               | Description                                                                 | Required | Vocab |
|-----------------|------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------|-------|
| name            | str  | `"my file name"`                                                                                      | descriptive name for the file node                                          | False, defaults to source file name | |
| source          | str  | `"path/to/my/file"` or `"https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system"` | source to the file can be URL or local path                                 | True     |                            |
| type            | str  | `"logs"`                                                                                              |                                                                             | True     |[Name](https://app.criptapp.org/vocab/file_type/)|
| extension       | str  | `".csv"`                                                                                              | file extension                                                              | False    |                            |
| data_dictionary | str  | `"my extra info in my data dictionary"`                                                               | set of information describing the contents, format, and structure of a file | False    |                            |
| notes           | str  |                                                                                                       | miscellaneous information, or custom data structure (e.g.; JSON)            |          |                            |



### Delete
[Generic Deletion](../delete.md)