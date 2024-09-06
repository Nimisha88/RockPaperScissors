#!/usr/bin/env python3
from pickle import FALSE
import random
import re
from shutil import move

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def update_score(self):
        self.score += 1

    def learn(self, my_move, their_move):
        pass


"""The RandomPlayer class is a Player that
chooses its move at random in this game"""


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


"""The HumanPlayer class is a Player that
asks the human user what move to make in this game"""


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        while True:
            move_input = input(("Please input one - "
                                "rock, paper, scissors: ")).lower()
            if (move_input in moves):
                return move_input
            else:
                print("Invalid input! Please try again.")


"""The ReflectPlayer class is a Player that remembers what move the opponent
played in last round, and plays the same move in the current round
in this game"""


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        random_move = random.choice(moves)
        self.learn(random_move, random_move)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        return self.their_move


"""The CyclePlayer class is a Player that remembers what move it played
in last round, and cycles through the different moves in this game"""


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.move_index = -1

    def update_move(self):
        self.move_index = (self.move_index+1) % 3

    def move(self):
        self.update_move()
        return moves[self.move_index]


"""The beats function can be used to determine which player won the round"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


"""The Game class is used to play rounds, display who wins the
individual rounds and final scores of the players"""


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1.update_score()
            print("***** Player 1 beats Player 2 *****")
        elif beats(move2, move1):
            self.p2.update_score()
            print("***** Player 2 beats Player 1 *****")
        else:
            print("***** That's a tie *****")
        print(("***** SCORE ~~~ "
               f"Player 1: {self.p1.score} ~~~ "
               f"Player 2: {self.p2.score} *****"))

    def play_game(self):
        print("~~~ GAME START! ~~~")
        round = 0
        playNextRound = True
        while playNextRound:
            round += 1
            print(("=================\n"
                   f"     Round {round}     \n"
                   "================="))
            self.play_round()
            playMore = input(("Play more rounds? "
                              "Enter y or yes to continue: ")).lower()
            playNextRound = True if playMore in ['y', 'yes'] else False
        print("~~~ GAME OVER! ~~~")
        if (self.p1.score == self.p2.score):
            winner = "TIE"
        elif (self.p1.score > self.p2.score):
            winner = "PLAYER 1"
        else:
            winner = "PLAYER 2"
        print(("=================\n"
               "   FINAL SCORE   \n"
               "=================\n"
               f"Rounds: {round}\n"
               f"Player 1: {self.p1.score}\n"
               f"Player 2: {self.p2.score}\n"
               "=================\n"
               f"Winner: {winner}\n"
               "================="))


if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()
