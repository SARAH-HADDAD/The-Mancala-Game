# For testing, let's just draw in the terminal

import pygame
from constants import LIGHT_BROWN, DARK_BROWN, BLACK, BLUE, WHITE, GREEN
from constants import BOWL_SIZE, BOWL_PADDING_X, BOWL_PADDING_Y, NUM_BOWLS_ROW, BOWL_SELECTED_WIDTH
from constants import TABLE_PADDING_WIDTH, TABLE_PADDING_HEIGHT, TABLE_CORNER_RADIUS
from constants import PIECE_SIZE, PIECE_SPREAD_PADDING, PIECE_OUTLINE
from constants import WIDTH, HEIGHT 
from constants import VALUE_FONT, TURN_INDICATOR_SIZE, TURN_INDICATOR_WIDTH
import random

class Drawer:
     def __init__(self):
          pass

     def draw_terminal(self, game):
          # We draw print the first column first, then the stores, and then the last column
          print()
          print(game.state.board)
          print()
     
     def draw(self, win, board, pieces, left_store, right_store, active_player, selected):
          win.fill(DARK_BROWN)
          self.draw_table(win)
          self.draw_bowl(win, board, pieces, selected)
          self.draw_store(win, left_store, right_store, pieces)
          self.draw_active_player(win, active_player)

     def draw_active_player(self, win, active_player):
          # I'm gonna try and draw a green circle in the corner
          xcoords = TABLE_PADDING_WIDTH + BOWL_PADDING_X//2 if active_player == "left" else WIDTH - (TABLE_PADDING_WIDTH + BOWL_PADDING_X//2)
          ycoords = TABLE_PADDING_HEIGHT + BOWL_PADDING_Y//3
          pygame.draw.circle(win, GREEN, (xcoords, ycoords), TURN_INDICATOR_SIZE)
          pygame.draw.circle(win, BLACK, (xcoords, ycoords), TURN_INDICATOR_SIZE, TURN_INDICATOR_WIDTH)

     def draw_bowl(self, win, board, pieces, selected):
          # Ignore the first spot, that's where the store goes
          # The distance from the edge is padding_y
          # Assume there are two rows
          board_row = 0

          bowl_coords = (
               TABLE_PADDING_WIDTH + BOWL_PADDING_X*2 + BOWL_SIZE + BOWL_SIZE//2, 
               TABLE_PADDING_HEIGHT + BOWL_PADDING_Y + BOWL_SIZE//2
          )
          for board_col in range(NUM_BOWLS_ROW):
               # Here also goes in all the pieces
               pygame.draw.circle(win, DARK_BROWN, bowl_coords, BOWL_SIZE)
               self.draw_bowl_value(win, board[board_row][board_col], bowl_coords)
               self.draw_piece(win, pieces, (board_row, board_col))

               # Draw the selected bowl if there is one
               if selected == (board_row, board_col):
                    pygame.draw.circle(win, WHITE, bowl_coords, BOWL_SIZE, BOWL_SELECTED_WIDTH)

               bowl_coords = (bowl_coords[0] + BOWL_SIZE + BOWL_PADDING_X, bowl_coords[1]) # Y does not change
          
          # Repeat for the second column
          board_row = 1

          bowl_coords = (
               TABLE_PADDING_WIDTH + BOWL_PADDING_X*2 + BOWL_SIZE + BOWL_SIZE//2, 
               HEIGHT - (TABLE_PADDING_HEIGHT + BOWL_PADDING_Y + BOWL_SIZE//2)
          )
          for board_col in range(NUM_BOWLS_ROW):
               pygame.draw.circle(win, DARK_BROWN, bowl_coords, BOWL_SIZE)
               self.draw_bowl_value(win, board[board_row][board_col], bowl_coords)
               self.draw_piece(win, pieces, (board_row, board_col))

               # Draw the selected bowl if there is one
               if selected == (board_row, board_col):
                    pygame.draw.circle(win, WHITE, bowl_coords, BOWL_SIZE, BOWL_SELECTED_WIDTH)

               bowl_coords = (bowl_coords[0] + BOWL_SIZE + BOWL_PADDING_X, bowl_coords[1])

     def draw_store(self, win, left_store, right_store, pieces):
          # The upper bound is the first columns y-cord
          # The lower is the same, but the second column
          # Draw circles with the same size at these points
          # And then a rectangel between with the diameter as the width
          store_width = BOWL_SIZE*2
          store_height = (HEIGHT - (TABLE_PADDING_HEIGHT + BOWL_PADDING_Y + BOWL_SIZE//2)) - (TABLE_PADDING_HEIGHT + BOWL_PADDING_Y + BOWL_SIZE//2)

          upper_coords = (
               TABLE_PADDING_WIDTH + BOWL_PADDING_X + BOWL_SIZE//2, 
               TABLE_PADDING_HEIGHT + BOWL_PADDING_Y + BOWL_SIZE//2
          )

          lower_coords = (
               TABLE_PADDING_WIDTH + BOWL_PADDING_X + BOWL_SIZE//2, 
               HEIGHT - (TABLE_PADDING_HEIGHT + BOWL_PADDING_Y + BOWL_SIZE//2)
          )

          pygame.draw.circle(win, DARK_BROWN, upper_coords, BOWL_SIZE)
          pygame.draw.circle(win, DARK_BROWN, lower_coords, BOWL_SIZE)
          # Now the in-between
          pygame.draw.rect(win, DARK_BROWN, (upper_coords[0] - BOWL_SIZE, upper_coords[1], store_width, store_height))
          # Then the value
          self.draw_store_value(win, left_store, upper_coords)
          self.draw_piece(win, pieces, "left")

          # Now the same for the other side
          upper_coords = ( # Only X needs to change
               WIDTH - (TABLE_PADDING_WIDTH + BOWL_PADDING_X + BOWL_SIZE//2), 
               TABLE_PADDING_HEIGHT + BOWL_PADDING_Y + BOWL_SIZE//2
          )

          lower_coords = (
               WIDTH - (TABLE_PADDING_WIDTH + BOWL_PADDING_X + BOWL_SIZE//2), 
               HEIGHT - (TABLE_PADDING_HEIGHT + BOWL_PADDING_Y + BOWL_SIZE//2)
          )

          pygame.draw.circle(win, DARK_BROWN, upper_coords, BOWL_SIZE)
          pygame.draw.circle(win, DARK_BROWN, lower_coords, BOWL_SIZE)
          # Now the in-between
          pygame.draw.rect(win, DARK_BROWN, (upper_coords[0] - BOWL_SIZE, upper_coords[1], store_width, store_height))
          # Then the value
          self.draw_store_value(win, right_store, upper_coords)
          self.draw_piece(win, pieces, "right")


     def draw_table(self, win):
          table_width = WIDTH - (TABLE_PADDING_WIDTH*2) # There is padding on both sides
          table_height = HEIGHT - (TABLE_PADDING_HEIGHT*2)
          table_cords = self.get_coords_from_center(WIDTH//2, HEIGHT//2, table_width, table_height)
          pygame.draw.rect(win, LIGHT_BROWN, (table_cords[0], table_cords[1], table_width, table_height))

          # Now I want smooth edges, whitch works by hiding the corners and drawing circles
          table_corners_cords = (table_cords, 
          (table_cords[0], table_cords[1] + table_height), 
          (table_cords[0] + table_width, table_cords[1]), 
          (table_cords[0] + table_width, table_cords[1] + table_height))

          for corner_cords in table_corners_cords:
               # We need to now which quadrant we are in
               change_x = 1 if corner_cords[0] < WIDTH//2 else -1
               change_y = 1 if corner_cords[1] < HEIGHT//2 else -1

               # Remove sharp corners
               square_eraser_cords = self.get_coords_from_center(corner_cords[0], corner_cords[1], TABLE_CORNER_RADIUS*2, TABLE_CORNER_RADIUS*2)
               pygame.draw.rect(win, DARK_BROWN, (square_eraser_cords[0], square_eraser_cords[1], TABLE_CORNER_RADIUS*2, TABLE_CORNER_RADIUS*2))

               # Draw the smooth circles
               circle_center = (corner_cords[0] + (TABLE_CORNER_RADIUS*change_x), corner_cords[1] + (TABLE_CORNER_RADIUS*change_y))
               pygame.draw.circle(win, LIGHT_BROWN, circle_center, TABLE_CORNER_RADIUS)

     def draw_piece(self, win, pieces, index):
          for piece in pieces[index]:
               piece.draw(win)
          
     def draw_bowl_value(self, win, value, cords):
          # Try and get all the values in the middle
          change_y = 1 if cords[1] < HEIGHT//2 else -1
          bowl_value_text = VALUE_FONT.render(str(value), True, BLACK)

          text_cords = (cords[0] - (bowl_value_text.get_rect().width//2), 
          cords[1] + (BOWL_SIZE + BOWL_PADDING_Y//4)*change_y - bowl_value_text.get_rect().height//2)

          win.blit(bowl_value_text, text_cords)

     def draw_store_value(self, win, value, cords):
          store_value_text = VALUE_FONT.render(str(value), True, BLACK)
          text_cords = (cords[0] - (store_value_text.get_rect().width//2), cords[1] - BOWL_SIZE - BOWL_PADDING_Y//2)
          win.blit(store_value_text, text_cords)

     def get_coords_from_center(self, x, y, width, height):
          cordsx = x - (width//2)
          cordsy = y - (height//2)
          return cordsx, cordsy