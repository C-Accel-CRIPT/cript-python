### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

ref1 = Reference(type="web_site", title="https://app.criptapp.org")
cit1 = Citation(type="reference", reference=ref1)
process1 = Process(name="process1", type="mix", citation=[cit1])
exp1 = Experiment(name="exp1", process=[process1])
col1=Collection(name="col1", experiment=[exp1])

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```


## Attributes
| attribute | type      | example                                    | description                                   | required      | vocab |
|-----------|-----------|--------------------------------------------|-----------------------------------------------|---------------|-------|
| type      | str       | journal_article                            | type of literature                            | True          | [Name](https://app.criptapp.org/vocab/reference_type)  |
| title     | str       | 'Living' Polymers                          | title of publication                          | True          |       |
| author    | str       | Michael Szwarc, Bradley Olsen              | list of authors comma separated               |               |       |
| journal   | str       | Nature                                     | journal of the publication                    |               |       |
| publisher | str       | Springer                                   | publisher of publication                      |               |       |
| year      | int       | 1956                                       | year of publication                           |               |       |
| volume    | int       | 178                                        | volume of publication                         |               |       |
| issue     | int       | 0                                          | issue of publication                          |               |       |
| pages     | str       | 1168, 1169                                 | page range of publication                     |               |       |
| doi       | str       | 10.1038/1781168a0                          | DOI: digital object identifier                | Conditionally |       |
| issn      | str       | 1476-4687                                  | ISSN: international standard serial number    | Conditionally |       |
| arxiv_id  | str       | 1501                                       | arXiv identifier                              |               |       |
| pmid      | int       | ########                                   | PMID: PubMed ID                               |               |       |
| website   | str       | https://www.nature.com/artic les/1781168a0 | website where the publication can be accessed |               |       |


### Delete
[Generic Deletion](../delete.md)