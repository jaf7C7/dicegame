# Dice Game


This is an exercise from the Udemy course
[*"Python OOP - Object Oriented Programming for
Beginners"*](https://www.udemy.com/course/python-object-oriented-programming-oop/learn/lecture/32919418#content).

The goal of the exercise is to understand the concepts of *inheritance*
and *asociation*, as well as how to design a solution to a problem
using OOP.


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


## Problem Description

Analyse the requirements below - Nouns imply objects and properties, and
verbs imply methods. Start thinking about how to design your application.


## General Requirements

- [ ] The game should have two players: a human player and a computer
      player. Both should have the same functionality.
- [ ] Both players will start with a counter of 10.
- [ ] Each player will have a particular die during the entire game.
- [ ] Both players will roll their corresponding die (once per round).
- [ ] The values of the dice will be compared to determine who wins the
      round. The player with the highest value wins the round.
- [ ] If the two values are equal, then there is a tie and there is no
      winner for that round. The counters are not modified.
- [ ] The counter of the player who wins a round will be decremented by 1.
- [ ] The counter of the player who loses a round will be incremented by 1.
- [ ] The counter will determine who wins the game. The player whose
      counter reaches the value 0 first wins the game.


## Specific Requirements

* **Interactivity**
    - [ ] Before the human player rolls the die, he/she should be prompted
          to press any key to start the round.

* **Rolling the dice**
    - [ ] When a player rolls the dice, the result should be a random
          integer between 1 and 6 (inclusive).

* **Messages**
    * The game should show a descriptive message:
        - [ ] When the game starts.
        - [ ] When a new round starts.
        - [ ] When the game ends. This message should mention who won the game.
    * The game should display messages to:
        - [ ] Show the value of each die after the players roll the dice.
        - [ ] Mention the winner of the round or if there was a tie.
        - [ ] Show both counters when a round ends.


### Die

* Each die should have:
    - [x] A value.
        - [x] This value should be either None (if the die has not been
              rolled yet) or a random integer between 1 and 6 (inclusive).
        - [x] This attribute should not be changed outside the class. The
              change should be handled internally.

* Each die should be able to:
    - [x] Roll: Generate a random integer between 1 and 6 (inclusive)
          and assign it to the value attribute.


### Player

* Each player should have the following attributes:
    - [x] A Die instance.
    - [x] A Boolean value (True/False) to indicate if the player is a
          human or the computer.
    - [x] A counter. The initial value should be 10.
    - [x] Make `die` a protected attribute
    - [x] Make `counter` a protected attribute

* Each player should be able to:
    - [x] Increment the value of the counter by 1.
    - [x] Decrement the value of the counter by 1.
    - [x] Roll the die.


### DiceGame

* This class will represent a dice game.

* Each instance of the game should have the following attributes:
    - [ ] A human player instance.
    - [ ] A computer player instance: This will create a relationship
          between these classes. A DiceGame "has a" human player and a
          computer player.

* Each instance of the game should be able to:
    - [ ] Start the game (play). This method will start the game
          logic. It should:
        - [x] Show a welcome message
        - [ ] Create the endless loop that will continue the game until
              a counter has reached the value 0.
    - [ ] Start a round (play round): This method should handle the main
          round logic. It should:
        - [x] Welcome the player to the round
        - [x] Roll the dice
        - [ ] Determine the winner and loser of the round
        - [ ] Update the counters accordingly
        - [ ] Show the values of the counters.
    - [ ] Determine when the game is over and stop the game.
        - [ ] The game should end when the counter of either one of
              the players has reached the value 0.
        - [ ] A descriptive message should be printed before the game ends.
