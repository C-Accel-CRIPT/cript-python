### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

comp_forcefield= ComputationalForcefield(key="mmff", building_block="atom")
mat1=Material(name="col1", computational_forcefield=comp_forcefield)

proj = Project(
    name="Change Project Name",
    material=[mat1]
)

print(proj)
```

## Attributes
| attribute              | type           | example                                                                | description                                                              | required | vocab |
|------------------------|----------------|------------------------------------------------------------------------|--------------------------------------------------------------------------|----------|-------|
| key                    | str            | CHARMM27                                                               | type of forcefield                                                       | True     | [Name](https://app.criptapp.org/vocab/data_type)  |
| building_block         | str            | atom                                                                   | type of building block                                                   | True     | [Name](https://app.criptapp.org/vocab/building_block)  |
| coarse_grained_mapping | str            | SC3 beads in MARTINI forcefield                                        | atom to beads mapping                                                    |          |       |
| implicit_solvent       | str            | water                                                                  | Name of implicit solvent                                                 |          |       |
| source                 | str            | package in GROMACS                                                     | source of forcefield                                                     |          |       |
| description            | str            | OPLS forcefield with partial charges calculated via the LBCC algorithm | description of the forcefield and any modifications that have been added |          |       |
| data                   | [Data](../data)|                                                                        | details of mapping schema and forcefield parameters                      |          |       |
| citation               | list[[Citation](../citation)] |                                                         | reference to a book, paper, or scholarly work                            |          |       |


### Delete
[Generic Deletion](../delete.md)