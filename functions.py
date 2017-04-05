import pygame
from settings import *

def title(screen):
    screen.fill(WHITE)
    pygame.display.flip()
    img = pygame.image.load("NIYA_INTRO.png").convert_alpha()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    screen.fill(BLACK)
    pygame.time.delay(2000)
    pygame.display.flip()

def menu(screen):

    myfont = pygame.font.SysFont("monospace", 15)

    # render text
    instructions = myfont.render("Instructions", 1, WHITE)
    start = myfont.render("Start", 1, WHITE)
    menu = myfont.render("Menu", 1, WHITE)
    screen.blit(menu, (300, 50))
    screen.blit(instructions, (500, 300))
    screen.blit(start, (100,300))
    pygame.display.flip()
    print("Welcome\nMenu\nInstructions\nStart")
