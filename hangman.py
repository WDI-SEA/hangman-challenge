from random import seed
from random import randint
# start with a list of words
# return a randomized word from that list as the value
shrug= ' ¯\_(ツ)_/¯ '

words = ['dogs', 'couch', 'teapot', 'recursion', 'javascript']
seed()
secret_word = words[randint(0,(len(words)))]
print('Welcome to Hangman! You have 6 guesses to find your word!')
global turns
turns = 6
foundWords = ''
display_word = ''
guess=''
def letter_compare():
    global display_word
    display_word = ''
    for i in secret_word:
        if i in foundWords:
           display_word += i
        else:
           display_word += ' _'
while turns > 0:
    letter_compare()
    print(display_word)
    guess = input('What\'s your guess? ').lower()
    displayMan = 'Shrugging man', shrug[0:(6-(turns))*2]
    if guess in secret_word:
        foundWords += guess
        letter_compare()
        if display_word == secret_word:
            print('You won!')
            turns = 0
        else:
            print('You got it dude')
            print(foundWords)            
    else:
        print('Nope, try again')
        turns -=1
    print(displayMan)
    print('This is the display word ', display_word)
    print('You have ', turns, ' more turns')
