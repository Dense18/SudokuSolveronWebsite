from model.Cell import *
from solver.ISudokuSolver import ISudokuSolver

class SudokuPreSolver(ISudokuSolver):
    """
    Sudoku solver class using custom rules and patterns. Note: Some cells may still be empty after using this solver.
    """
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.cells = [Cell(row_no, col_no, col) for row_no, row in enumerate(board) for col_no, col in enumerate(row)]
        self.initializeOptions()

    def getCellsFromRow(self, row_no: int) -> list[Cell]:
        return [cell for cell in self.cells if cell.row == row_no]
    
    def getCellsFromCol(self, col_no: int) -> list[Cell]:
        return [cell for cell in self.cells if cell.col == col_no]
    
    def getCellsFromBox(self, box_no: int) -> list[Cell]:
        return [cell for cell in self.cells if cell.box == box_no]
    
    def getCellsFromCell(self, cell_arg: Cell) -> list[Cell]:
        return [cell for cell in self.cells if cell.row == cell_arg.row or 
                                               cell.col == cell_arg.col or 
                                               cell.box == cell_arg.box]
    def initializeOptions(self):
        for cell in self.cells:
            self.updateOptions(cell)
    
    def updateOptions(self, cell_arg: Cell):
        for cell in self.getCellsFromCell(cell_arg):
            try:
                cell.options.remove(cell_arg.value)
            except:
                continue

    def placeValue(self, cell: Cell, value: int):
        cell.value = value
        self.board[cell.row][cell.col] = value

        cell.options = []
        self.updateOptions(cell)

    def checkUniqueOption(self) -> bool:
        for cell in self.cells:
            if len(cell.options) == 1:
                self.placeValue(cell, cell.options[0])
                return True
        return False
    
    def checkUniqueValue(self) -> bool:
        for num in range(9):
            if self.checkUniqueValueGroup(self.getCellsFromRow(num)):
                return True
            if self.checkUniqueValueGroup(self.getCellsFromCol(num)):
                return True
            if self.checkUniqueValueGroup(self.getCellsFromBox(num)):
                return True
        return False
    
    def checkUniqueValueGroup(self, cell_group: list[Cell]) -> bool: 
        counts = [0] * 10
        
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
    

    def __str__(self) -> str:
        output = ""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                output += "- - - - - - - - - - - - - \n"

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    # print("| ", end="")
                    output += "| "

                if j == 8:
                    output += f"{self.board[i][j]}\n"
                else:
                    output += f"{self.board[i][j]} "
        return output


    
    
    





