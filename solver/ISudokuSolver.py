from abc import ABC, abstractmethod

class ISudokuSolver(ABC):
    """
    Interface for Sudoku Solver
    """
    @abstractmethod
    def solve(self):
        raise NotImplementedError