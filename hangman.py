from random import choice

#main game logic
def hangman():
    # choice method selects a random word from list 
    list = choice(["underscores", "corgis", "ramen", "pseudocode", "variables", "reveal", "preferably", "explore", "action", "coffee", "print"])
    # print(list) ---test out random word generator

    # declare number of turns
    turns = 7

    # empty list where correct letters are added
    guessed = []

    # stores all the incorrect guesses
    wrong = []

    while turns > 0:
        out = ""
        # for loop 
        for letter in list:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == list:
            break
            # print("You guessed", list)

        print("Guess the word:", out)
        print(turns, "guesses left")

        # input finds out what the player typed
        guess = input()

        #find out if the letter is in the word
        #if you guess a letter that is already in the guessed list
        if guess in guessed or guess in wrong:
            print("Already guessed:", guess)
        elif guess in list:
            print("Correct! 😁")
            # if the guessed letter is in the random word, append it and display that letter
            guessed.append(guess)
        #incorrect letter guess
        #for incorrect guesses, subtract one turn
        else:
            if turns > 0:
                turns = turns - 1
                wrong.append(guess)
            if turns == 0:
                print("game over")

    if turns:
        print(f"You guessed the correct word: {list}!")
        playAgain()
    else:
        print(f"You didn't get this word: {list} 😔")
        playAgain()       
#hangman()


def playAgain():
    playAgain = input("Do you want to play again? (y/n)\n")
    if playAgain == "y":
        hangman()
    else:
        print("See ya l8ter when you're brave enough to play!")

# starts game
def startGame():
    play = input("Do you want to play hangman? (y/n)\n")
    # if yes, start the game
    if play == "y":
        hangman()
    # if no then bye
    else:
        print("See you later!")

startGame()
        



