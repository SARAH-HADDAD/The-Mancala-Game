from MancalaBoard import MancalaBoard


class Game:
    def __init__(self, player):
        # représenter l’état (c’est-à-dire une instance de la classe MancalaBoard)
        self.state = MancalaBoard()
        # le numéro du joueur choisi par l’utilisateur (player1 ou player2)
        self.playerSide = player

    def gameOver(self):  # va vérifier si la partie est finie
        # toutes les fosses de l’un des joueurs sont vides
        gameOver1 = True
        gameOver2 = True
        for fosse in self.state.fosses1:
            if self.state.board[fosse] != 0:
                gameOver1 = False
                break
        for fosse in self.state.fosses2:
            if self.state.board[fosse] != 0:
                gameOver2 = False
                break
        if (gameOver1 == False and gameOver2 == False):
            return False
        # Lorsque le joueur 1 n’a plus de graines dans toutes ses fosses, la partie se termine
        # le joueur 2peut prendre toutes les graines restantes et les placer dans son  magasin
        if (gameOver1):
            for fosse in self.state.fosses2:
                self.state.board[2] += self.state.board[fosse]
                self.state.board[fosse] = 0
            return True
        if (gameOver2):
            for fosse in self.state.fosses1:
                self.state.board[1] += self.state.board[fosse]
                self.state.board[fosse] = 0
            return True

    def findWinner(self):  # va retourner le gagnant de la partie, ainsi que son score
        print("mabrouk 3lik el ka2s")
        if (self.state.board[1] > self.state.board[2]):
            return 1, self.state.board[1]
        else:
            return 2, self.state.board[2]

    def evaluate(self):  # va estimer le gain
        return (self.state.board[1] - self.state.board[2])
