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

#  list of words and random word generator and creates the blank guessing field
# def correct_word():
words = ["shrek", "my chemical romance", "george bush", "bada bing", "bada boom", "just", "hate", "ogres"]
shuffle(words)
print(f"this is teh shuffled list of words - {words}")
random_word = words[0]
print(f"this is the random_word - {random_word}")
print(f'this is the length of random_word - {len(random_word)}')
word_len = int(len(random_word))
secret_word = "_" * word_len
print(f"this is the secret - {secret_word}")
# for i in range(word_len):
# 	print(f" this is i in the range - {i}")

# prompt asking for user guess
guess = input("what letter would you like to guess ")
print(guess)
for i in random_word:
	# print(f"this is the i in random_word - {i}")
	if i == guess:
		print("correct!!")
	# else:
	# 	print("dying")
















