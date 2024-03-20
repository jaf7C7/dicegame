## Inheritance and Association

### Inheritance: "is a"

`Dalmatian` *"is a"* `Dog` (inherits from Dog)


### Association: "has a"

`Employee` *"has a"* `Vehicle` (if `Employee` is fired, `Vehicle` goes to
another `Employee` - it can exist independently.)

Association can be *one-* or *two-way*:

* One-way: Object `A` can access properties of `B` but not vice versa
* Two-way: Objects `A` and `B` can access each other's properties

There are two subtypes of association - **composition** and **aggregation**.


#### Composition: "creates a":

`A` creates an instance of `B`

##### Composition example:

```python
import random

class Die:
    """A 6-sided die"""

    def __init__(self, value=None):
        self.value = value

    def roll(self):
        self.value = random.choice(range(1, 7))


class Player:
    """A player who rolls a die each turn

    The `take_turn` method creates a new instance of `Die`, meaning the
    `Player` object is in total control of the lifetime of the `Die`
    object. This is a *composition* relationship.
    """

    def __init__(self, name):
        self.name = die

    def take_turn(self):
        die = Die()
        die.roll()
        print(die.value)

```


#### Aggregation: "uses a"

`A` uses an pre-existing instance of `B`. `A` and `B` exist independently
of each other.


##### Aggregation example:

```python
import random

class Die:
    """A 6-sided die"""

    def __init__(self, value=None):
        self.value = value

    def roll(self):
        self.value = random.choice(range(1, 7))


class Player:
    """A player who rolls a die each turn

    `__init__` takes an instance of `Die` as an argument, meaning that
    the `Die` object can exist independently of the instance of `Player`,
    and so the relationship is that of *aggregation*.
    """

    def __init__(self, name, die):
        self.name = name
        self.die = die

    def take_turn(self):
        self.die.roll()
        print(self.die.value)

```
