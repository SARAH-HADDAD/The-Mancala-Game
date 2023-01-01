import pygame
from MancalaBoard import MancalaBoard
# Initialize Pygame
pygame.init()

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

class Drawer:
     def __init__(self):
          self.screen=pygame.display.set_mode((1300, 700))
          # Set the title of the window
          pygame.display.set_caption("Mancala")
          self.board=dict()
          self.drawBoard()
          self.drawfosses()
          self.drawStore1()
          self.drawStore2()
        
     def drawBoard(self):
        pygame.draw.rect(self.screen, board_color, (board_x, board_y, board_width, board_height),width=0, border_radius=50)
        pygame.display.flip()

     def drawStore1(self):
        pygame.draw.rect(self.screen, store_color, (store1_x, store1_y, store_width, store_height),width=0, border_radius=50)
        pygame.display.flip()

     def drawStore2(self):
        pygame.draw.rect(self.screen, store_color, (store2_x, store2_y, store_width, store_height),width=0, border_radius=50)
        pygame.display.flip()
     def drawfosses(self):
        # Draw the fosses
        m=MancalaBoard()
        f1=m.fosses1
        f2=m.fosses2
        fosse_y = HEIGHT-200
        for i in range(len(f1)):
            fosse_x = 335+ (i * (fosse_width + fosse_spacing))
            #pygame.draw.rect(self.screen, fosse_color, (fosse_x, fosse_y, fosse_width, fosse_height),width=0, border_radius=20)
            pygame.draw.circle(self.screen, fosse_color, (fosse_x, fosse_y), fosse_width)
            self.board[f1[i]]=(fosse_x, fosse_y)
        fosse_y = 200
        for i in range(len(f2)):
            fosse_x = 335+ (i * (fosse_width + fosse_spacing))
            pygame.draw.circle(self.screen, fosse_color, (fosse_x, fosse_y), fosse_width)
            self.board[f2[i]]=(fosse_x, fosse_y)
        print(self.board)
        pygame.display.flip()
     def updatefosses(self,lettre):
        pygame.draw.circle(self.screen, fosse_color, self.board[lettre], fosse_width)
        pygame.display.flip()


    
    
    







