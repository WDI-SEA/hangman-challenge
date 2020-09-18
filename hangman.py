from random import seed
from random import randint
# start with a list of words
# return a randomized word from that list as the value
words = ['dogs', 'couch', 'teapot', 'recursion', 'javascript']
seed()
secret_word = words[randint(0,(len(words)))]
print(secret_word)