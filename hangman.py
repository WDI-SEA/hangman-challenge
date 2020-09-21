import random 
words = ['banana', 'tree', 'plate', 'mirror', 'chair']

# def shuffle(ls):
#     random.shuffle(ls)

#     return display_word(random_word)  

# print(shuffle(word))


def wrong_answer(count):
    if count == 1:
        print( "|-\ \n|  0 \n|    \n| \n try again!")
    elif count == 2:
        print( "|-\ \n|  0 \n|  | \n| \n try again!")
    elif count == 3:
        print("|-\ \n|  0 \n| /| \n| \n try again!")
    elif count == 4:
        print("|-\ \n|  0 \n| /|\ \n| \n try again!")
    elif count == 5:
        print("|-\ \n|  0 \n| /|\ \n|  | \n try again!")
    elif count == 6:
        print("|-\ \n|  0 \n| /|\ \n| /| \n try again!")
    elif count == 7:
        print("|-\ \n|  0 \n| /|\ \n| /|\ \n Game Over, try new game")
        return display_word(words)



def letter_check(word,length,blank,count=0):
    
    length = len(word)


    
    print(word)
    # print(count)
    # print('look',length)
    if length == 0 :
        print('Great!!')
        return
    else:
        input_letter = input('insert letter \n')
        if input_letter in word:
            for i in range (length):
                if word[i] == input_letter:
                    # blank = blank[:i] + input_letter + blank[i + 1:]   
                    # blank[word.index(input_letter)]=input_letter
                    blank += input_letter

                    print(blank)

                    word = [x for x in word if x != input_letter]
                    length = len([x for x in word if x != input_letter])

                    return (blank, letter_check(word,length,blank,count))
        
        else:
            print('try again')
            count=count+1
            return (wrong_answer(count),letter_check(word,length,blank,count))

def display_word(ls):
    blank = ''
    random.shuffle(ls)
    word = [char for char in ls[0]]
    blank = len(word)*'_ '
    print ("|-\ \n|    \n|    \n| \n", blank)

    return letter_check(word,len(word),blank)

display_word(words)











