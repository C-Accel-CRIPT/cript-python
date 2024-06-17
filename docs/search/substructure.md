# Substructure search

## Bigsmiles

```python
from cript import *

result = Search(node="Material", q="{[][<]CCO[>][]}", field="bigsmiles", filters={"limit": 10})

for r in result:
    print(r)
```


## Smiles

```python
from cript import *

result = Search(node="Material", q="CCO", field="smiles", filters={"limit": 10})

for r in result:
    print(r)
```

### Fields

| Attribute  | Type             | Required |
|------------|------------------|----------|
| node       | string or class  | t        |
| q          | str              | t        |
| field      | str              | o        |
| filters    | Dict             | o        |

#### Filters

| Attribute  | Type             | Required |
|------------|------------------|----------|
| limit      | int, default 100 | o        |
