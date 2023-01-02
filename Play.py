from Game import Game
from MancalaBoard import MancalaBoard
import math
import copy
import random
from copy import deepcopy



class Play:
    # def __init__(self):

    def humanTurn(self, game):  # va permettre à l’utilisateur de jouer son tour
        move = random.choice(game.state.possibleMoves(1))
        curent_player = game.state.doMove(1, move)
        return curent_player

    def computerTurn(self, game, play, depth=8):
        if len(game.state.possibleMoves(2)) > 0:
            best_node = play.minmaxAlphaBetaPruning(
                game, 2, depth, -math.inf, math.inf)
            print('computer:', best_node[1])
            curent_player = game.state.doMove(2, best_node[1])
        return curent_player, game

    # def computerTurn(self):#va permettre à l’ordinateur de jouer son tour
    def negaMaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        # game is an instance of the Game class and player = COMPUTER (Max) or HUMAN (Min)
        if game.gameOver() or depth == 0:
            bestValue = game.evaluate()
            if player == 1:  # human
                bestValue = -bestValue
            return bestValue, None

        bestValue = -float("inf")
        bestPit = None

        for pit in game.state.possibleMoves(player):
            childGame = copy.deepcopy(game)
            curent_player = childGame.state.doMove(player, pit)
            if curent_player == 1:
                value, _ = self.negaMaxAlphaBetaPruning(
                childGame, curent_player, depth-1, -beta, -alpha)
            else:
                value, _ = self.negaMaxAlphaBetaPruning(
                childGame, curent_player, depth-1, beta, alpha)                
            value = -value

            if value > bestValue:
                bestValue = value
                bestPit = pit

            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break
        # print(bestValue)
        # print(bestPit)
        return bestValue, bestPit

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



# Tests
"""
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
print(game.findWinner())
"""
# print(test.negaMaxAlphaBetaPruning(game,1,4,-math.inf,math.inf))
