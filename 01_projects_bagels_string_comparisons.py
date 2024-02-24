"""Bagels, by Al Sweigart al@inventwithpython.com		
2	A deductive logic game where you must guess a number based on clues.		
3	This code is available at https://nostarch.com/big-book-small-python-programming		
4	A version of this game is featured in the book, "Invent Your Own		
5	Computer Games with Python" https://nostarch.com/inventwithpython		
6	Tags: short, game, puzzle"""		

import random

NUM_DIGITS = 3 # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10 # (!) Trey setting this to 1 or 100.


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess waht it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagel       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))                           # gleicher und neuere Methode mit F-String: print(f"I am thinking of a modern way like {NUM_DIGITS}-digit number.")

    while True:     #  Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(" You have {} guesses to get it.".format(MAX_GUESSES))        # gleicher und neuere Methode mit F-String: print(f"You have {MAX_GUESSES} guesses to get it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))                     # gleicher und neuere Methode mit F-String: print(f"Guess #{numGuesses}: ")
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break   # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretNum))

        # Ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith("y"):
            break
    print("Thanks for playing!")