# print("Hello World")
from random import random
from math import floor
# Initialize game
secret_word = ""
letters_left = 0
hangman_guesses_left = 6
letters_guessed = []
errors = 0
underscored_secret_word = ""
secret_words = ["wicked", "newsies", "rent", "beetlejuice",
                "once", "hamilton", "cabaret", "tangled", "frozen", "chicago"]
# visual variables
hangman1 = '''
______
|    |
|    O
|
|
|__________
'''
hangman2 = '''
______
|    |
|    O
|    |
|
|__________
'''
hangman3 = '''
______
|    |
|    O
|   /|
|
|__________
'''
hangman4 = '''
______
|    |
|    O
|   /|\\
|
|__________
'''
hangman5 = '''
______
|    |
|    O
|   /|\\
|   /
|__________
'''
hangman6 = '''
______
|    |
|    O
|   /|\\
|   / \\
|__________
'''
hangman_table = [
    f'\n{hangman6}\n',
    f'\n{hangman5}\n',
    f'\n{hangman4}\n',
    f'\n{hangman3}\n',
    f'\n{hangman2}\n',
    f'\n{hangman1}\n'
]
# -----------------------------PLANNING------------------------------
# global variables up above
# functions
# game_init
# win, los
# add_to_guesses
# success
# print_hangman
# failure
# continue_game
# game loop


def game_init():
    global secret_word
    global letters_left
    global hangman_guesses_left
    global letters_guessed
    global errors
    global underscored_secret_word
    random_index = floor(random() * 6)
    secret_word = secret_words[random_index]
    letters_left = len(secret_word)
    hangman_guesses_left = 6
    letters_guessed = []
    errors = 0

    # print(secret_word)

    underscored_secret_word = " "

    i = 0
    while i < len(secret_word):
        underscored_secret_word = underscored_secret_word + "_ "
        i += 1


def lose():
    print("Hangman :(")
    print(f"The word was {secret_word}")


def add_to_guesses(guess):
    letters_guessed.append(guess)


def success(guess):
    global underscored_secret_word
    global win
    print("correct")
    add_to_guesses(guess)
    index = 0
    for letter in secret_word:
        if letter == guess:
            if index == 0:
                underscored_secret_word = guess + underscored_secret_word[1:]
            elif index < (len(secret_word) - 1):
                underscored_secret_word = underscored_secret_word[0:(
                    (index * 2))] + guess + " " + underscored_secret_word[(index * 2 + 2):]
            else:
                underscored_secret_word = underscored_secret_word[:-2] + guess
        index += 1

    for letter in underscored_secret_word:
        if letter == "_":
            continue_game()
            return
    win()


def print_hangman(incorrect_guesses_left):
    print(hangman_table[incorrect_guesses_left])


def failure(guess):
    global hangman_guesses_left
    add_to_guesses(guess)
    hangman_guesses_left -= 1
    print_hangman(hangman_guesses_left)
    continue_game()


def already_guessed():
    print("you already guessed that")
    continue_game()


def continue_game():
    global errors
    print(f"You have {hangman_guesses_left} guesses left")
    print(f"you have guessed {letters_guessed}")
    print(f" the word you need : {underscored_secret_word}")

    if hangman_guesses_left > 0:
        guess = input("guess a letter:\n").lower()
        if guess == secret_word:
            win()
            return
        if len(guess) > 1 and errors < 1:
            print("You biffed it. try again")
            errors += 1
            continue_game()
            return
        try:
            int(guess)
            if errors < 1:
                print("it looks like you entered a number. Dont do that")
                errors += 1
                continue_game()
                return
        except ValueError:
            pass
    if guess in letters_guessed:
        already_guessed()
        return
    for letter in secret_word:
        if letter == guess:
            success(guess)
            return
        failure(guess)
        return
    else:
        lose()


looping = True
game_init()
continue_game()
while looping:
    should_continue = input(
        "would you like to continue playing? yes or no\n").lower()
    if should_continue == "yes" or should_continue == "y":
        game_init()
        continue_game()
    elif should_continue == "no" or should_continue == "n":
        print("thanks for playing")
        looping = False
    else:
        print("im not sure what if thats a yes or no")
