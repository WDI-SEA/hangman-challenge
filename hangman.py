#took from python libary called radnom
import random
#from the file words.py I can import the words i have in my hang_words array
from words import hang_words #want to randomly choose words from this list so python has built in library called import random
#first define a function that gets words which will return a word for our game
def get_word():
    #Can either create a list of words or can import a list of words for the program to choose from
    # inside get word lets call random.choice on word list
    word = random.choice(hang_words)
    # lets return this word all upper case for the user to read
    return word.upper()

#interactive gameplay def a function so users can play the game
# several variables that will be updating each turn the user takes 

# first want to display the word during each turn
def play(word):
    # represent unguessed letters as underscores & show letters as correct guesses are made
    #to do this lets make a string called word_completion and will be the same length as the chosen word
    # will initially contain all underscores
    word_completion = "_" * len(word)

    # next creating a variable called guess thats initialized to false
    guessed = False

    # now create 2 lists one that will hold the letter the user guessed and set it to in empy array
    guessed_letters = []
    # and one that will hold the word the user guessed and also set to an empty array
    guessed_words = []
