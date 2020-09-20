import random, time, pygame, sys
from pygame.locals import *

black = (0, 0, 0)
red = (255, 0, 0)
pynk = (255, 213, 213)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

def main():
    pygame.init()
    pygame.mixer.init()
    sysfont = pygame.font.get_default_font()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Hangman')

    # start main loop
    while True:

        # draw screen and an empty Hangman
        screen.fill(pynk)
        # heady
        pygame.draw.circle(screen, black, (200, 175), 25, 5)
        # body
        pygame.draw.line(screen, black, (200, 200), (200, 300), 5)
        # left arm
        pygame.draw.line(screen, black, (150, 200), (200, 225), 5)
        # right arm
        pygame.draw.line(screen, black, (200, 225), (250, 200), 5)
        # left leg
        pygame.draw.line(screen, black, (150, 350), (200, 300), 5)
        # right leg
        pygame.draw.line(screen, black, (200, 300), (250, 350), 5)
        # pole
        pygame.draw.lines(screen, black, False, [(200, 150), (200, 100), (400, 100), (400, 350)], 5)
        # base
        pygame.draw.rect(screen, black, (350, 350, 100, 50), 5)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.flip()
                pygame.quit()
                sys.exit(0)
        # change buffers
        pygame.display.flip()

if __name__ == '__main__':
    main()
