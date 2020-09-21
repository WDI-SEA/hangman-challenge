import random
import time

words = ('apple', 'banana', 'orange', 'mississippi', 'washington')
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("")
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
random_word = random.choice(words)
ls =[]


def display_word():
    display = ""
    for i in random_word:
        letter = i
        if letter in ls:
            display += letter
        else:
            display += '_'
    print(display)

display_word()


def guess_letter():
    turns = 6
    while turns > 0:
        letter = input('Guess a letter: ')
        if letter not in random_word:
            # letter = input('Guess a letter: ')
            turns -= 1
            ls.append(letter)
            print(ls)
            display_word()
            print('Wrong, sorry try again')
            print('You have', + turns, 'more guesses')
        elif letter in random_word:
            # letter = input('Guess a letter: ')
            turns -= 1
            ls.append(letter)
            print(ls)
            display_word()
            print('You got it right let\'s try again', + turns )
        if letter == random_word:
            print('You won!')
            
        
        # else:
        #     print('Try again')
        #     break
            
        # display_word()
        print(ls)
guess_letter()







