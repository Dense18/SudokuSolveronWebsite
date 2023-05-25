class Cell:
    """
        Class storing information on each cell of the Sudoku
    """
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.box = (row // 3 * 3)  + (col // 3)
        self.value = value
        self.options = self.initializeOptions()
    
    def initializeOptions(self):
        return [] if self.value != 0 else [*range(1, 10)]


