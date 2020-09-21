from random import choice
# list of words
# choice method selects a random word from list 
list = choice(["underscores", "corgis", "ramen", "pseudocode", "variables", "reveal", "preferably"])
# print(list) ---test out random word generator

# declare number of turns
turns = 7

# empty list where correct letters are added
guessed = []

# stores all the incorrect guesses
wrong = []

#loops that asks for letters
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
        break

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
        print("Try again")
        turns = turns - 1
        wrong.append(guess)
    
    print()

if turns:
    print("You guessed the correct word:", list, "!")
else:
    print("You didn't get this word:", list, "😔")


