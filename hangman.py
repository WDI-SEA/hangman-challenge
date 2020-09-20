import random 

words = ['apple', 'park', 'sleepy', 'hamburger', 'pizza', 'jellyfish']

start = input('Welcome to hangman! You have 6 guesses. To start, press enter')

def hangman():
    attempts = 6
    word = random.choice(words).lower()
    # print(word)
    guesses = 0
    spaces = '-' * len(word)

    print(spaces)
    
    while guesses < attempts:
        user_answer = input("Choose a letter: ")
        for letters in word:
            if user_answer in word:
                print("Letter " + user_answer + " was found!")
                print(spaces) # need the letter to print here
                break
            else:
                print("Letter " + user_answer + " was not found! Try again.")
                guesses += 1
                break
    else: 
        play_again = input('Would you like to play again? (y/n)')
        if play_again == 'y':
            hangman()
        else:
            print('Okay! Better luck next time!')

hangman()
