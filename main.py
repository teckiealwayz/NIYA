import pygame
import sys
from functions import *
from settings import *

# initialize pygame
pygame.init()
# boolean variable for game loop
running = True
# Open a window on the screen
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("NIYA")

# Call to the menu function to display title then menu
title(screen)
menu(screen)

# Main game loop
while running:

    pygame.event.pump()
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()