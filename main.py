import pygame, sys
from settings import *

class Tile:
    def __init__(self, screen, pointx, pointy, x,y):
        self.pointx = pointx
        self.pointy = pointy
        self.size = tile_size
        self.isActive = True
        self.screen = screen
        self.x = x
        self.y = y

    def draw_tile(self):
        #pygame.draw.Rect(self.screen, self.color1, self.size /2, self.size/2)
        pygame.draw.rect(self.screen, rect_color[self.x], (self.pointx, self.pointy, self.size, self.size))
        pygame.draw.ellipse(self.screen, circle_color[self.y], (self.pointx, self.pointy, self.size / 2, self.size / 2))


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.running = True
        self.tile = []




    def draw_grid(self):


        for x in range(board_width):
            for y in range(board_width):
                startx = (x * tile_size) + XMARGIN
                starty = (y * tile_size) + YMARGIN
                endy = YMARGIN + (board_height * tile_size)

                self.tile.append( Tile(self.screen, startx,starty, x,y))

        for tile in range(len(self.tile)):
            self.tile[tile].draw_tile()





        for x in  range(board_width + 1):
            startx = (x * tile_size) + XMARGIN
            starty = YMARGIN
            endx = (x * tile_size) + XMARGIN
            endy = YMARGIN + (board_height * tile_size)


            pygame.draw.line(self.screen, WHITE, (startx, starty), (endx, endy))
        for y in  range(board_height + 1):
            startx = XMARGIN
            starty = (y * tile_size) + YMARGIN
            endx = XMARGIN + (board_width * tile_size)
            endy = (y * tile_size) + YMARGIN
            pygame.draw.line(self.screen, WHITE, (startx, starty), (endx, endy))

        #draw tiles




    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False;

    def run(self):
        while self.running:
            self.screen.fill(BLACK)
            self.draw_grid()
            self.events()
            pygame.display.flip()




game = Game()
game.run()

'''
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

    if pygame.mouse.get_pressed() == (1,0,0):
        print(pygame.mouse.get_pos())


'''