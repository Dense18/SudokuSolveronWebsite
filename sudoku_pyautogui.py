import pyautogui as pg
import numpy as np
import time

from solver.SudokuSolver import SudokuSolver

def placeSolution(solved_board):
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

def obtainBoardfromInput():
    board = []
    i = 0

    while (len(board) < 9):
        row_list = list(input(f"Row Number {i + 1}: "))
        int_row_list = list(map(lambda x : int(x), row_list))

        if(len(x) != 9):
            print("Please enter a valid row value")
            continue
        board.append(int_row_list)
        i += 1
    return board
    
def main():
    board = obtainBoardfromInput()
    
    sudoku_solver = SudokuSolver(board)
    sudoku_solver.solve()
    time.sleep(2)
    
    # Website tested is on sudoku.com
    placeSolution(sudoku_solver.board)

if __name__ == "__main__":
    main()

    
