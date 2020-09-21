import os
import random
from math import floor

############################################################################
#                             Initializations                              #
############################################################################
secret_word = "Much Wow"
wrong_choices = 0
word_dictionary = ["variable", "function", "object", "conditional", "loop", "scope", "iterator", "async", "await", "argument", "algorithm", "boolean", "integer", "class", "constant", "immutable", "mutable", "declaration"]
correct_letters = []

############################################################################
#           Screen Centering Functions (Responsive to the terminal)        #
############################################################################

def printCenter(string):
    print(string.center(os.get_terminal_size().columns))

def printBlankSpace(lines):
    print("\n"*(lines-1)) # Need to remove 1 because we already have the first line break by default
    
def printMultiCenter(multiString):
    print(padToCenter(multiString.splitlines(),os.get_terminal_size().columns))

def inputCenter(string):
    return input(string.center(os.get_terminal_size().columns)).center(os.get_terminal_size().columns)

def padToCenter(l:list,w:int)->str:
    padding =  ' '*(w//2) # a 1 char line would need at most w/2 spaces in front
    parts = [ padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

############################################################################
#                            Game Functions                                #
############################################################################

def init_game():
    clear_screen()
    printBlankSpace(4)
    printCenter("[=============================]".center(os.get_terminal_size().columns))
    printMultiCenter(
        '''
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                    |___/                       
        ''')
    printCenter("Programming Edition")
    printCenter("Created By Anthony Gregis")
    printCenter("[=============================]")
    printBlankSpace(3)
    inputCenter("Press Enter to continue")
    start_game()
    
def start_game():
    pick_word()
    clear_screen()
    generate_hangman()
    guess_words()

def pick_word():
    global secret_word
    secret_word = random.choice(word_dictionary)

def generate_hangman():
    blank_space = "                 "
    printBlankSpace(4)
    printMultiCenter(
    f'''
______________    
|             |   
|{'            ---  ' if wrong_choices >= 1 else blank_space}
|{'           |x x| ' if wrong_choices >= 1 else blank_space}
|{'            ---  ' if wrong_choices >= 1 else blank_space}
|{'             |   ' if wrong_choices >= 2 else blank_space}
|{'           L |' if wrong_choices >= 3 else blank_space}{' L ' if wrong_choices >= 4 else '   ' if wrong_choices >= 3 else ''}
|{'             |   ' if wrong_choices >= 5 else blank_space}
|{'            L ' if wrong_choices >= 5 else blank_space}{'L  ' if wrong_choices >= 6 else '   ' if wrong_choices >= 5 else ''}
|                 
|                 
---------------   
    ''')
    return

def handle_guess(letter):
    global correct_letters
    global wrong_choices
    if letter in secret_word:
        if letter in correct_letters: return
        for char in secret_word:
            if letter == char:
                correct_letters.append(letter)
    else:
        wrong_choices += 1

def generate_filler():
    filler = []
    for char in secret_word:
        if char in correct_letters:
            filler.append(char)
        else:
            filler.append('_')
    printBlankSpace(1)
    printCenter(" ".join(filler))
    printBlankSpace(1)

def handle_gameover():
    if len(correct_letters) == len(secret_word):
        printBlankSpace(5)
        printCenter("You Win")
        printCenter("Thanks for playing!")
    else:
        printBlankSpace(5)
        printCenter("You Lose")
        printCenter("Better luck next time")
    printBlankSpace(5)
    inputCenter("Press enter to close game")
    clear_screen()

def guess_words():
    while wrong_choices < 6:
        if len(correct_letters) == len(secret_word):
            handle_gameover()
            break
        generate_filler()
        print(f"Correct Letters: {''.join(correct_letters)}".center(os.get_terminal_size().columns))
        guess = inputCenter("Guess a word")
        handle_guess(guess)
        clear_screen()
        generate_hangman()
    else:
        handle_gameover()

init_game()