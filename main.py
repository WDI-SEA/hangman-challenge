# main.py
from random import shuffle

# |----------I
# |          |
# |          0
# |
# |
# |
# |
# |
# |_______________________
#

#  👱🏼‍♂️
# 🦾👕🤳🏼‍
#   🩳
#  🦴 🦿
#

#  i need to create a hangman game
# [X] Store a list (or tuple) of 5 to 10 words in your script.
# [X] Randomly choose a word from this list as the secret word.
# [X] Display the unrevealed word as underscores (with the same length.)
# [X] Prompt the user to enter a letter.
# [ ] If the letter is in the word, mark it as revealed and visually display that letter in the word.
# [ ] If the letter is incorrect, draw another part onto the stick person.

# list of words

# function hangman
# randomly pick word from list
# convert word to underscores for player
# get input from user with letter
# if letter is in word, fill in the blank
# else add a lil man hanging
# do it again



# def correct_word():
#  list of words
words = ["shrek", "my chemical romance", "george bush", "bada bing", "bada boom", "copacetic", "butt dial", "michael gary scott"]
#  shuffle those words
shuffle(words)
print(f"this is teh shuffled list of words - {words}")
#  pick the first random word
random_word = words[0]
print(f"this is the random_word - {random_word}")
print(f'this is the length of random_word - {len(random_word)}')
# split up the phrase if needed
individual_string = random_word.split()
print(f"this is random word after split - {individual_string}")
user_view = ""
# this will return underscore for letters and a space to the user
for i in random_word:
	if i == " ":
		user_view += " "
	else:
		user_view += "_"
print(f"this is user_view after loop - {user_view}")


# word_len = int(len(random_word))
# secret_word = "_" * word_len
# print(f"this is the secret - {secret_word}")
# for i in range(word_len):
# 	print(f" this is i in the range - {i}")

# # prompt asking for user guess
# guess = input("what letter would you like to guess ")
# print(guess)
# for i in random_word:
# 	# print(f"this is the i in random_word - {i}")
# 	if i == guess:
# 		print("correct!!")
# 	# else:
# 	# 	print("dying")
















