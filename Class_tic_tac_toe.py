
class TicTacToe():
    count = 0
    def __init__(self,n=3,biased= False):
        self.board = [["#" for j in range(n)] for i in range(n)] # creating nxn board
        self.horizontal =[[0 for i in range(n)] for j in range(2)]
        self.vertical =  [[0 for i in range(n)] for j in range(2)]
        self.diagonal =  [[0,0],[0,0]]
        self.n =n

    def showBoard(self):
        for row in self.board:
            for element in row:
                print(element,end =" ")
            print()
    
    def isFinished(self,recent_pos):
        iteration = TicTacToe.count
        row = recent_pos//self.n
        column = recent_pos%self.n

        if(iteration<=self.n): # Can't win in <=4 steps
            return False
        elif(self.vertical[iteration%2][column]==self.n or self.horizontal[iteration%2][row]==self.n or self.diagonal[iteration%2][0]==self.n or self.diagonal[iteration%2][1]==self.n):
            return True
        return False
        
    
    def Move(self):
        def update(recent_pos):
            row = recent_pos//self.n
            column = recent_pos%self.n
            hashmap ={1:"X",2:"0"}
            iteration = TicTacToe.count

            self.board[row][column] =hashmap[(iteration%2) +1]

            self.vertical[iteration%2][column]+=1
            self.horizontal[iteration%2][row]+=1
            
            diag1_set = set([self.n*i+i for i in range(self.n)])
            diag_set2 = set([self.n*i-i for i in range(self.n)])

            if(recent_pos in diag1_set):
                self.diagonal[iteration%2][0]+=1

            if(recent_pos in diag_set2):
                self.diagonal[iteration%2][1]+=1

        print("Enter the input from 0 to n*n-1")
        for iteration in range(self.n*self.n):
            self.showBoard()
            recent_pos = int(input("Hey player no. {} it's your turn enter your move: ".format(iteration%2+1)))
            update(recent_pos)
            if(self.isFinished(recent_pos)):
                print("Congrats player {} ,you won".format((iteration%2)+1))
                break
            elif(iteration==(self.n*self.n)-1):
                print("Game End in Draw! ")

            

            TicTacToe.count +=1
if __name__ == "__main__":

    size_of_board = int(input("Enter the size of the square board: "))
    game = TicTacToe(size_of_board)
    game.Move()