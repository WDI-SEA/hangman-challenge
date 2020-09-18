from random import seed
from random import randint

word_bank = ['booger', 'ostrich', 'dinosaur', 'tweaker', 'hamburger', 'orange', 'television', 'fungus', 'tarantula', 'bulging']

# seed random number
seed()
print(randint(0, len(word_bank)))

class Game:
  def __init__(self):
    # get a word from a random index of word_bank
    self.word = word_bank[randint(0, len(word_bank) - 1)]
    self.game_over = True
    self.hangman = '''
    ___
    |  o
    | -|-
    |  /\\
    |
    ______   
    '''

  def __str__(self):
    # print current Game's word
    return self.hangman

class Word(Game):
  def __init__(self):
    # we pass in letters because the parent class
    # needs access to that information
    super().__init__()
    self.letters = []

print(Game())