from solver.SudokuPreSolver import SudokuPreSolver
from solver.SudokuBacktrack import SudokuBacktrack

class SudokuSolver:
    """
        Sudoku Solver class using backtracking and a custom pre-solver
    """
    def __init__(self, board):
        self.board = board
    
    def solve(self):
        pre_sudoku_solver = SudokuPreSolver(self.board)
        pre_sudoku_solver.solve()

        sudoku_backtrack = SudokuBacktrack(pre_sudoku_solver.board)
        sudoku_backtrack.solve()

        




    
    
    





