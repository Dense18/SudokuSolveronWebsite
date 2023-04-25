from Cell import *

class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.cells = []
        for row_no, row in enumerate(board):
            for col_no, col in enumerate(row):
                self.cells.append(Cell(row_no, col_no, col))
        
        self.initializeOptions()

    def getCellsFromRow(self, row_no):
        return [cell for cell in self.cells if cell.row == row_no]
    
    def getCellsFromCol(self, col_no):
        return [cell for cell in self.cells if cell.col == col_no]
    
    def getCellsFromBox(self, box_no):
        return [cell for cell in self.cells if cell.box == box_no]
    
    def getCellsFromCell(self, cell_arg):
        return [cell for cell in self.cells if cell.row == cell_arg.row or 
                                               cell.col == cell_arg.col or 
                                               cell.box == cell_arg.box]
    def initializeOptions(self):
        for cell in self.cells:
            self.updateOptions(cell)
    
    def updateOptions(self, cell_arg):
        for cell in self.getCellsFromCell(cell_arg):
            try:
                cell.options.remove(cell_arg.value)
            except:
                continue

    def placeValue(self, cell, value):
        cell.value = value
        self.board[cell.row][cell.col] = value

        cell.options = []
        self.updateOptions(cell)

    def checkUniqueOption(self):
        for cell in self.cells:
            if len(cell.options) == 1:
                self.placeValue(cell, cell.options[0])
                return True
        return False
    
    def checkUniqueValue(self):
        for num in range(9):
            if self.checkUniqueValueGroup(self.getCellsFromRow(num)):
                return True
            if self.checkUniqueValueGroup(self.getCellsFromCol(num)):
                return True
            if self.checkUniqueValueGroup(self.getCellsFromBox(num)):
                return True
        return False
    
    def checkUniqueValueGroup(self, cell_group): 
        counts = [0] * 10
        
        ##Try adding a hasp map here
        for cell in cell_group:
            for option in cell.options:
                counts[option] += 1
        
        if 1 in counts:
            unique_val = counts.index(1)
            for cell in cell_group:
                if unique_val in cell.options:
                    self.placeValue(cell, unique_val)
                    return True
        return False
    
    def solve(self):
        while (True):
            if not self.checkUniqueOption():
                if not self.checkUniqueValue():
                    break
    
    def print(self):
        last_cell_row_no = 0
        for cell in self.cells:
            if last_cell_row_no != cell.row:
                print()
            print(cell.value, end = " ")
            last_cell_row_no = cell.row
        print("\n- - - - - - - - -")

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
            


    
    
    





