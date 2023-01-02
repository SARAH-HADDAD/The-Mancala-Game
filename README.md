# Mancala

This is a simple implementation of the ancient African board game called Mancala in Python, using Pygame for the GUI.
The game can be played by one human player against the computer.

## Files
### MancalaBoard.py: 
Contains the MancalaBoard class which is responsible for representing the game board and performing moves.
### Game.py:
Contains the Game class which is responsible for managing the game flow and determining the winner.
### Play.py:
Contains the Play class which is responsible for managing the interactions with the human player.
### GUI.py:
Contains the Drawer class which is responsible for rendering the game board to the screen.
### main.py: 
Is the entry point of the program and contains the game loop.

## How to play
To play the game, run main.py. The human player will play first and can choose any of their non-empty pits by clicking on it. The computer player will then make its move. The game ends when one player has no more stones on their side of the board. The player with the most stones in their store wins.

## Requirements
This code requires Pygame to run. To install Pygame, run pip install pygame.
