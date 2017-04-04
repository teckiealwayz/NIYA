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
    print("Welcome")
