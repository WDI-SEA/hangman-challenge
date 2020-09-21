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
    guessed_list = set() # Display the letters guessed so far.
    numbers = 10 # Display hangman or number of guesses remaining.

    # Ask the user for a letter.
    # Loop back up to step 6 and continue until the word is fully revealed or guesses are used up.
    while len(word_letter) > 0 and numbers > 0:
        print('You have ', numbers, 'lives left! And you guessed these letters: ',''.join(guessed_list))

        # diplaying the secret words which guessing
        word_list = [letter if letter in guessed_list else '-' for letter in word]
        print('Secret Words: ', ''.join(word_list))

        input_letter = input('Guess a letter: ').lower() # lower case for input
        # Determine if letter is correct or incorrect.
    
        if input_letter in alphabet - guessed_list:
            guessed_list.add(input_letter)
            if input_letter in word_letter:
                #if is correct add the letter to the guessed list, redraw the secret word with the new letter(s) showing.
                word_letter.remove(input_letter)
                print('')
            else:
                # If incorrect, add the letter to the guessed list, decrement remaining guesses, and/or draw another bit of the hangman.
                numbers = numbers - 1  # takes away a life if wrong guess
                print('\nYour letter,',input_letter, 'is not in the list')
        elif input_letter in guessed_list:
            print('\n This letter already used! Guess a new letter!')
        else:
            print('n\That is not a valid letter! Guess a new letter!')

    # gets here when len(word_letters) == 0 OR when numbers == 0
    if numbers == 0:
        print('You died, sorry. The ANSWER is', word)
    else:
        print('YAY! GOTCHA! It is ', word, '!!')

# restart a game
def main():
    hangman()
    while input("Play Again? (Y/N) ").upper() == "Y":

        hangman()

if __name__ == '__main__':
   main()