from random import seed
from random import randint

word_bank = ['booger', 'ostrich', 'dinosaur', 'tweaker', 'hamburger', 'orange', 'television', 'fungus', 'tarantula', 'bulging']

# seed random number
seed()
print(randint(0, len(word_bank)))

class Game:
  def __init__(self):
    self.word = word_bank[randint(0, len(word_bank))]

  def __str__(self):
    return self.word

print(Game())