class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.box = (row // 3 * 3)  + (col // 3)
        self.value = value
        self.options = self.initializeOptions()
    
    def getOptions(self):
        return self.options
    
    def initializeOptions(self):
        if self.value != 0:
            return []
        else:
            return [*range(1,10)]

