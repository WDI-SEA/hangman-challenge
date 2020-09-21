import random

def wordList():
    words = ["banana", "apple", "orange", "pineapple", "papaya"]
    return random.choice(words)

def playAgain():
    answer = input('WOuld you like to play again ? y/n ' ).lower()
    if answer == 'y':
        hangman()
    else:
        pass

def hangman():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = wordList()
    letters_guessed = []
    tries = 7
    guessed = False

    print('The word contains', len(word), 'letters.')
    print(len(word) * ' _ ')

    while guessed == False and tries > 0:
        print('You have ' + str(tries) + ' tries')
        guess = input('Please enter one letter or the full word.').lower()

        # when the user input a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('You have not entered a letter.')
            elif guess in letters_guessed:
                print('you have already guessed that letter before')
            elif guess not in word:
                print('Sorry, that is not a word')
                letters_guessed.append(guess)
                tries -= 1
            elif guess in word:
                print('Good job !')
                letters_guessed.append(guess)
            else:
                print('Error, please try again.')
        
        # when the user input the full word
        elif len(guess) == len(word):
            if guess == word:
                print('Good job! You have guessed the word !')
                guessed = True
            else:
                print('Sorry, wrong word.')
                tries -= 1

        # when the user input wrong length of word
        else:
            print('The length of your guess is not the same as the word you guess.')

        # for loop to show the input word or empty space
        status =''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += ' _ '
            print(status)

        # if the user gets correct guess
        if status == word:
            print('Good Job, you guessed the word!')
            guessed = True
        elif tries == 0:
            print('You have run out of tries and you have not guessed the word.')

    playAgain()

hangman()