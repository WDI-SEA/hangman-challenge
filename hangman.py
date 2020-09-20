import random 
word = ['banana', 'tree', 'plate', 'mirror', 'chair']

# def shuffle(ls):
#     random.shuffle(ls)

#     return display_word(random_word)  

# print(shuffle(word))

def correct_letter(letter):
    input_letter = input('insert letter')
    print(letter)
    if len(letter) == 1:
        print('Game over')
        return
    if input_letter in letter:
        print('correct')
        letter.remove(input_letter)
        print (letter)
        return correct_letter(letter)
    else:
        print('try again')
        return correct_letter(letter)




def display_word(ls):
    random.shuffle(ls)
    # print(ls[0])
    letter = [char for char in ls[0]]
    # print(letter)
    print (len(letter)*'_ ')

    return correct_letter(letter)

display_word(word)

