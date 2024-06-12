### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

mat1=Material(name="col1")

proj = Project(
    name="Change Project Name",
    material=[mat1]
)

print(proj)
```

## Attributes
| attribute                 | type                                                                 | example                                           | description                                         | required    | vocab |
|---------------------------|----------------------------------------------------------------------|---------------------------------------------------|-----------------------------------------------------|-------------|-------|
| name                      | str                                                                  |                                                   | unique name of the material                         |   t         |       |
| component                 | list[[Material](../material)]                                        |                                                   | list of component that make up the mixture          |             |       |
| property                  | list[[Property](../property)]                                        |                                                   | material properties                                 |             |       |
| computational_forcefield  | list[[ComputationalForcefield](../computational_forcefield)]         |                                                   | computation forcefield                              | Conditional |       |
| keyword                   | str                                                                  | [thermoplastic, homopolymer, linear, polyolefins] | words that classify the material                    |             | [Name](https://app.criptapp.org/vocab/material_keyword)  |
| notes                     | str                                                                  | "my awesome notes"                                | miscellaneous information, or custom data structure |             |       |
| amino_acid                | str                                                                  | "LeuProHis"                                       | if the material is an amino acid sequence, list it. | Conditional |       |
| bigsmiles                 | str                                                                  | "CC{[$][$]CC[$][]}"                               | BigSMILES string for polymer                        | Conditional |       |
| chem_formula              | str                                                                  | "C22H33NO10"                                      | Chemical formula of the material or monomer         | Conditional |       |
| chem_repeat               | str                                                                  | "C=Cc1ccccc1"                                     | Chemical formula of the repeat unit                 | Conditional |       |
| chemical_id               | str                                                                  | "126094"                                          | Unique chemical ID                                  | Conditional |       |
| inchi                     | str                                                                  | "InChI=1S/H2O/h1H2"                               | InChI string of the chemical                        | Conditional |       |
| inchi_key                 | str                                                                  | "XLYOFNOQVPJJNP-UHFFFAOYSA-N"                     | InChI key of the chemical                           | Conditional |       |
| lot_number                | str                                                                  | "123"                                             | Lot number of the chemical                          | Conditional |       |
| pubchem_cid               | int                                                                  | 962                                               | PubChemID of the chemical                           | Conditional |       |
| smiles                    | str                                                                  | "O"                                               | Smiles string of the chemical                       | Conditional |       |
| vendor                    | str                                                                  | "fisher scientific"                               | Vendor the chemical was purchased from              | Conditional |       |

### Delete
[Generic Deletion](../delete.md)