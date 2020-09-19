import random

words = ['astronaut', 'farmer', 'engineer', 'actor', 'mechanic', 'accountant']

def hangman(choices):
    # initialize varialbles
    word = choices[random.randint(0, len(words)-1)].lower()
    guess = [''] * len(word)
    board = '\n💈🀱 🀱 🀱💈\n💈\n💈\n💈\n💈\n💈\n💈🀱 🀱 🀱 🀱 🀱 🀱 🀱 🀱 💈'
    chances  = 7
    ready = ''

    # display game to user
    print(board)
    print(guess)
    ready = input('Welcome to hangman, are you ready to play? (y,n)\n')

    # if user wants to play
    if ready == 'y':
        # while hangman is alive
        while chances > 0:
            # show gameboard
            print(f'Here is your board:\n {board}')
            print(f'Here is your word:\n {guess}')
            # get guess from user
            current = input('Pick a letter\n').lower()
            # if wrong guess
            if current not in word:
                # -1 from chances left
                chances -= 1
                # depending on which chance, reset board with new image
                if chances == 6:
                    board = '\n💈🀱 🀱 🀱💈\n💈\n💈\n💈\n💈      \\\n💈\n💈🀱 🀱 🀱 🀱 🀱 🀱 🀱 🀱 💈'
                if chances == 5:
                    board = '\n💈🀱 🀱 🀱💈\n💈\n💈\n💈\n💈     /\\\n💈\n💈🀱 🀱 🀱 🀱 🀱 🀱 🀱 🀱 💈'
                if chances == 4:
                    board = '\n💈🀱 🀱 🀱💈\n💈\n💈\n💈     ()\n💈     /\\\n💈\n💈🀱 🀱 🀱 🀱 🀱 🀱 🀱 🀱 💈'
                if chances == 3:
                    board = '\n💈🀱 🀱 🀱💈\n💈\n💈\n💈    /()\n💈     /\\\n💈\n💈🀱 🀱 🀱 🀱 🀱 🀱 🀱 🀱 💈'
                if chances == 2:
                    board = '\n💈🀱 🀱 🀱💈\n💈\n💈\n💈    /()\\\n💈     /\\\n💈\n💈🀱 🀱 🀱 🀱 🀱 🀱 🀱 🀱 💈'
                if chances == 1:
                    board = '\n💈🀱 🀱 🀱💈\n💈\n💈     😳\n💈    /()\\\n💈     /\\\n💈\n💈🀱 🀱 🀱 🀱 🀱 🀱 🀱 🀱 💈'
                # lose condition
                if chances == 0:
                    board = '\n💈🀱 🀱 🀱💈\n💈     |\n💈     😵\n💈    /()\\\n💈     /\\\n💈\n💈🀱 🀱 🀱 🀱 🀱 🀱 🀱 🀱 💈'
                    # show board, ask if they want to play again
                    print(f'{board}\n')
                    play_again = print(f'Ummmmmmm, yeaaaaaaa. We were looking for {word}.\nTry again? (y,n)\n')
                    # if yes, run again
                    if play_again == 'y':
                        hangman(words)
                    # if not y, exit
                    else:
                        print('Thanks for playing!')
                        return
            # if right guess, 
            else:
                # insert correct guess in all places where correct
                for i in range(0, len(word)):
                    if current == word[i]:
                        guess[i] = current
                # change back to string to check against answer
                seperator = ''
                guess_string = seperator.join(guess)
                # win condition
                if guess_string == word:
                    # show board and tell user they won
                    print(f'{board}\n')
                    play_again = input(f'You saved the criminal!\nYou had {chances} chances remaining.\nPlay again? (y,n)\n')
                    chances = 0
                    if play_again == 'y':
                        hangman(words)
                    else:
                        print('Thanks for playing!')
                        return   
    # if user doesn't want to play    
    elif ready == 'n':
        print('Come back when you are ready to play!\n')
        return 
    # if user inputs invalid option
    else:
        print('Please select a valid option.\n')
        return hangman(words)

hangman(words)