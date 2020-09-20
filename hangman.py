import random

secret_words=["uniform", "improve", "subrata", "extreme",  "hangman", "manager", "limited", "initail", "revenge", "counter"]
hanggedman = [ 
        " ____",
        "|    |",
        "|    O",
        "|   -|-",
        "|   / \\",
        "|",
        "-",
        ]

# Randomly select a secret word.
secret_w = secret_words[random.randint(0, 9)]

# Initialize the game: Initialize all variables to default values.
def hangman(secret_word, guess_word = ["_", "_", "_", "_", "_", "_", "_"], guess_left = 7, user_hanged_man = []):

    # if user guessed word matchs with the secret_w then return
    if (secret_w == "".join(guess_word)):
        print(f"\nYou revealed the secret word: {secret_w}")
        print("😎 You saved the Man. 🍺")
        return

    # if user ran out of guess count, then return
    if (guess_left == 0):
        print("👹 Deal with a Ghost Now! 👹")
        return 

    # Display number of guesses remaining.
    print(f"Remaining Guesses: {guess_left}")

    # Display the word as blanks.
    # Display the characters guessed so far.
    print(f'Word guessed so far {" ".join(guess_word)}')

    # Display hint of the word.
    print(f"Hint: {secret_w[0]}*****{secret_w[-1]}")

    # Ask the user for a character.
    character = input('Enter a character you are guessing:')

    guess_left -= 1
    guess = False

    # Ask for another input while there is more than 1 character
    while len(character) != 1:
        character = input('Enter a character you are guessing:')

    # Determine if character exists in secret_word.
    if character in secret_word:
        character_index = secret_word.find(character)  # find the character index
        guess_word[character_index] = character # put that character into guess word at that character index

        secret_word_list = list(secret_word) # list secret word
        secret_word_list.pop(character_index) # remove that character from that secret word list
        secret_word_list.insert(character_index, "-") # insert a dash into that list index
        secret_word = "".join(secret_word_list) # joins back from list to a string
        guess_left += 1
        guess = True

    if(len(user_hanged_man) < 8):
        print("🙏 Please Save me. Don\'t let me hang. 🙏")

    # If incorrect, add the character to the guessed list, decrement remaining guesses, and/or draw another bit of the hangman.
    if(guess == False): # if guess is false, grabs an element from hanggedman list insert into fromt of user_hangged man
        user_hanged_man.insert(0, hanggedman[guess_left])

    # print user hangged man.
    for i in range(len(user_hanged_man)):
        print(f"{user_hanged_man[i]}")

    hangman(secret_word, guess_word, guess_left, user_hanged_man)

# invoke hangman function with secret_w
hangman(secret_w)