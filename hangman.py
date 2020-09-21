import random

words = ["potato", "salad", "yams", "coconut", "rhythm", "pineapple", "mangos", "oranges", "you're done", "get yeeted"]
secret_word = "yuh"

def game_start(arr):
    global secret_word
    random_index = random.randint(0, len(arr) - 1)
    secret_word = arr[random_index]
    solved_string = ""
    for i in range(len(secret_word)):
        solved_string += "-"
    hung_status(6)
    print(solved_string)
    hangman(solved_string, secret_word)


def hangman(solved_string, secret_word, lives=6):
    guess = input()
    if (len(guess) != 1):
        print("You have to guess using one letter!")
        hung_status(lives)
        print(solved_string)
        hangman(solved_string, secret_word, lives)
    elif (guess in secret_word):
        for i in range (len(secret_word)):
            if (secret_word[i] == guess):
                solved_string = solved_string[:i] + guess + solved_string[i + 1:]
            if (solved_string == secret_word):
                print("You win! \nThe word was {}!".format(secret_word))
                return
        hung_status(lives)
        print(solved_string)
        hangman(solved_string, secret_word, lives)
    else: 
        lives -= 1
        print(f"{guess} is not in the word!")
        hung_status(lives)
        print(solved_string)
        if (lives == 0):
            print("You lose! \nThe word was {}".format(secret_word))
            return
        hangman(solved_string, secret_word, lives)

def hung_status(lives):
    status = [".____.", "|    |", "|    ", "|   ", "|    ", "|"]
    if (lives == 5):
        status[2] = "|    O"
    elif(lives == 4):
        status[2] = "|    O"
        status[3] = "|    |"
    elif(lives == 3):
        status[2] = "|    O"
        status[3] = "|   -|"
    elif(lives == 2):
        status[2] = "|    O"
        status[3] = "|   -|-"
    elif(lives == 1):
        status[2] = "|    O"
        status[3] = "|   -|-"
        status[4] = "|    /"
    elif(lives == 0):
        status[2] = "|    O"
        status[3] = "|   -|-"
        status[4] = "|    /\\"
    for i in range(len(status)):
        print(status[i])

game_start(words)