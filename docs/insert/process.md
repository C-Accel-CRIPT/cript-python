### Usage

- Searches by name if the node doesn't exist it creates it otherwise updates it
- Idempotent operation

```python
from cript import *

process1 = Process(name="process1", type="mix")
exp1 = Experiment(name="exp1", process=[process1])
col1=Collection(name="col1", experiment=[exp1])

proj = Project(
    name="Change Project Name",
    collection=[col1]
)

print(proj)
```

## Attributes

| attribute               | type             | example                                                                         | description                                                         | required | vocab |
|-------------------------|------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------|----------|-------|
| name                    | str              |                                                                                 | name                                                                | True     |        |
| type                    | str              | mix                                                                             | type of process                                                     | True     | [Name](https://app.criptapp.org/vocab/process_type)  |
| ingredient              | list[[Ingredient](../ingredient)] |                                                                                 | ingredients                                                         |          |       |
| description             | str              | To oven-dried 20 mL glass vial, 5 mL of styrene and 10 ml of toluene was added. | explanation of the process                                          |          |       |
| equipment               | list[[Equipment]((../equipment))]  |                                                                                 | equipment used in the process                                       |          |       |
| product                 | list[[Material(../material)]]   |                                                                                 | desired material produced from the process                          |          |       |
| waste                   | list[[Material](../material)]   |                                                                                 | material sent to waste                                              |          |       |
| prerequisite_ processes | list[[Process](../process)]    |                                                                                 | processes that must be completed prior to the start of this process |          |       |
| condition               | list[[Condition](../condition)]  |                                                                                 | global process condition                                            |          |       |
| property                | list[[Property](../property)]   |                                                                                 | process properties                                                  |          |       |
| keyword                 | list[str]        |                                                                                 | words that classify the process                                     |          | [Name](https://app.criptapp.org/vocab/process_keyword)  |
| citation                | list[[Citation](../citation)]   |                                                                                 | reference to a book, paper, or scholarly work                       |          |       |
| notes                   | str              |                                                                                 | miscellaneous information, or custom data structure                 |          |       |

### Delete
[Generic Deletion](../delete.md)