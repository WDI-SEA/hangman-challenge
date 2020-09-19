import random
word_list = ['Hello', 'Computer', 'Together', 'Dog', 'Later', 'Yesterday']

def hangman(lst1):
    word1 = random.choice(lst1)
    word = word1.upper()
    print(word)
    result_spaces = "_ " * len(word)
    print(result_spaces)
    letters_guess = []
    tries_left = 6

    while tries_left > 1:
        guess = input("Enter a letter: ").upper()
        if len(guess) > 1:
            print("Please enter only one letter")
        elif guess in letters_guess:
            print("sorry the letter "+guess+" has already been picked")
        elif guess not in word:
            print("Sorry "+guess+" is not in the word")
            tries_left -= 1
        else:
            letters_guess.append(guess)
            if guess in word:
                print("Good job the Letter: "+guess+" is in the word")
                tries_left -= 1



hangman(word_list)
