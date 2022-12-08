class MancalaBoard:
    def __init__(self):
        # les clés sont les indices des 12 fosses et 2 magasins, et les valeurs sont le nombre de graines qu’il y a à l’intérieur:
        self.board={"A":4, "B":4, "C":4, "D":4, "E":4, "F":4,
                    "G":4, "H":4, "I":4, "J":4, "K":4, "L":4,
                    1:0, 2:0}
        # les indices (les lettres) des fosses du joueur 1:
        self.fosses1=('A', 'B', 'C', 'D', 'E', 'F')
        # les indices (les lettres) des fosses du joueur 2:
        self.fosses2=('G', 'H', 'I', 'J', 'K', 'L')
        # la fosse opposée:
        self.fosse_op={'A':'G', 'B':'H', 'C':'I', 'D':'J', 'E':'K','F':'L','G':'A', 'H':'B', 'I':'C', 'J':'D','K':'E', 'L':'F'}
        # la fosse suivante  
        self.fosse_suiv={'A':'B', 'B':'C', 'C':'D', 'D':'E', 'E':'F', 'F':'1', '1':'L', 'L':'K', 'K':'J', 'J':'I', 'I':'H', 'H':'G','G':'2', '2':'A'}    

    def possibleMoves(self,Board):
        # cette fonction va retourner les indices des fosses du joueur qui contiennent des graines    
        PossibleMoves=[]
        for cle, valeur in Board.items():
            if(valeur !=0 and cle !=1 and cle !=2):
                PossibleMoves.append(cle)
                #print("l'élément de clé", cle, "vaut", valeur)

        return PossibleMoves    

# Tests 
#test= MancalaBoard()
#B={"A":0, "B":1, "C":4, "D":3, "E":4, "F":4,"G":4, "H":4, "I":4, "J":4, "K":4, "L":4,1:0, 2:0}
#print(test.possibleMoves(B))

