# RockPaperScissors
A python based game of Rock Paper Scissors. The game has two players - a human player and a computer player. In a single round of the game, each player secretly chooses one of three moves — rock, paper, or scissors. Then, players reveal their moves at the same time. If both players picked the same move, there is no winner. Otherwise, rock beats scissors; paper beats rock; and scissors beat paper.


## Application Preview

https://github.com/user-attachments/assets/16d847a5-0800-4398-a285-336380a05a02


## Software, Firmware and Hardware

* Python 3
* Terminal


## Installation instructions

* Install Python3
* Download code file
* Open terminal and cd to the folder containing code file
* Run command
```python3 rps.py```
* Follow the instructions on the screen and play the game
* In order to change the computer player's playing strategy, the code file `rps.py` should to be edited in \__main__ function to RandomPlayer(), ReflectPlayer() or CyclePlayer()


## Folder Structure

* README.md - Read me file with project details and instructions
* rps.py - Python code file


## Highlights

The game has two players - a human player and a computer player. The coumputer can act like a:
* Random Player - One that chooses its move at random
* Reflection Player - One that remembers what move the human opponent played in the last round, and plays that same move in this round
* Cycle Player - One that cycles through the different moves by remembering what it played last
Score is tracked while the player plays and winner is declared in the end.


## Copyright

The code is developed by **Nimisha Viraj** as a part of [Udacity Software Developer Foundations for Stellantis](https://www.udacity.com/enrollment/nd000-ent-stellantis). 


## Acknowledgements

[Udacity](https://udacity.com) - Source of code challenge


## Limitation and Scope

The program can be fine tuned to pick computer player's playing strategy at random which is hard coded at present
