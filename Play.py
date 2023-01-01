from Game import Game
from MancalaBoard import MancalaBoard
import math
import copy
class Play:
    #def __init__(self):


    def humanTurn(self,game):#va permettre à l’utilisateur de jouer son tour 
        print(game.state.possibleMoves(1))
        move = input("Selectionez parmis les choix :")
        curent_player = game.state.doMove(1, move)
        return curent_player
    def computerTurn(self,game,play,depth = 6 ):
        if len(game.state.possibleMoves(2)) > 0:
            #(game,1,4,-math.inf,math.inf))
            best_node = play.negaMaxAlphaBetaPruning(game,2, depth,-math.inf,math.inf)
            print('computer:',best_node[1])
            curent_player = game.state.doMove(2, best_node[1])
        return curent_player, game

    #def computerTurn(self):#va permettre à l’ordinateur de jouer son tour
    def negaMaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        # game is an instance of the Game class and player = COMPUTER (Max) or HUMAN (Min)
        if game.gameOver() or depth == 0:
            bestValue = game.evaluate()
            if player == 1:#human
                bestValue = -bestValue
            return bestValue, None

        bestValue = -float("inf")
        bestPit = None

        for pit in game.state.possibleMoves(player):
            childGame = copy.deepcopy(game)
            childGame.state.doMove(player, pit)
            if(player==1):
                player=2
            else: player=1
            value, _ = self.negaMaxAlphaBetaPruning(childGame, player, depth-1, -beta, -alpha)
            value = -value

            if value > bestValue:
                bestValue = value
                bestPit = pit

            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break
        #print(bestValue)
        #print(bestPit)
        return bestValue, bestPit
    
#Tests
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
#print(test.negaMaxAlphaBetaPruning(game,1,4,-math.inf,math.inf))
