# Dice Game


This is an exercise from the Udemy course
[*"Python OOP - Object Oriented Programming for
Beginners"*](https://www.udemy.com/course/python-object-oriented-programming-oop/learn/lecture/32919418#content).

The goal of the exercise is to understand the concepts of [*inheritance*
and *association*](inheritance_and_association.md), as well as how to incrementally design a solution to
a problem using OOP and TDD.

The code is my own, the instructor's code can be found [here](instructor_solution.md).


## Problem Description

Analyse the requirements below - Nouns imply objects and properties, and
verbs imply methods. Start thinking about how to design your application.


## General Requirements

- [x] The game should have two players: a human player and a computer
      player. Both should have the same functionality.
- [x] Both players will start with a counter of 5.
- [x] Each player will have a particular die during the entire game.
- [x] Both players will roll their corresponding die (once per round).
- [x] The values of the dice will be compared to determine who wins the
      round. The player with the highest value wins the round.
- [x] If the two values are equal, then there is a tie and there is no
      winner for that round. The counters are not modified.
- [x] The counter of the player who wins a round will be decremented by 1.
- [x] The counter of the player who loses a round will be incremented by 1.
- [x] The counter will determine who wins the game. The player whose
      counter reaches the value 0 first wins the game.


## Specific Requirements

* **Interactivity**
    - [x] Before the human player rolls the die, he/she should be prompted
          to press any key to start the round.

* **Rolling the dice**
    - [x] When a player rolls the dice, the result should be a random
          integer between 1 and 6 (inclusive).

* **Messages**
    * The game should show a descriptive message:
        - [x] When the game starts.
        - [x] When a new round starts.
        - [x] When the game ends. This message should mention who won the game.
    * The game should display messages to:
        - [x] Show the value of each die after the players roll the dice.
        - [x] Mention the winner of the round or if there was a tie.
        - [x] Show both counters when a round ends.


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
    - [x] A counter. The initial value should be 5.
    - [x] Make `die` a protected attribute
    - [x] Make `counter` a protected attribute

* Each player should be able to:
    - [x] Increment the value of the counter by 1.
    - [x] Decrement the value of the counter by 1.
    - [x] Roll the die.


### DiceGame

* This class will represent a dice game.

* Each instance of the game should have the following attributes:
    - [x] A human player instance.
    - [x] A computer player instance: This will create a relationship
          between these classes. A DiceGame "has a" human player and a
          computer player.

* Each instance of the game should be able to:
    - [x] Start the game (play). This method will start the game
          logic. It should:
        - [x] Show a welcome message
        - [x] Create the endless loop that will continue the game until
              a counter has reached the value 0.
    - [x] Start a round (play round): This method should handle the main
          round logic. It should:
        - [x] Welcome the player to the round
        - [x] Roll the dice
        - [x] Determine the winner and loser of the round, or if the
              round is a tie
        - [x] Update the counters accordingly
        - [x] Show the values of the counters.
        - [x] Declare the results of the round.
    - [x] Determine when the game is over and stop the game.
        - [x] The game should end when the counter of either one of
              the players has reached the value 0.
        - [x] A descriptive message should be printed before the game ends.
        - [x] The final message should declare the winner of the game.
