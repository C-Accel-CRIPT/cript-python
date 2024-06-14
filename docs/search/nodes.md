# Search nodes

```python
from cript import *

result = Search(node="Material", q="tol", filters={"limit": 100})

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
| exact      | bool, default 0  | o        |
| case_sensitive| bool, default 0 | o      |