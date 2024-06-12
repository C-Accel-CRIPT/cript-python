### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

prop1 = Property(key="air_flow", type="number", unit="L/s", value=1)
mat1=Material(name="col1", property=[prop1])

proj = Project(
    name="Change Project Name",
    material=[mat1]
)

print(proj)
```

## Attributes

| attribute           | type               | example                                  | description                                                                   | required   | vocab   |
|---------------------|-------------------|-----------------------------------------|------------------------------------------------------------------------------|----------|-------|
| **key**             | str                | enthalpy                                 | type of property                                                               | **True**    | [Material (Name)](https://app.criptapp.org/vocab/material_property_key) <br>  [Process (Name)](https://app.criptapp.org/vocab/process_property_key) <br>   [ComputationProcess (Name)](https://app.criptapp.org/vocab/computational_process_property_key)     |
| **type**            | str                | min                                      | type of value stored                                                           | **True**    | [Material (Value_type)](https://app.criptapp.org/vocab/material_property_key) <br>  [Process (Name)](https://app.criptapp.org/vocab/process_type) <br>   [ComputationProcess (Name)](https://app.criptapp.org/vocab/computational_process_type)         |
| **value**           | Any                | 1.23                                     | value or quantity                                                              | **True**    |         |
| **unit**            | str                | gram                                     | unit for value                                                                 | **True**    |         |
| **uncertainty**     | Number             | 0.1                                      | uncertainty of value                                                           |           |         |
| **uncertainty_type**| str                | standard_deviation                       | type of uncertainty                                                            |           | [Name](https://app.criptapp.org/vocab/uncertainty_type)   |
| **component**       | list[[Material](../material)]     |                                         | material that the property relates to**                                       |           |         |
| **structure**         | str                | {[\[\\]\\[$\\]\\[C:1\\]\\[C:1\\]\\[$\\]  | specific chemical structure associate with the property with atom mappings**   |           |         |
| **method**            | str                | sec                                      | approach or source of property data                                           |           | [Material (Method)](https://app.criptapp.org/vocab/material_property_key) <br>  [Process (Method)](https://app.criptapp.org/vocab/process_property_key) <br>   [ComputationProcess (Method)](https://app.criptapp.org/vocab/computational_process_property_key)   |
| **sample_preparation**| Process            |                                         | sample preparation                                                             |           |         |
| **condition**         | list[[Condition](../condition)]    |                                         | conditions under which the property was measured                               |           |         |
| **data**              | Data               |                                         | data node                                                                     |           |         |
| **computation**       | list[[Computation](../computation)]  |                                         | computation method that produced property                                      |           |         |
| **citation**          | list[[Citation](../citation)]     |                                         | reference to a book, paper, or scholarly work                                  |           |         |
| **notes**             | str                |                                         | miscellaneous information, or custom data structure   (e.g.; JSON)              |           |         |

### Delete
[Generic Deletion](../delete.md)