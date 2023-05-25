import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from solver.SudokuSolver import SudokuSolver


def placeSolution(solved_board: list[list[int]], driver: webdriver):
    for row_num in range(len(solved_board)):
        for col_num in range(len(solved_board[row_num])):
            string_id = f"f{row_num}{col_num}"
            solve_cell = driver.find_element(By.ID, string_id)
            solve_cell.send_keys(f"{solved_board[col_num][row_num]}")

    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()

def initializeBoardfromWebSudoku(driver) -> list[list[int]]:
    board = []

    for row_num in range(9):
        board.append([])
        for col_num in range(9):
            string_id = f"f{col_num}{row_num}"
            cell = driver.find_element(By.ID, string_id)
            cell_value = cell.get_attribute("value")
            if(cell_value !=  ""):
                board[row_num].append(int(cell_value))
            else:
                board[row_num].append(0)
    
    return board

def getNewPuzzle(driver):
    try:
        new_game_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "newgame"))
        )
        new_game_button.click()
    except Exception as e:
        raise e
    
def main(argv):
    current_puzzle_number = 0 
    num_puzzle_to_solve = 1 if len(argv) == 1 else int(argv[1])

    url = "https://nine.websudoku.com/?level=2"
    # url = "https://www.websudoku.com/?level=2"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    # driver.switch_to.frame(0)

    while current_puzzle_number < num_puzzle_to_solve:
        #driver.switch_to.parent_frame()
        #driver.switch_to.frame(0)
        time.sleep(2)
        
        board = initializeBoardfromWebSudoku(driver)
        sudoku_solver = SudokuSolver(board)
        sudoku_solver.solve()
        placeSolution(sudoku_solver.board, driver)

        
        try:
            getNewPuzzle(driver)
            current_puzzle_number += 1
        except Exception as e:
            print(e)
            break
    
    driver.quit()

if __name__ == "__main__":
    main(sys.argv)

