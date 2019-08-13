# Based on Minimax Algorithm
# In this version, always Computer play the first move

class Play():
    count =0
    def __init__(self):
        self.board = [["#" for i in range(3)] for j in range(3)]
    
    def isFinished(self,val):
        for row in self.board:
            if(row==[val,val,val]):
                return True

        def checkColumn(i,val):
            col = [self.board[j][i] for j in range(3)]
            if(col==[val,val,val]):
                return True
            return False
        
        def checkDiagonal(val):
            diag1 = [self.board[0][0],self.board[1][1],self.board[2][2]]
            diag2 = [self.board[0][2],self.board[1][1],self.board[2][0]]

            if(diag1==[val,val,val] or diag2 ==[val,val,val]):
                return True
            return False
        if(checkColumn(0,val) or checkDiagonal(1,val) or checkColumn(2,val)):
            return True
        if(checkDiagonal(val)):
            return True
        return False

    def getBest(self,iteration):

        team = {0:"X",1:"O"}

        computer_win = self.isFinished("X")
        human_win    = self.isFinished("#")

        if(human_win):
            return -1
        if(computer_win):
            return 1
        if((not human_win) and (not computer_win)):
            return 0

        score = self.isFinished()
        if(score in [1,-1]):
            return score
        elif(score ==0):
            return 0

        store =[]

        for place in range(9):
            row = place//3
            column = place%3
            move_info = {"x":row,"y":column,"score":0}
            if(board[row[column]=="#"]):
                
                board[row][column] = team[palyer%2]

                move_info["score"] = self.getBest(iteration+1)
                board[row][column] = "#"
            store.append(move_info)

        best_score = -1000
        best_move =0
        if (iteration%2==0):
            for item in store:
                if(item["score"]>best_score):
                    best_score = item["score"]
                    best_move = item
            return best_move
        else:
            best_score =1000
            for item in store:
                if(item["score"]<best_score):
                    best_score = item["score"]
                    best_move =item
            return best_move
    
    def Move(self,iteration):

        team = {0:"X",1:"O"}
        if(iteration%2==0):
            getMove =getBest(iteration)
            self.board[getMove["x"]][getMove["y"]] = team[iteration%2]
        else:
            place = int(input("Enter the move: "))
            self.board[palce//3][place%3] = team[1]
    
    def showBoard(self):
        for row in self.board:
            for element in row:
                print(element,end =" ")
            print()
    
    

    