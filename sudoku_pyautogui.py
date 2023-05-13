import pyautogui as pg
import numpy as np
import time

from SudokuSolver import *
from Sudoku import *

def placeSolution(solved_board):
    ## Flatten 2d array to 1d array
    solution = np.ravel(solved_board)

    counter = 0
    for i, num in enumerate(solution):
        pg.press(str(num))
        counter += 1

        if(counter % 9!= 0):
            pg.hotkey("right")
        else:
            pg.hotkey("down")
            for i in range(8):
                pg.hotkey("left")

def main():
    board = []
    i = 0

    while (len(board) < 9):
        ls = list(input(f"Row Number {i + 1}: "))
        x = list(map (lambda x : int(x), ls))

        if(len(x) != 9):
            continue
        board.append(x)
        i += 1
    
    print(board)

    pre_sudoku_solver = SudokuSolver(board)
    pre_sudoku_solver.solve()

    solver = Sudoku(pre_sudoku_solver.getBoard())
    solver.solve()

    time.sleep(2)
    # Website tested is on sudoku.com
    placeSolution(solver.getBoard())
    solver.show()

if __name__ == "__main__":
    main()

    
