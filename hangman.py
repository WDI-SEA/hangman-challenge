from random import random

#Store a list (or tuple) of 5 to 10 words in your script.
word_list = ["wicked", "newsies", "rent", "beetlejuice",
 "once", "hamilton", "cabaret", "tangled", "frozen", "chicago"]


def pick_word():
     word = random.choice(word_list)
     return word.upper()

def display_tree(attempts):
    states =[''' 
    _____
    |    |
    |    
    |   
    |    
    |
    -
    ''',
    ''' 
    _____
    |    |
    |    ^
    |   
    |    
    |
    -
    ''',
    ''' 
    _____
    |    |
    |    ^
    |   ^ 
    |
    |
    -
    ''',
    ''' 
    _____
    |    |
    |    ^
    |   ^ ^
    |    
    |
    -
    ''',
    ''' 
     _____
    |    |
    |    ^
    |   ^ ^
    |  ^  
    |
    -
    ''',
    ''' 
    _____
    |    |
    |    ^
    |   ^ ^
    |  ^ ^ 
    |
    -
    ''',
    ''' 
     _____
    |    |
    |    ^
    |   ^ ^
    |  ^ ^ ^  
    |
    -
    ''',]
    return states[attempts]

def round(word):
    finished_word = "_" * len(word)
    guessed_correct = False
    guessed_letters = []
    guessed_words = []
    attempts = 7 
    print("Guess the Musical, or build a tree. It's a win win here")
    print(display_tree(attempts))
    print(finished_word)
    print("\n")
    while not guessed_correct and attempts >0:
        guess = input("Pick a letter from a-z, or guess the word!").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Letter already guessed! Pick another letter. ", (guess))
            elif guess not in word:
                print(guess, "is not in this musical, try again.")
                attempts -=1
                guessed_letters.append(guess)
            else:
                print("Great job!", guess, "is in this musical!")
                guessed_letters.append(guess)
                word_to_list = list(finished_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_to_list[index] = guess
                finished_word = "".join(word_to_list)
                if "_" not in finished_word:
                    guessed_correct = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Silly goose, you've already guessed that!")
            elif guess != word:
                print(guess, "is not part of this musical.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed_correct = True
                finished_word = word


        else:
            print("Sorry, this guess is invalid")
        print(display_tree(attempts))
        print(finished_word)
        print("\n")
    if guessed_correct:
        print("Congrats! You named the musical!")
    else:
        print("Sorry, you didn't guess the musical within the attempts. The word was" + word+ "But check out that tree you built!")

def play():
    word = pick_word()
    round(word)
    while input("Would you like to play another round? (Y/N)").upper() == "Y":
        word = pick_word()
        round(word)


play()

