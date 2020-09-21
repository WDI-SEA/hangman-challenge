import random
words_list = ['github', 'general assembly', 'rome bell', 'software engineering', 'instagram', 'python', 'coding']

def get_random_word():
    word = random.choice(words_list)
    return word

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to Hangman")
    print(hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ")

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already tried that letter.", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guess == True
                    
        elif len(guess) == len(word):
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else: 
                guessed = True
                word_completion = word

        print(hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you win!")
    else:
        print("You failed, try playing again")

def hangman(tries):
    stages = [
        "-o-|-<",
        "-o-|-",
        "-o-|",
        "-o-",
        "-o",
        "-",
        " "
    ]
    return stages[tries]

def main():
    word = get_random_word()
    play(word)

if __name__ == "__main__":
    main()