# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math

# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """

    tries = 0
    guess = int((high + low) / 2)
    bingo = False
    while not bingo:
        tries = tries + 1
        if guess == actual_number:
            print(
                "bingo！your guessed {} is the right anwer, it takes {} tries".format(
                    guess, tries
                )
            )
            bingo = True
        elif guess < actual_number:
            print("your guessed {} is low, keep going ".format(guess))
            temp = guess
            guess = int((high + guess) / 2)
            low = temp
            if guess + 1 == actual_number:
                guess = guess + 1
            elif guess - 1 == actual_number:
                guess = guess - 1
            print("low is {} , high is {} ".format(low, high))
        elif actual_number < guess:
            print("your guessed {} is high, keep going".format(guess))
            temp = guess
            guess = int((low + guess) / 2)
            high = temp
            if guess + 1 == actual_number:
                guess = guess + 1
            elif guess - 1 == actual_number:
                guess = guess - 1
            print("low is {} , high is {} ".format(low, high))
    print("u got it")
    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
