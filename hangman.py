import random 

words = ['apple', 'park', 'sleepy', 'hamburger', 'pizza', 'jellyfish']

start = input('Welcome to hangman! You have 6 guesses. To start, press enter')

def hangman():
    attempts = 6
    word = random.choice(words).lower()
    # print(word)
    guesses = 0
    spaces = '-' * len(word)

    print()
    print(spaces)
    print()
    
    while guesses < attempts:
        user_answer = input("Choose a letter: ")
        for letters in word:
            if user_answer in word:
                print("Letter " + user_answer + " was found!")
                break
            else:
                print("Letter " + user_answer + " was not found! Try again.")
                guesses += 1
                break
    else: 
        print("Game over!")

hangman()