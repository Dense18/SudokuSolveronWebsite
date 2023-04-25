from SudokuSolver import *
import time
from Sudoku import *
import numpy as np

def possible(grid, x, y, n):
    for i in range(0, 9):
        if grid[i][x] == n and i != y: # Checks for number (n) in X columns
            return False

    for i in range(0, 9):
        if grid[y][i] == n and i != x: # Checks for number (n) in X columns
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  # Checks for numbers in box(no matter the position, it finds the corner)
            if grid[Y][X] == n:
                return False    
    return True

def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid,x, y, n):
                        grid[y][x] = n
                        if (solve(grid)):
                            return True
                        grid[y][x] = 0
                return False
    return True


board = [[ 3, 0, 6, 5, 0, 8, 4, 0, 0],
[ 5, 2, 0, 0, 0, 0, 0, 0, 0],
[ 0, 8, 7, 0, 0, 0, 0, 3, 1],
[ 0, 0, 3, 0, 1, 0, 0, 8, 0],
[ 9, 0, 0, 8, 6, 3, 0, 0, 5],
[ 0, 5, 0, 0, 9, 0, 6, 0, 0],
[ 1, 3, 0, 0, 0, 0, 2, 5, 0],
[ 0, 0, 0, 0, 0, 0, 0, 7, 4],
[ 0, 0, 5, 2, 0, 6, 3, 0, 0]]

solve(board)
print(board)

board = [[ 3, 0, 6, 5, 0, 8, 4, 0, 0],
[ 5, 2, 0, 0, 0, 0, 0, 0, 0],
[ 0, 8, 7, 0, 0, 0, 0, 3, 1],
[ 0, 0, 3, 0, 1, 0, 0, 8, 0],
[ 9, 0, 0, 8, 6, 3, 0, 0, 5],
[ 0, 5, 0, 0, 9, 0, 6, 0, 0],
[ 1, 3, 0, 0, 0, 0, 2, 5, 0],
[ 0, 0, 0, 0, 0, 0, 0, 7, 4],
[ 0, 0, 5, 2, 0, 6, 3, 0, 0]]

pre_solver = SudokuSolver(board)
pre_solver.solve()

solver = Sudoku(pre_solver.getBoard())
start_time2 = time.time()
solver.solve()
print(time.time() - start_time2)
solver.show()
