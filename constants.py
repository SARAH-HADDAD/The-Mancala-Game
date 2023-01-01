import pygame
pygame.init()

# The cols have to be even, there are two rows
ROWS, COLS = 2, 6
WIDTH, HEIGHT = 1300, 700

# Game configurations
STARTING_PIECES = 6

# Game drawing
TABLE_PADDING_WIDTH = 10
TABLE_PADDING_HEIGHT = 50
TABLE_CORNER_RADIUS = 50

BOWL_SIZE = 60
BOWL_SELECTED_WIDTH = 5
NUM_BOWLS_ROW = COLS
# Bowl padding needs to be calculated for symmetry
BOWL_PADDING_X = ((WIDTH - TABLE_PADDING_WIDTH*2) - (BOWL_SIZE*(NUM_BOWLS_ROW+2))) // (NUM_BOWLS_ROW+2 + 1) # Two stores, and then one more
BOWL_PADDING_Y = 130

PIECE_SIZE = 15
PIECE_OUTLINE = 5
PIECE_SPREAD_PADDING = 20


DRAW_MOVE_DELAY = 300 # milliseconds
TURN_INDICATOR_SIZE = 25
TURN_INDICATOR_WIDTH = 5


# rgb
LIGHT_BROWN = (232, 200, 144)
DARK_BROWN = (205, 153, 102)
BLACK = (0, 0, 0)
BLUE = (131, 140, 222)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# fonts
VALUE_FONT = pygame.font.Font("freesansbold.ttf", 40)

# variations
CAPTURE_EMPTY = False
END_CAPTURE = True