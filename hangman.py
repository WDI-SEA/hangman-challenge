# Pseudocode
# Initialize the game: Initialize all variables to default values.
# Display hangman or number of guesses remaining.
# Randomly select a secret word.
# Display the word as blanks.
# Display the letters guessed so far.
# Ask the user for a letter.
# Determine if letter is correct or incorrect.
# If incorrect, add the letter to the guessed list, decrement remaining guesses, and/or draw another bit of the hangman.
# If correct, add the letter to the guessed list, redraw the secret word with the new letter(s) showing.
# Loop back up to step 6 and continue until the word is fully revealed or guesses are used up.

import random
from secret_words import secret_words
import string

def get_words(secret_words):
    # randomly choose a secret_words from list
    word = random.choice(secret_words)
    # as long as the statement is true, it keeps iterating until it's not true
    while '-' in word or ' ' in word:
        word = random.choice(secret_words)
    return word

# Initialize the game: Initialize all variables to default values.
def hangman():
    # Randomly select a secret word.
    word = get_words(secret_words)
    word_letter = set(word)  # letter in word
    alphabet = set(string.ascii_lowercase) # from english dictionary
    used_letters = set() # Display the letters guessed so far.
    numbers = 6 # Display hangman or number of guesses remaining.

