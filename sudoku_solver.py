import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from SudokuSolver import *
from Sudoku import *


##Website should be in WebSudoku.com
def solveInWebSudoku(solved_board, driver):
    for row_num in range(len(solved_board)):
        for col_num in range(len(solved_board[row_num])):
            string_id = f"f{row_num}{col_num}"
            solve_cell = driver.find_element(By.ID, string_id)
            solve_cell.send_keys(f"{solved_board[col_num][row_num]}")

    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()

def initializeBoardfromWebSudoku(driver):
    board = []

    for row_num in range(0,9):
        board.append([])
        for col_num in range(0,9):
            string_id = f"f{col_num}{row_num}"
            cell = driver.find_element(By.ID, string_id)
            cell_value = cell.get_attribute("value")
            if(cell_value !=  ""):
                board[row_num].append(int(cell_value))
            else:
                board[row_num].append(0)
    
    return board

def main(argv):
    counter_limit = 0
    counter = 0

    if (len(argv) == 1):
        counter_limit = 1

    if (len(argv) >= 2):
        counter_limit = int(argv[1])

    url = "https://nine.websudoku.com/?level=2"
    # url = "https://www.websudoku.com/?level=2"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    # driver.switch_to.frame(0)

    while counter < counter_limit:
        #driver.switch_to.parent_frame()
        #driver.switch_to.frame(0)

        time.sleep(2)
        board = initializeBoardfromWebSudoku(driver)
        pre_sudoku_solver = SudokuSolver(board)
        pre_sudoku_solver.solve()

        sudoku = Sudoku(pre_sudoku_solver.board)
        sudoku.solve()

        solveInWebSudoku(sudoku.board, driver)

        try:
            new_game_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "newgame"))
            )

            new_game_button.click()
            counter += 1
            #time.sleep(2)

        except:
            print("Error")
            break;
    
    driver.quit()
    return


if __name__ == "__main__":
    main(sys.argv)

