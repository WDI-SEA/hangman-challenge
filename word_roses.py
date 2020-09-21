# Initialize the game: Initialize all variables to default values.
import random

word_list = [
    'sanity',
    'squad',
    'django',
    'python',
    'dequeue',
    'sandwich',
    'cashews',
    'rubber',
    'duck'
]

# Display hangman or number of guesses remaining.
def show_rose(turns):
    stages = [  '''
                   ({@}) 
                    ~|
                     |{*>
                  <*}|
                     |~           
                ''',
                '''
                     @
                    ~|
                     |{*>
                  <*}|
                     |~
                ''',
                '''
                    ~|
                     |{*>
                  <*}|
                     |~  
                ''',
                '''
                     |{*>
                  <*}|
                     |~ 
                ''',
                '''
                  <*}|
                     |~ 
                ''',
                '''

                     | 
                '''
    ]
    return stages[turns]

# Randomly select a secret word.
def choose():
    secret_word = random.choice(word_list)
    return secret_word.upper()

def game_init(secret_word):
    # Display the word as blanks.
    complete = "@" * len(secret_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    turns = 5
    print('@ WORD ROSE @')
    print(show_rose(turns))
    print(complete)
    print('\n')
    while not guessed and turns >= 0:
        # Ask the user for a letter.
        guess = input('Guess a letter or word: ').upper()
        # Determine if letter is correct or incorrect.
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Already guessed ', guess)
            # If incorrect, add the letter to the guessed list, decrement remaining guesses, and/or draw another bit of the hangman.
            elif guess not in secret_word:
                print(guess, ' is not in the word.')
                turns -= 1
                guessed_letters.append(guess)
            else:
                # If correct, add the letter to the guessed list, redraw the secret word with the new letter(s) showing.
                print('Nice! ', guess, ' is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(complete)
                indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                complete = ''.join(word_as_list)
                if '@' not in complete:
                    guessed = True
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess in guessed_words:
                print('Already guessed ', guess)
            elif guess != secret_word:
                print(guess, ' is an incorrect guess.')
                turns -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                complete = secret_word          
        else:
            print('Invalid guess')
        print(show_rose(turns))
        print(complete)
        # Display the letters guessed so far.
        print('Already guessed: ', guessed_letters)
        print('\n')
    if guessed:
        print('Nice job! You guessed the word!')
    else:
        print('Out of guesses😓 The word was: ' + secret_word + '. Please accept this rose as consolation.')

def main():
    secret_word = choose()
    game_init(secret_word)
    while input('Play again? (Y/N)').upper() == 'Y':
        secret_word = choose()
        game_init(secret_word)

if __name__ == '__main__':
    main()

# Loop back up to step 6 and continue until the word is fully revealed or guesses are used up.