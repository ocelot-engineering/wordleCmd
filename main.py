# This is a quick wordle clone in the command line.

import random
import sys
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Wordle:
    """The Wordle game in your command line!"""

    def __init__(self, lexicon, max_guesses):
        self.lexicon = lexicon
        self.max_guesses = max_guesses
        self.n_guesses = 0
        self.chosen_word = None
        self.sleep_speed = 0.8

    def choose_word(self):
        word_index = random.randint(0, len(self.lexicon)-1)
        chosen_word = self.lexicon[word_index]
        self.chosen_word = list(chosen_word.upper())
        return None

    def end_game(self, msg = "game over."):
        sys.exit("\n" + msg)

    def invalid_guess(self, guess):
        if len(guess) != 5:
            return True

    def print_guess_results(self, guess_list):

        for i in range(5):
            current_letter = guess_list[i]

            if current_letter == self.chosen_word[i]:
                print(f"{bcolors.OKGREEN}{current_letter}", end="")
            elif current_letter in self.chosen_word:
                print(f"{bcolors.WARNING}{current_letter}", end="")
            else:
                print(f"{bcolors.FAIL}{current_letter}", end="")

            time.sleep(self.sleep_speed)

    def guess(self, guess):
        # Check if guess is valid
        if self.invalid_guess(guess):
            print("Guess is invalid, please guess a 5 letter word.")
            return None

        # Convert guess to correct format
        guess_list = list(guess.upper())

        # Print results
        self.print_guess_results(guess_list)

        # Check if won
        if guess_list == self.chosen_word:
            self.end_game(f"{bcolors.BOLD}{bcolors.HEADER}" + "you won!")

        # Check if max guess limit is reached
        self.n_guesses += 1
        if self.n_guesses >= self.max_guesses:
            self.end_game()

    def ask_for_guess(self):
        guess_str = input(f"{bcolors.ENDC}\n")
        self.guess(guess_str) # exit condition in this function
        self.ask_for_guess() # recursive call, exit condition in guess()

    def run_game(self):
        self.choose_word()
        print("Guess the 5 letter word I am thinking of...")
        self.ask_for_guess()



lexicon = ["thing", "words", "smash", "slope", "bread"]

wordle_game = Wordle(lexicon, max_guesses=5)

wordle_game.run_game()
