from Game import Game
from MancalaBoard import MancalaBoard
import math
import copy
import random
from copy import deepcopy
import pygame

class Play:
    # def __init__(self):

    def humanTurn(self, game):
    # Listen for user input
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # Get the position of the mouse click
                pos = pygame.mouse.get_pos()
                # Convert the mouse position to a fosse index (A, B, C, etc.)
                fosse = self.getFosseFromPos(pos)
                # If the fosse is a valid move, make the move and return the current player
                if fosse in game.state.possibleMoves(1):
                    curent_player = game.state.doMove(1, fosse)
                    return curent_player
        # If no valid move was made, return the same player
        return 1


    def computerTurn(self, game, play, depth=8):
        if len(game.state.possibleMoves(2)) > 0:
            best_node = play.negamaxAlphaBetaPruning(
                game, 2, depth, -math.inf, math.inf)
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

