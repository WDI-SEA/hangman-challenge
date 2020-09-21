# main.py
from random import shuffle
import re

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
# #  list of words
# words = ["shrekie", "farting solo", "george bush", "bada ping", "bada shroom", "copacetique", "butt dial",
#          "michael gary scott"]
# #  shuffle those words
# shuffle(words)
# #  pick the first random word
# random_word = words[0]
# print(f"this is the random_word - {random_word}")
# split up the phrase if needed
# individual_string = random_word.split()
user_view = ""


# this will return underscore for letters and a space to the user
# for i in random_word:
# 	if i == " ":
# 		user_view += " "
# 	else:
# 		user_view += "_"
#
# # # prompt asking for user guess
# guess = input("you would like to guess the letter ")
#
#
# #  replacer function, takes old string and replaces with new string at specified index
# def replacer(old_string, new_string, index):
# 	if index < 0:  # add it to the beginning
# 		return new_string + old_string
# 	if index > len(old_string):  # add it to the end
# 		return old_string + new_string
# 	# insert the new string between "slices" of the original
# 	return old_string[:index] + new_string + old_string[index + 1:]
#
#
# # def swap_letter():
# #
# #
# count = 0
#
# for i in random_word:
# 	if i == guess:
# 		count += 1
# 		print(f"i'm printing the count - {count}")
# 		# print("correct")
# 		letter_index = int(random_word.find(i))
# 		# print(f"this is the correct letters index in the string - {letter_index}")
# 		next_index = random_word.index(i, letter_index + 1, -1)
# 		# print(f"next index - {next_index}")
# 		guess_letter = re.findall(i, random_word)
# 		times_repeated = len(guess_letter)
# 		print(f"{guess} is repeated {times_repeated} times")
# 		updated_view = replacer(user_view, guess, letter_index)
# 		print(f"this is updated_view after replace - {updated_view}")
# 		if times_repeated == 2:
# 			second_updated_view = replacer(updated_view, guess, next_index)
# 			print(f"this is updated_view after replace in nexted if - {second_updated_view}")
#
# 		if count == times_repeated:
# 			print("done")


def pick_random_word():
	"""We return a random work from the array of potential words"""
	words = ["shrekie", "farting solo", "george bush", "bada ping", "bada shroom", "copacetique", "butt dial",
	         "michael gary scott"]
	#  shuffle those words
	shuffle(words)
	#  pick the first random word
	return words[0]


def replacer(guess, letter_lookup, reflected_guess):
	replaced = False
	for k, v in letter_lookup.items():
		if guess == letter_lookup[k]:
			replaced = True
			reflected_guess[k] = guess
	
	return replaced


def generate_underscore_view(word):
	letter_lookup = {k: v for k, v in enumerate(word)}
	reflected_guess = {k: '_' if k != ' ' else ' ' for k, _ in letter_lookup.items()}
	return (letter_lookup, reflected_guess)


def game_is_over(letter_lookup, reflected_guess, min_guesses, guess_left):
	if min_guesses <= guesses_left:
		return True
	
	for k, v in letter_lookup.items():
		if reflected_guess[k] != letter_lookup[k]:
			return False
	
	return True


def print_win_or_lose_message(letter_lookup, reflected_guess, max_guess, guess_left):
	if (max_guess <= guesses_left):
		return "You Lost Loser"
	
	for k, v in letter_lookup.items():
		if reflected_guess[k] != letter_lookup[k]:
			pass
	
	return "You Win"


word_to_guess = pick_random_word()
letter_lookup, reflected_guess = generate_underscore_view(word_to_guess)
guesses_left = 0

def game(word_to_guess, letter_lookup, reflected_guess, guess_left):
	print(f"word: {''.join(letter_lookup.values())}")
	print(f"word: {''.join(reflected_guess.values())}")
	guess = input("you would like to guess the letter ")
	did_replace = replacer(guess, letter_lookup, reflected_guess)
	
	if did_replace:
		guess_left -= 1
	
	if not game_is_over(letter_lookup, reflected_guess, 1, guess_left):
		return game(word_to_guess, letter_lookup, reflected_guess, guess_left)
	else:
		message = print_win_or_lose_message(letter_lookup, reflected_guess, 10, guess_left)
		print(message)

game(word_to_guess, letter_lookup, reflected_guess, 10)