class MancalaBoard:
    def __init__(self):
        # les clés sont les indices des 12 fosses et 2 magasins, et les valeurs sont le nombre de graines qu’il y a à l’intérieur:
        self.board={"A":4, "B":4, "C":4, "D":4, "E":4, "F":4,
                    "G":4, "H":4, "I":4, "J":4, "K":4, "L":4,
                    1:0, 2:0}
        # les indices (les lettres) des fosses du joueur 1:
        self.fosses1=("A", "B", "C", "D", "E", "F")
        # les indices (les lettres) des fosses du joueur 2:
        self.fosses2=("G", "H", "I", "J", "K", "L")
        # la fosse opposée:
        self.opposite={"A":"G", "B":"H", "C":"I", "D":"J", "E":"K","F":"L","G":"A", "H":"B", "I":"C", "J":"D","K":"E", "L":"F"}
        # la fosse suivante  
        self.next={"A":"B", "B":"C", "C":"D", "D":"E", "E":"F", "F":1, 1:"L", "L":"K", "K":"J", "J":"I", "I":"H", "H":"G","G":2, 2:"A"}    

    def possibleMoves(self,Board):
        # cette fonction va retourner les indices des fosses du joueur qui contiennent des graines:    
        PossibleMoves=[]
        for cle, valeur in Board.items():
            if(valeur !=0 and cle !=1 and cle !=2):
                PossibleMoves.append(cle)
                #print("l"élément de clé", cle, "vaut", valeur)

        return PossibleMoves    
    def doMove(self, player, position):
        # cette fonction va exécuter un mouvement, et retourner le numéro du joueur qui va jouer le prochain tour:

        #choisit une fosse de son côté du plateau et ramasse toutes ses graines
        graines=self.board[position]
        self.board[position]=0
        #Dans le sens inverse des aiguilles d’une montre, le joueur dépose une pierre dans chaque
        #fosse jusqu’à ce qu’ils n’aient plus de graines dans sa main
        while graines > 0:
            position = self.next[position]
            self.board[position]+=1
            graines=graines-1
        # Si la dernière graine déposée atterrit dans le magasin du joueur, ce joueur peut jouer un tour supplémentaire 
        if(position == player):
            return player
        #Si la dernière graine déposée atterrit dans une fosse vide du côté du joueur, cette graine
        #et toutes les graines dans la fosse du côté opposé (c’est-à-dire une fosse de l’adversaire)
        #vont à ce joueur, et sont placées dans son magasin
        if(self.board[position]==1):
            self.board[position]=0
            if(player==1):
                player_fosses=self.fosses1
                opposite=self.fosses2
            else:
                player_fosses=self.fosses2
                opposite=self.fosses1
            oppositePosition=-1    
            for i in range(len(player_fosses)): 
                if(position==player_fosses[i]):
                    oppositePosition=opposite[i] 
            if(oppositePosition!=-1):        
                self.board[player]+=self.board[oppositePosition]          
                self.board[oppositePosition] = 0
        if(player==1):
            return 2
        else:
            return 1    

# Tests 
test= MancalaBoard()
#print(test.doMove(1,"F"))
#print(test.board)
#B={"A":0, "B":1, "C":4, "D":3, "E":4, "F":0,"G":4, "H":4, "I":4, "J":4, "K":4, "L":4,1:0, 2:0}
#print(test.possibleMoves(B))
