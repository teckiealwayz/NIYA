import pygame, sys, random
from settings import *
from functions import *

class Tile:
    def __init__(self, screen, pointx, pointy, x,y, counter):
        self.startx = pointx
        self.starty = pointy
        self.size = tile_size
        self.screen = screen
        self.x = x
        self.y = y
        self.counter = counter


    def draw_tile(self):

        print "inside tile", COLORS
        print self.counter
        pygame.draw.rect(self.screen, list_colors[self.counter][0], (self.startx, self.starty, self.size, self.size))
        self.color = list_colors[self.counter][0]
        pygame.draw.ellipse(self.screen, list_colors[self.counter][1], (self.startx, self.starty, self.size / 2, self.size / 2))
        self.color2 = list_colors[self.counter][1]

    def update(self, x, y, turn):

        if self.startx < x < self.startx + self.size and self.starty < y < self.starty + self.size:

            if turn % 2 == 0:
                pygame.draw.rect(self.screen, BLACK, (self.startx, self.starty, self.size, self.size))
                pygame.draw.rect(self.screen, self.color,
                                 (XMARGIN - self.size * 1.2, screen_height / 2, self.size, self.size))
                pygame.draw.ellipse(self.screen, self.color2,
                                    (XMARGIN - self.size * 1.2, screen_height / 2, self.size / 2, self.size / 2))

            else:
                pygame.draw.rect(self.screen, RED, (self.startx, self.starty, self.size, self.size))
                pygame.draw.rect(self.screen, self.color, (
                XMARGIN + board_width * self.size + self.size / 3, screen_height / 2, self.size, self.size))
                pygame.draw.ellipse(self.screen, self.color2, (
                XMARGIN + board_width * self.size + self.size / 3, screen_height / 2, self.size / 2, self.size / 2))


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.fill(SPRING_GREEN)
        self.running = True
        self.tile = []
        self.counter = 0
        self.color_count = 0
        self.list_count = 0
        self.x = 0
        self.y = 0
        self.player_turn = 0

    def draw_board(self):



        for x in range(board_width):
            if self.color_count < 4:
                random.shuffle(COLORS)
                random.shuffle(COLORS2)
                self.color_count += 1
            for y in range(board_width):
                startx = (x * tile_size) + XMARGIN
                starty = (y * tile_size) + YMARGIN
                endy = YMARGIN + (board_height * tile_size)
                # if(self.counter > 3):
                #     self.counter = 0

                self.tile.append( Tile(self.screen, startx,starty, x,y, self.counter))
                self.tile[self.list_count].draw_tile()
                self.counter += 1
                self.list_count += 1



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


    def update(self):

        for tile in range(len(self.tile)):
            self.tile[tile].update(self.x,self.y, self.player_turn)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False;
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                self.player_turn += 1
                self.x, self.y = event.pos
                print("Mouse clicked", event.pos)

    def run(self):
        self.screen.fill(SPRING_GREEN)
        pygame.display.flip()
        self.draw_board()

        while self.running:
            self.events()
            self.update()
            pygame.display.flip()




start = True
instruct = True

game = Game()
title(game.screen)

while start:

    pygame.event.pump()
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    if (menu(game.screen) == "Instructions"):
        instructions(game.screen)
        # if pygame.mouse.get_pressed() == (1,0,0):
        #     print("Clicked")
    elif (menu(game.screen) == "Start"):
        start = False
        game.run()