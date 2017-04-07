import pygame
from settings import *

def title(screen):
    screen.fill(WHITE)
    pygame.display.flip()
    img = pygame.image.load("NIYA_INTRO.png").convert_alpha()
    screen.blit(img, (-20, 0))
    pygame.display.flip()
    screen.fill(BLACK)
    pygame.time.delay(2000)
    pygame.display.flip()

def instructions(screen):
    screen.fill(BLACK)
    pygame.display.flip()
    myfont = pygame.font.SysFont("monospace", 15)
    instruct = myfont.render("These are the instructions", 1, WHITE)
    i = screen.blit(instruct, (200,300))
    pygame.display.flip()
    if pygame.KEYDOWN == pygame.K_0:
        return "in"
def menu(screen):

    myfont = pygame.font.SysFont("monospace", 15)
    # render text
    instructions = myfont.render("Instructions", 1, WHITE)
    start = myfont.render("Start", 1, WHITE)
    menu = myfont.render("Menu", 1, WHITE)
    screen.blit(menu, (300, 50))
    i = screen.blit(instructions, (450, 300))
    s = screen.blit(start, (100,300))
    pygame.display.flip()
    if pygame.mouse.get_pressed() == (1,0,0):
        if s.collidepoint(pygame.mouse.get_pos()):
            return "Start"
        elif i.collidepoint(pygame.mouse.get_pos()):
            return "Instructions"

