import random

secret_words = ['word', 'banana', 'divorce', 'cat', 'dinosaur']
random_word = random.choice(secret_words)
output = list('_'*len(random_word))
hang_array = ['O\n\I/\n//', 'O\n\I/\n/', 'O\n\I/', 'O\nI/', 'O\nI', 'O']
def hang_man():
    print(random_word)
    if len(hang_array) > 0:
        for w in range(len(hang_array)):
            letter = str(input("Enter a Letter:\n"))
            if letter in random_word:
                for i, j in enumerate(random_word):
                    if j is letter:
                        output[i] = letter
                        new_output = ''.join(output)
                        print(new_output)
                        if new_output == random_word:
                            print("You've won!")
            else:
                print(letter + " is not in the word")
                print(hang_array.pop())
                if len(hang_array) < 1:
                    print("You have lost, the word was {}, please try again.".format(random_word))
                    hang_man()
hang_man()
