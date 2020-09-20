import random 
word = ['banana', 'tree', 'plate', 'mirror', 'chair']

# def shuffle(ls):
#     random.shuffle(ls)

#     return display_word(random_word)  

# print(shuffle(word))

def correct_letter(letter,length):
    
    length = len(letter)
    print(letter)
    
    # print('look',length)
    if length == 0 :
        print('Game over')
        return
    else:
        input_letter = input('insert letter')    
        if input_letter in letter:
            print('correct')
            # print(length)
            # letter.remove(input_letter)
            letter = [x for x in letter if x != input_letter]
            length = len([x for x in letter if x != input_letter])
            
            print (letter)
            print(length)
            
            return correct_letter(letter,length)
        else:
            print('try again')
            return correct_letter(letter,length)




def display_word(ls):
    random.shuffle(ls)
    # print(ls[0])
    letter = [char for char in ls[0]]
    # print(letter)
    print (len(letter)*'_ ')

    return correct_letter(letter,len(letter))

display_word(word)




# |-\
# |  0
# | /|\
# | /| \

