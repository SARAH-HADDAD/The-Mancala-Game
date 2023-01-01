import pygame
from constants import BLUE, BLACK
from constants import PIECE_SIZE, PIECE_OUTLINE

class Piece:
     def __init__(self, coords):
          self.coords = coords

     def draw(self, win):
          pygame.draw.circle(win, BLUE, self.coords, PIECE_SIZE)
          pygame.draw.circle(win, BLACK, self.coords, PIECE_SIZE, width=PIECE_OUTLINE)