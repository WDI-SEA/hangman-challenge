from random import seed, randint

word_bank = ['booger', 'ostrich', 'dinosaur', 'tweaker', 'hamburger', 'orange', 'television', 'fungus', 'tarantula', 'bulging']

# seed random number each time the script is run based on system time
seed()

class Game:
  def __init__(self):
    # get a word from a random index of word_bank
    self.word = list(word_bank[randint(0, len(word_bank) - 1)])
    self.game_over = True
    self.hangman = ['-', '-o', '-o-', '-o-|', '-o-|-', '-o-|-<']
    self.hangman_display = self.hangman[0]
    self.guesses = [] # display letters chosen by the player
    self.display = ['_'] * len(self.word) # generate a string/array the same len of self.word consisting only of underscores
    self.wrong_guesses = 0

  def __str__(self):
    # print current Game's word
    return f'''The secret word is {self.word} 
    its length is {len(self.word)}, 
    the game is displaying {self.display}, 
    its len is {len(self.display)}'''

  def take_turn(self):
    self.game_over = False

    if self.game_over == False:
      print('------------------------------------\n')
      if self.guesses:
        print('\nGUESSES: \n{}\n'.format(self.guesses))
      print('THE GALLOWS: \n\n{}\n'.format(self.hangman_display))
      print('SECRET WORD: \n {}\n'.format(self.display))
      guess = input('Enter a Letter\n')
      # replace underscore with correct guess at indeces found
      chars_found = [i for i in range(len(self.word)) if self.word[i] == guess]

      if chars_found:
        for i in range(len(chars_found)):
          index = chars_found[i] # store the indeces of the word where guess letter matches
          self.display[index] = guess # change the display word at the found indeces to match user guess
        self.guesses.append(guess)
        
        if '_' not in self.display:
          self.game_over = False
          print('\nThe secret word was: '+''.join(self.word) + '\n\nYOU WIN!\n')
        else:
          self.take_turn() # recursive call

      else:
        self.guesses.append(guess)
        self.wrong_guesses += 1
        self.hangman_display = self.hangman[self.wrong_guesses]
        if self.wrong_guesses >= 5:
          self.game_over = True
          print('\nGAME OVER!')
        else:
          self.take_turn()

print('!HANGED-MAN!\n')
new_game = Game()
new_game.take_turn()