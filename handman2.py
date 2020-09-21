import random, time, pygame, sys
from pygame.locals import *

black = (0, 0, 0)
pynk = (255, 213, 213)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
word_list = ['Hello', 'Computer', 'Together', 'Dog', 'Later', 'Yesterday']
parts = 0

def main(lst1):
#def hangman(lst1):
    pygame.init()
    sysfont = pygame.font.get_default_font()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Hangman')


    word1 = random.choice(lst1)
    word = word1.upper()
    print(word)
    result_spaces = "_ " * len(word)
    letters_guess = []
    fail_letters = []
    good_guess = []
    tries_left = 6

    def try_win(word, good_guess):
        input1 = ''
        if len(word) == len(good_guess):
            sysfont = pygame.font.get_default_font()
            size = width, height = 500, 500
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Hangman')
            screen.fill(white)
            screen.blit(pygame.font.SysFont(sysfont, 60).render("You Won! the word was: "+word, True, red), (20, 50))
            screen.blit(pygame.font.SysFont(sysfont, 60).render("wan't to play again?(y/n)", True, blue), (20, 200))
            pygame.display.flip()
            while aa==0:
                for event in pygame.event.get():
                    if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                        key_name = pygame.key.name(event.key)
                        input1 = key_name.upper()
                    if event.type == QUIT:
                        pygame.display.flip()
                        pygame.quit()
                        sys.exit(0)
                if input1 == 'Y':
                    return main(lst1)
                elif input1 == 'N':
                    pygame.quit()
                    sys.exit(0)
        else:
            return False

    def body_hangman(tries_left):
        if tries_left <= 5:
            pygame.draw.circle(screen, black, (200, 175), 25, 5)
        if tries_left <= 4:
            pygame.draw.line(screen, black, (200, 200), (200, 300), 5)
        if tries_left <= 3:
            pygame.draw.line(screen, black, (150, 200), (200, 225), 5)
        if tries_left <= 2:
            pygame.draw.line(screen, black, (200, 225), (250, 200), 5)
        if tries_left <= 1:
            pygame.draw.line(screen, black, (150, 350), (200, 300), 5)
        if tries_left == 0:
            pygame.draw.line(screen, black, (200, 300), (250, 350), 5)
        pygame.display.flip()
		# pole


    while tries_left > 0:

        # draw screen and an empty Hangman
        screen.fill(pynk)
        pygame.draw.lines(screen, black, False, [(200, 150), (200, 100), (400, 100), (400, 350)], 5)
		# base
        pygame.draw.rect(screen, black, (350, 350, 100, 50), 5)
        resultstr1 = " ".join(fail_letters)
        screen.blit(pygame.font.SysFont(sysfont, 40).render("Letters used: "+resultstr1, True, black), (20, 50))
        screen.blit(pygame.font.SysFont(sysfont, 50).render(result_spaces, True, black), (20, 420))
        screen.blit(pygame.font.SysFont(sysfont, 25).render("Enter a letter: ", True, black), (20, 470))
        screen.blit(pygame.font.SysFont(sysfont, 25).render("You have: "+str(tries_left)+" tries left!", True, red), (100, 30))
        body_hangman(tries_left)

        pygame.display.flip()
        key_name = ''
        aa=0
        guess = ''
        while aa==0:
            for event in pygame.event.get():
                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    key_name = pygame.key.name(event.key)
                    guess = key_name.upper()
                    aa=1
                if event.type == QUIT:
                    pygame.display.flip()
                    pygame.quit()
                    sys.exit(0)

        if guess in letters_guess:
            screen.blit(pygame.font.SysFont(sysfont, 25).render("sorry the letter "+guess+" has already been picked", True, black), (140, 470))
            pygame.display.flip()
            time.sleep(1)
        elif guess not in word:
            screen.blit(pygame.font.SysFont(sysfont, 25).render("Sorry "+guess+" is not in the word", True, black), (140, 470))
            time.sleep(1.5)
            tries_left -= 1
            pygame.display.flip()
            time.sleep(1)
            letters_guess.append(guess)
            fail_letters.append(guess)
        else:
            letters_guess.append(guess)
            word_guess_list = list(result_spaces)
            answer_list = list(word)
            for i in range(len(answer_list)):
                if answer_list[i] == guess:
                    position = i * 2
                    word_guess_list.insert(position, answer_list[i])
                    good_guess.append(guess)
                    word_guess_list.pop(position+1)
                    result_spaces = "".join(word_guess_list)
            screen.blit(pygame.font.SysFont(sysfont, 25).render("Good job the Letter: "+guess+" is in the word", True, black), (140, 470))
            pygame.display.flip()
            time.sleep(1)
            try_win(word, good_guess)

    if tries_left == 0:
        screen.blit(pygame.font.SysFont(sysfont, 25).render("Better luck next time, the word was: "+word+"Try again? (Y/N)", True, black), (20, 50))
        pygame.display.flip()
        time.sleep(1)
    pygame.display.flip()


if __name__ == '__main__':
	main(word_list)
#hangman(word_list)

# todo:
