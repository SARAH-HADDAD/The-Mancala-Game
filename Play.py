from Game import Game
from MancalaBoard import MancalaBoard
import math
import copy
class Play:
    #def __init__(self):


    #def humanTurn(self):#va permettre à l’utilisateur de jouer son tour 


    #def computerTurn(self):#va permettre à l’ordinateur de jouer son tour
    def negaMaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        # game is an instance of the Game class and player = COMPUTER (Max) or HUMAN (Min)
        if game.gameOver() or depth == 0:
            bestValue = game.evaluate()
            if player == 1:
                bestValue = -bestValue
            return bestValue, None

        bestValue = -float("inf")
        bestPit = None

        for pit in game.state.possibleMoves(str(player)):
            childGame = copy.deepcopy(game)
            childGame.state.doMove(player, pit)
            value, _ = self.negaMaxAlphaBetaPruning(childGame, -player, depth-1, -beta, -alpha)
            value = -value

            if value > bestValue:
                bestValue = value
                bestPit = pit

            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break

        return bestValue, bestPit
    
#Tests
print("game class")
test=Play()
game=Game(1)
print(test.negaMaxAlphaBetaPruning(game,1,4,-math.inf,math.inf))
