import random
word_list = ['Hello', 'Computer', 'Together', 'Dog', 'Later', 'Yesterday']

def hangman(lst1):
    word1 = random.choice(lst1)
    word = word1.upper()
    print(word)
    result_spaces = "_ " * len(word)
    letters_guess = []
    good_guess = []
    tries_left = 6

    def try_win(word, good_guess):
        if len(word) == len(good_guess):
            print("congratulations you win! The word was: "+word)
            pa = input("Want to play again? (Y/N)")
            playagain = pa.upper()
            if playagain == 'Y':
                return hangman(word_list)
            else:
                exit()
        else:
            return False


    while tries_left > 0:
        print(result_spaces)
        guess = input("Enter a letter: ").upper()
        if len(guess) > 1:
            if guess == word:
                print("congratulations you win! The word was: "+word)
                pa = input("Want to play again? (Y/N)")
                playagain = pa.upper()
                if playagain == 'Y':
                    return hangman(word_list)
                else:
                    exit()
            else:
                print("Sorry "+guess+" is not in the word")
                tries_left -= 1
                print("You have: "+str(tries_left)+" tries left!")
        elif guess in letters_guess:
            print("sorry the letter "+guess+" has already been picked")
        elif guess not in word:
            print("Sorry "+guess+" is not in the word")
            tries_left -= 1
            print("You have: "+str(tries_left)+" tries left!")
            letters_guess.append(guess)
        else:
            letters_guess.append(guess)
            word_guess_list = list(result_spaces)
            answer_list = list(word)
            for i in range(len(answer_list)):
                if answer_list[i] == guess:
                    position = i * 2
                    word_guess_list.insert(position, answer_list[i])
                    good_guess.append(guess)
                    word_guess_list.pop(position+1)
                    result_spaces = "".join(word_guess_list)
            try_win(word, good_guess)
            print("Good job the Letter: "+guess+" is in the word")
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
# animation no idea how to make it on a console (plus is boring) might try pygame
# not so happy with the word list might try to get a word list online
# last try and correct word are mix, must fix
