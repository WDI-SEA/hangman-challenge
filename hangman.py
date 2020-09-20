import random 

words = ['apple', 'park', 'sleepy', 'hamburger', 'pizza', 'jellyfish']

# define hangman function
def hangman():
    attempts = 6
    word = random.choice(words).lower()
    # print(word)
    guess = [''] 
    correct_guess = ['']
    spaces = '-' * len(word)




#call function
hangman()