import random, time, pygame, sys
from pygame.locals import *

black = (0, 0, 0)
pynk = (255, 213, 213)
red = (255, 0, 0)
word_list = ['Hello', 'Computer', 'Together', 'Dog', 'Later', 'Yesterday']


def main(lst1):
#def hangman(lst1):
    pygame.init()
    sysfont = pygame.font.get_default_font()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Hangman')

    word1 = random.choice(lst1)
    word = word1.upper()
    # print(word)
    word_letter_sort = sorted(word)
    word_letter = []
    for i in word_letter_sort:
        if i not in word_letter:
            word_letter.append(i)

    result_spaces = "_ " * len(word)
    result_spaces1 = "_" * len(word)
    letters_guess = []
    fail_letters = []
    good_guess = []
    tries_left = 6
    cuenta = 0


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
        if len(word_letter) == len(good_guess):
            time.sleep(2)
            screen.fill(pynk)
            screen.blit(pygame.font.SysFont(sysfont, 40).render("Want to play again? (Y/N)", True, red), (20, 50))
            pygame.display.flip()
            bb=0
            p_a = ""
            while bb==0:
                for event in pygame.event.get():
                    if event.type in (pygame.KEYDOWN,):
                        key_name = pygame.key.name(event.key)
                        p_a = key_name.upper()
                        if p_a == 'Y':
                            return main(word_list)
                        else:
                            pygame.quit()
                            sys.exit(0)
                    if event.type == QUIT:
                        pygame.display.flip()
                        pygame.quit()
                        sys.exit(0)

        key_name = ''
        aa=0
        guess = ''
        while aa==0:
            for event in pygame.event.get():
                #if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                if event.type in (pygame.KEYDOWN,):
                    key_name = pygame.key.name(event.key)
                    guess = key_name.upper()
                    aa=1
                if event.type == QUIT:
                    pygame.display.flip()
                    pygame.quit()
                    sys.exit(0)

        if guess in letters_guess:
            screen.blit(pygame.font.SysFont(sysfont, 25).render("Sorry the letter "+guess+" has already been picked", True, black), (140, 470))
            pygame.display.flip()
            time.sleep(2)
        elif guess not in word:
            letters_guess.append(guess)
            fail_letters.append(guess)
            screen.blit(pygame.font.SysFont(sysfont, 25).render("Sorry "+guess+" is not in the word", True, black), (140, 470))
            pygame.display.flip()
            time.sleep(2)
            tries_left -= 1
        else:
            letters_guess.append(guess)
            word_guess_list = list(result_spaces)
            answer_list = list(word)
            for i in range(len(answer_list)):
                if answer_list[i] == guess:
                    #print(cuenta)
                    cuenta +=1
                    position = i * 2
                    #print(word_guess_list)
                    word_guess_list.insert(position, answer_list[i])
                    #print(word_guess_list)
                    word_guess_list.pop(position+1)
                    #print(word_guess_list)
                    if guess not in good_guess:
                        good_guess.append(guess)
                    #print(good_guess)
                    result_spaces = "".join(word_guess_list)
            #screen.blit(pygame.font.SysFont(sysfont, 50).render(result_spaces, True, black), (20, 420))
            screen.blit(pygame.font.SysFont(sysfont, 25).render("Good job the Letter: "+guess+" is in the word", True, black), (140, 470))
            pygame.display.flip()
            time.sleep(2)
            #print(len(word_letter))
            #print(len(good_guess))




    if tries_left == 0:
        pygame.draw.line(screen, black, (200, 300), (250, 350), 5)
        screen.blit(pygame.font.SysFont(sysfont, 25).render("Better luck next time, the word was: "+word, True, black), (20, 80))
        pygame.display.flip()
        time.sleep(3)
        screen.fill(pynk)
        screen.blit(pygame.font.SysFont(sysfont, 40).render("Want to play again? (Y/N)", True, red), (20, 50))
        pygame.display.flip()
        bb = 0
        p_a = ""
        while bb==0:
            for event in pygame.event.get():
                if event.type in (pygame.KEYDOWN,):
                    key_name = pygame.key.name(event.key)
                    p_a = key_name.upper()
                    if p_a == 'Y':
                        return main(word_list)
                    else:
                        pygame.quit()
                        sys.exit(0)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)






    pygame.display.flip()


if __name__ == '__main__':
	main(word_list)
