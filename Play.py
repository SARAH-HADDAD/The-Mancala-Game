from Game import Game
from MancalaBoard import MancalaBoard
import math
import copy
import random
from copy import deepcopy
import pygame
def getFosseFromPos(pos):
    # Convert the mouse position to a fosse index (A, B, C, etc.)
    fosse_index = None
    # Check if the mouse position is within the bounds of a fosse
    if (335 -55 <= pos[0] <= 335+55) and (500-55 <= pos[1] <= 500+55):
        fosse_index = "A"
    elif (460 -55 <= pos[0] <= 460 +55) and (500-55 <= pos[1] <= 500+55):
        fosse_index = "B"
    elif (585 -55 <= pos[0] <= 585 +55) and (500-55 <= pos[1] <= 500+55):
        fosse_index = "C"
    elif (710 -55 <= pos[0] <= 710 +55) and (500-55 <= pos[1] <= 500+55):
        fosse_index = "D"
    elif (835 -55 <= pos[0] <= 835 +55) and (500-55 <= pos[1] <= 500+55):
        fosse_index = "E"
    elif (960 -55 <= pos[0] <= 960 +55) and (500-55 <= pos[1] <= 500+55):
        fosse_index = "F"
    return fosse_index
class Play:
    # def __init__(self):

    def humanTurn(self, game):
        # Initialize a flag to track whether a valid move has been made
        move_made = False
        # Run the loop until a valid move is made
        while not move_made:
            # Listen for user input
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position of the mouse click
                    pos = pygame.mouse.get_pos()
                    # Convert the mouse position to a fosse index (A, B, C, etc.)
                    fosse = getFosseFromPos(pos)
                    # If the fosse is a valid move, make the move and set the flag to True
                    if fosse in game.state.possibleMoves(1):
                        curent_player = game.state.doMove(1, fosse)
                        move_made = True
                        break
            # Pause the game loop for a short time to allow the computer to process events
            pygame.time.delay(50)
        # Return the current player
        return curent_player

    def computerTurn(self, game, play, depth=8):
        if len(game.state.possibleMoves(2)) > 0:
            best_node = play.minmaxAlphaBetaPruning(
                game, 2, depth, -math.inf, math.inf)
            print('computer:', best_node[1])
            curent_player = game.state.doMove(2, best_node[1])
        return curent_player, game

    # def computerTurn(self):#va permettre à l’ordinateur de jouer son tour
    def negamaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        if depth == 0 or game.gameOver():
            return game.evaluate(), None

        best_value = -math.inf
        best_move = None
        for move in game.state.possibleMoves(player):
            new_game = deepcopy(game)
            current_player = new_game.state.doMove(player, move)
            if current_player == player:  # player gets an extra turn
                value, _ = self.negamaxAlphaBetaPruning(new_game, player, depth, alpha, beta)
            else:
                value, _ = self.negamaxAlphaBetaPruning(new_game, 3 - player, depth - 1, -beta, -alpha)
            value = -value
            if value > best_value:
                best_value = value
                best_move = move
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        return best_value, best_move


    def minmaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        if depth == 0 or game.gameOver():
            return game.evaluate(), None

        if player == 1:
            best_value = -math.inf
            best_move = None
            for move in game.state.possibleMoves(player):
                new_game = deepcopy(game)
                new_game.state.doMove(player, move)
                value, _ = self.minmaxAlphaBetaPruning(new_game, 2, depth - 1, alpha, beta)
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    break
            return best_value, best_move
        else:
            best_value = math.inf
            best_move = None
            for move in game.state.possibleMoves(player):
                new_game = deepcopy(game)
                new_game.state.doMove(player, move)
                value, _ = self.minmaxAlphaBetaPruning(new_game, 1, depth - 1, alpha, beta)
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if alpha >= beta:
                    break
            return best_value, best_move

