from random import choice
# list of words
# choice method selects a random word from list 
list = choice(["underscores", "corgis", "ramen", "pseudocode", "variables", "reveal", "preferably"])
# print(list) ---test out random word generator

# empty list where correct letters are added
guessed = []

# stores all the incorrect guesses
wrong = []

#loops that asks for letters
while True:
    out = ""
    # for loop 
    for letter in list:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == list:
        print("You guessed", list)
        break


    print("Guess the word:", out)

    # input finds out what the player typed
    guess = input()

    #find out if the letter is in the word
    #if you guess a letter that is already in the guessed list
    if guess in guessed:
        print("Already guessed:", guess)
    elif guess in list:
        print("Correct! 😁")
        # if the guessed letter is in the random word, append it and display that letter
        guessed.append(guess)
    #incorrect letter guess
    else:
        print("Try again")
        wrong.append(guess)
    
    print()

# If the letter is incorrect, draw another part onto the stick person.

