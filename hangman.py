import random 
word = ['banana', 'tree', 'plate', 'mirror', 'chair']

# def shuffle(ls):
#     random.shuffle(ls)

#     return display_word(random_word)  

# print(shuffle(word))


def wrong_answer(count):
    if count == 1:
        print( "|-\ \n|  0 \n|    \n|")
    elif count == 2:
        print( "|-\ \n|  0 \n|  | \n|")
    elif count == 3:
        print("|-\ \n|  0 \n| /| \n|")
    elif count == 4:
        print("|-\ \n|  0 \n| /|\ \n|")
    elif count == 5:
        print("|-\ \n|  0 \n| /|\ \n|  | ")
    elif count == 6:
        print("|-\ \n|  0 \n| /|\ \n| /| ")
    elif count == 7:
        print("|-\ \n|  0 \n| /|\ \n| /|\ \n Game Over, try new game")
        return display_word(word)
    


def correct_letter(letter,length,count=0):
    
    length = len(letter)
    # print(letter)
    # print(count)
    # print('look',length)
    if length == 0 :
        print('Game over')
        return
    else:
        input_letter = input('insert letter \n')    
        if input_letter in letter:
            print('correct')
            # print(length)
            # letter.remove(input_letter)
            letter = [x for x in letter if x != input_letter]
            length = len([x for x in letter if x != input_letter])
            
            # print (letter)
            # print(length)
            
            return correct_letter(letter,length,count)
        else:
            print('try again')
            count=count+1
            return (wrong_answer(count),correct_letter(letter,length,count))

def display_word(ls):
    random.shuffle(ls)
    # print(ls[0])
    letter = [char for char in ls[0]]
    # print(letter)
    print ("|-\ \n|    \n|    \n| \n", len(letter)*'_ ')

    return correct_letter(letter,len(letter))

display_word(word)













# |-\
# |  0
# | /|\
# | /| \

