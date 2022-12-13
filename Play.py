from Game import Game
from MancalaBoard import MancalaBoard
import math
import copy
class Play:
    #def __init__(self):


    #def humanTurn(self):#va permettre à l’utilisateur de jouer son tour 


    #def computerTurn(self):#va permettre à l’ordinateur de jouer son tour


    def negaMaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        # game est une instance de la classe Game et player = COMPUTER(Max) ou HUMAN(Min)
        if (game.gameOver() or depth == 1):
            bestValue = game.evaluate()
            bestPit = None
            if player == 1:
                bestValue = - bestValue

            return bestValue, bestPit
        
        bestValue = -math.inf
        bestPit = None
        
        for pit in game.state.possibleMoves():
            child_game = copy.deepcopy(game)
            child_game.state.doMove(game.playerSide, pit)
            value,pit = self.negaMaxAlphaBetaPruning(child_game, -player, depth-1, -beta, -alpha)
            value = - value
            if (value > bestValue):
                bestValue = value
                bestPit =pit
            if (bestValue > alpha):
                alpha = bestValue
            if (beta <= alpha):
                break
        return bestValue, bestPit    

    
#Tests
test=Play()
game=Game(1)
print(test.negaMaxAlphaBetaPruning(game,1,2,-math.inf,math.inf))
