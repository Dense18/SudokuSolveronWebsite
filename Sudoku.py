class Sudoku:
    def __init__(self, board):
        self.board = board
    
    def getEmptyPosition(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if (self.board[row][col] == 0):
                    return (row, col)
        return None
    
    def isValid(self, num, pos):
         #Check for rows
        for i in range(len(self.board[0])):
            if (self.board[pos[0]][i] == num):
                return False
            
        #Check for cols
        for i in range(len(self.board)):
            if (self.board[i][pos[1]] == num):
                return False
        
        ##Check for squares 
        group_row = pos[0] // 3
        group_col = pos[1] // 3
        
        for row in range(group_row * 3,(group_row * 3) + 3):
            for col in range(group_col * 3,(group_col * 3) + 3):
                if (self.board[row][col] == num):
                    return False
        
        return True

    def solve(self):
        pos = self.getEmptyPosition()
        if (pos == None):
            return True
        else:
            row, col = pos
        
        for num in range(1,10):
            if self.isValid(num, pos):
                self.board[row][col] = num
                
                if self.solve():
                    return True
                
                self.board[row][col] = 0
        
        return False
    
    #Print the board in a clear format
    def show(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

    def getBoard(self):
        return self.board