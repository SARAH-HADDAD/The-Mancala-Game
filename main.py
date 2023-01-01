
import pygame
from GUI import Drawer
from Play import Play
from Game import Game

draw = Drawer()
# Run the game loop
running = True
print("game class")
test=Play()
game=Game(1)
player=1
while(not game.gameOver()):
    if(player==1):
        print()
        player=test.humanTurn(game)
        print()
    else:
        print()
        player,game=test.computerTurn(game,test)
        print()
    print(game.state.board)
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            running = False
print(game.findWinner())
pygame.quit()
