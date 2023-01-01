
import pygame
from GUI import Drawer
draw = Drawer()
# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
