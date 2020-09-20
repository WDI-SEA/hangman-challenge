from random import seed
from random import randint

word_bank = ['booger', 'ostrich', 'dinosaur', 'tweaker', 'hamburger', 'orange', 'television', 'fungus', 'tarantula', 'bulging']

# seed random number each time the script is run based on system time
seed()
# DONE display secret word as underscores
# 

class Game:
  def __init__(self):
    # get a word from a random index of word_bank
    self.word = word_bank[randint(0, len(word_bank) - 1)]
    self.game_over = True
    self.hangman = '-o-|-<'
    self.letters = [] # display letters chosen by the player
    self.display = ['_'] * len(self.word)# generate a string/array the same len of self.word consisting only of underscores

  def __str__(self):
    # print current Game's word
    return f'''The secret word is {self.word} 
    its length is {len(self.word)}, 
    the game is displaying {self.display}, 
    its len is {len(self.display)}'''

  def take_turn(self):
    turn = input('enter a letter\n')
    print(f'HERES THE TURN {turn}')
    if turn in self.word:
      print('thats true')
    else:
      print('thats false')

class Word(Game):
  def __init__(self):
    # we pass in letters because the parent class
    # needs access to that information
    super().__init__()
    self.letters = []




new_game = print(Game())
Game().take_turn()