import random

words = ['apple', 'park', 'sleepy', 'hamburger', 'pizza', 'jellyfish']

start = input('Welcome to hangman! You have 6 attempts. To start, press enter')
word = random.choice(words).lower()


def game_init():
    attempts = 0
    # print(word)
    guesses = 6
    spaces = '- ' * len(word)
    guessed_letters = []
    reveal_word = ""

    print(spaces)

    while guesses > attempts:
        print("Letters guessed:" + str(guessed_letters))
        user_answer = input("Choose a letter: ")
        for letters in word:
            if user_answer in word:
                print(f'Letter {user_answer} was found!')
                guessed_letters.append(user_answer)
                reveal_word = reveal_word + user_answer
                print(reveal_word)
                # if reveal_word == word:
                #     print ('Congrats! You won!')
                # else:
                #     print('Keep trying!')
                break
            else:
                print(f'Letter {user_answer} was not found! Try again.')
                guessed_letters.append(user_answer)
                guesses -= 1
                print(f'You have {guesses} remaining')
                reveal_word = "_" + reveal_word
                break

    else:
        play_again = input('Would you like to play again? (y/n)')
        if play_again == 'y':
            game_init()
        else:
            print('Okay! Better luck next time!')

game_init()


