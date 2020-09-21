from random import choice
# list of words
# choice method selects a random word from list 
list = choice(["underscores", "corgis", "ramen", "pseudocode", "variables", "reveal", "preferably"])
print(list)

out = ""
# for loop 
for letter in list:
    out = out + "_"
print("Guess a letter:", out)

# input find out what the player typed
guess = input()

#find out if the letter is in the word
if guess in list:
    print("Correct! 😁")
else:
    print("Try again")

# game functionality
# def hangman(guesses):
#     # declare number of turns player will have
#     turns = 7
#     # randomly chooses a word from list
#     random_word = random.choice(list).lower()
#     correct_guess = [""]


# def getRandomWord(words):
