import pygame
import random
from MancalaBoard import MancalaBoard
# Initialize Pygame
pygame.init()
# create a font object.
font = pygame.font.Font('Arial.ttf', 30)
# Set the window size
WIDTH, HEIGHT = (1300, 700)
# rgb
LIGHT_GRAY = (150, 150, 150)
DARK_GRAY = (40, 40, 40)
BLACK = (0, 0, 0)
BLUE = (131, 140, 222)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set the board properties
board_width = WIDTH-100
board_height = HEIGHT-100
board_color = DARK_GRAY
board_x = 50
board_y = 50

# Set the fosse properties
fosse_width = 55
fosse_color = LIGHT_GRAY
fosse_spacing = 70

# Set the store properties
store_width = 100
store_height = HEIGHT-300
store_color = LIGHT_GRAY
store1_x = 150
store1_y = 150
store2_x = WIDTH-250
store2_y = 150

# Set the seeds properties
seed_width=15
seed_color=[(221,160,221),(230,220,240),(238,130,238),(255,0,255),(147,112,219),(75,0,130),(216,191,216),(218,112,214),(186,85,211),(138,43,226),(176,224,230),(135,206,250),(0,191,255),(100,149,237),(123,104,238),(106,90,205),(72,61,139),(65,105,225),(0,0,255),(0,0,205),(0,0,139),(0,0,128),(25,25,112),(95,158,160),(255,160,122),(250,128,114),(240,128,128),(220,20,60),(178,34,34),(219,112,147),(0,250,154),(255,218,185),(199,21,133),(255,192,203),(255,105,180),(255,20,147),(127,255,212),(0,206,209),(0,139,139),(255,215,0),(152,251,152),(165,42,42),(255,127,80),(255,99,71),(255,69,0),(255,140,0)]

class Drawer:
    def __init__(self):
        self.screen = pygame.display.set_mode((1300, 700))
        # Set the title of the window
        pygame.display.set_caption("Mancala")
        self.board = dict()
        self.drawBoard()
        self.drawFosses()
        self.drawStore1()
        self.drawStore2()
        for cle, valeur in self.board.items():
            self.drawSeed(valeur)
            self.drawSeed(valeur)
            self.drawSeed(valeur)
            self.drawSeed(valeur)
            if(cle in ["A", "B", "C", "D", "E", "F"]):
                self.PitValue(valeur,4,-100)
            else:self.PitValue(valeur,4,100)


    def drawBoard(self):
        pygame.draw.rect(self.screen, board_color, (board_x, board_y,
                         board_width, board_height), width=0, border_radius=50)
        pygame.display.flip()

    def drawStore1(self):
        pygame.draw.rect(self.screen, store_color, (store1_x, store1_y,
                         store_width, store_height), width=0, border_radius=50)
        pygame.display.flip()

    def drawStore2(self):
        pygame.draw.rect(self.screen, store_color, (store2_x, store2_y,
                         store_width, store_height), width=0, border_radius=50)
        pygame.display.flip()

    def drawFosses(self):
        # Draw fosses
        m = MancalaBoard()
        f1 = m.fosses1
        f2 = m.fosses2
        fosse_y = HEIGHT-200
        for i in range(len(f1)):
            fosse_x = 335 + (i * (fosse_width + fosse_spacing))
            #pygame.draw.rect(self.screen, fosse_color, (fosse_x, fosse_y, fosse_width, fosse_height),width=0, border_radius=20)
            pygame.draw.circle(self.screen, fosse_color,
                               (fosse_x, fosse_y), fosse_width)
            self.board[f1[i]] = (fosse_x, fosse_y)
        fosse_y = 200
        for i in range(len(f2)):
            fosse_x = 335 + (i * (fosse_width + fosse_spacing))
            pygame.draw.circle(self.screen, fosse_color,
                               (fosse_x, fosse_y), fosse_width)
            self.board[f2[i]] = (fosse_x, fosse_y)
        print(self.board)
        pygame.display.flip()

    def drawSeed(self,cor):
        x,y=cor
        x=x+random.randint(-30, 30)
        y=y+random.randint(-30, 30)
        pygame.draw.circle(self.screen, random.choice(seed_color),
                               (x,y), seed_width)
        pygame.draw.circle(self.screen, BLACK,
                               (x,y), seed_width,1)
        pygame.display.flip()
    def PitValue(self,cor,value,add):
        x,y=cor
        y=y+add
        # create a text surface object,
        # # on which text is drawn on it.
        text = font.render(f"{value}", True, WHITE, DARK_GRAY)
        # create a rectangular object for the
        # # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = x,y
        self.screen.blit(text,textRect)
        pygame.display.flip()

    def updateFosses(self, lettre):
        pygame.draw.circle(self.screen, fosse_color,
                           self.board[lettre], fosse_width)
        pygame.display.flip()
