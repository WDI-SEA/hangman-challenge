import random

word_list = ['Hello', 'World', 'Developer', 'Python', 'Macbook']


def hangman(lst1):
    word1 = random.choice(lst1)
    word = word1.upper()
    word_copy = list(word)
    print(word)
    result_spaces = '_' * len(word)
    res = ' '.join(list(result_spaces)) 
    print(res)
    letter_guess = []
    secret_word = []
    tries_left = 6

    while tries_left >= 1:
        guess = input('Enter a letter: ').upper()
        letter_guess.append(guess)
        print('Letters guessed so far',letter_guess)
        if guess in word_copy:
            print('Good job the letter '+guess+' is in the word')
            index = word_copy.index(guess)
            result_spaces = letter_print(index, word_copy, result_spaces)
            word_copy = replace_letter(index, word_copy)
            print(word_copy)
        else:
            tries_left -= 1

def letter_print(ind, word, result_spaces):
    result = list(result_spaces)
    print('SOMETHING',result)
    for i in range(len(word)):
        if i == ind:
            result[i] = word[i]
    result_spaces = ''.join(result)
    res = ' '.join(list(result_spaces)) 
    print(res)
    # print(result_spaces)
    return result_spaces 

def replace_letter(index, lst):
    for i in range(len(lst)):
        if i == index:
            lst[i] = '.'
    return lst 


hangman(word_list)


