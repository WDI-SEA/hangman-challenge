import random
word_list = ['Hello', 'Computer', 'Together', 'Dog', 'Later', 'Yesterday']

def hangman(lst1):
    word1 = random.choice(lst1)
    word = word1.upper()
    print(word)
    result_spaces = "_ " * len(word)
    wordlist = list(result_spaces)
    print(wordlist)
    # print(result_spaces)
    letters_guess = []
    tries_left = 6

    while tries_left > 0:
        print(result_spaces)
        guess = input("Enter a letter: ").upper()
        if len(guess) > 1:
            print("Please enter only one letter")
        elif guess in letters_guess:
            print("sorry the letter "+guess+" has already been picked")
        elif guess not in word:
            print("Sorry "+guess+" is not in the word")
            tries_left -= 1
            print("You have: "+str(tries_left)+" tries left!")
        else:
            letters_guess.append(guess)
            if guess in word:
                print("Good job the Letter: "+guess+" is in the word")
                tries_left -= 1
    if tries_left == 0:
        print("Better luck next time, the word was: ", word)
        pa = input("Want to play again? (Y/N)")
        playagain = pa.upper()
        if playagain == 'Y':
            return hangman(word_list)
        else:
            exit()


hangman(word_list)

# todo:
# find a way to find the index of the word  add them on result result_spaces
# will probably use a list() and "".join
# remember that I use "_ " with a space so it will have to be the index * 2
# take way the print(listword)
