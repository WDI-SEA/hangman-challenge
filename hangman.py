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

