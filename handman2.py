import random, time, pygame, sys
from pygame.locals import *

black = (0, 0, 0)
pynk = (255, 213, 213)
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
        if len(word) == len(good_guess):
            print("congratulations you win! The word was: "+word)
            pa = input("Want to play again? (Y/N)")
            playagain = pa.upper()
            if playagain == 'Y':
                return hangman(word_list)
            else:
                exit()
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
        # screen.blit(pygame.font.SysFont(sysfont, 40).render("2 =  _", True, black), (20, 150))
        # screen.blit(pygame.font.SysFont(sysfont, 40).render("3 =  _", True, black), (20, 200))
        # screen.blit(pygame.font.SysFont(sysfont, 40).render("4 =  _", True, black), (20, 250))
        # screen.blit(pygame.font.SysFont(sysfont, 40).render("5 =  _", True, black), (20, 300))
        # screen.blit(pygame.font.SysFont(sysfont, 40).render("6 =  _", True, black), (20, 350))

        screen.blit(pygame.font.SysFont(sysfont, 50).render(result_spaces, True, black), (20, 420))
        screen.blit(pygame.font.SysFont(sysfont, 25).render("Enter a letter: ", True, black), (20, 470))
        body_hangman(tries_left)

        pygame.display.flip()
        key_name = ''
        aa=0
        guess = ''
        while aa==0:
            for event in pygame.event.get():
                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    # key name
                    key_name = pygame.key.name(event.key)
                    # uppercase the key
                    guess = key_name.upper()
                    #parts +=1
                    aa=1
                if event.type == QUIT:
                    pygame.display.flip()
                    pygame.quit()
                    sys.exit(0)
		# change buffers
        #pygame.display.flip()

        print(result_spaces)
        #guess = input("Enter a letter: ").upper()
        # if len(guess) > 1:
        #     screen.blit(pygame.font.SysFont(sysfont, 25).render("Please enter only one letter", True, black), (140, 470))
        #     pygame.display.flip()
        #     time.sleep(1)
        #     print("Please enter only one letter")
        if guess in letters_guess:
            screen.blit(pygame.font.SysFont(sysfont, 25).render("sorry the letter "+guess+" has already been picked", True, black), (140, 470))
            pygame.display.flip()
            time.sleep(1)
            print('🤦🏻‍♀️', guess)
            print("sorry the letter "+guess+" has already been picked")
        elif guess not in word:
            screen.blit(pygame.font.SysFont(sysfont, 25).render("Sorry "+guess+" is not in the word", True, black), (140, 470))
            # pygame.display.flip()
            # time.sleep(1)
            print("Sorry "+guess+" is not in the word")
            tries_left -= 1
            # body_hangman(tries_left)
            screen.blit(pygame.font.SysFont(sysfont, 25).render("You have: "+str(tries_left)+" tries left!", True, black), (100, 30))
            pygame.display.flip()
            # time.sleep(1)
            print("💃🏻", guess)
            letters_guess.append(guess)
            fail_letters.append(guess)
            print("You have: "+str(tries_left)+" tries left!")
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
            try_win(word, good_guess)
            screen.blit(pygame.font.SysFont(sysfont, 25).render("Good job the Letter: "+guess+" is in the word", True, black), (140, 470))
            pygame.display.flip()
            time.sleep(1)
            print("Good job the Letter: "+guess+" is in the word")
            #tries_left -= 1

    if tries_left == 0:
        screen.blit(pygame.font.SysFont(sysfont, 25).render("Better luck next time, the word was: ", True, black), (20, 50))
        pygame.display.flip()
        time.sleep(3)
        print("Better luck next time, the word was: ", word)
        #pa = input("Want to play again? (Y/N)")
        #playagain = pa.upper()
        #if playagain == 'Y':
        #    return hangman(word_list)
        #else:
        #exit()
        pygame.quit()
        sys.exit(0)
    pygame.display.flip()


if __name__ == '__main__':
	main(word_list)
#hangman(word_list)

# todo:
