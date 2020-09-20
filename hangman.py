import random 
word = ['banana', 'tree', 'plate', 'mirror', 'chair']

# def shuffle(ls):
#     random.shuffle(ls)

#     return display_word(random_word)  

# print(shuffle(word))

def display_word(ls):
    random.shuffle(ls)
    # print(ls[0])
    letter = [char for char in ls[0]]
    # print(letter)
    print (len(letter)*'_ ')

    return letter

display_word(word)