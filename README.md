# Sudoku Solver on Website
Automated solving sudoku puzzles on a website using selenium and pyautogui, with a custom solver. Tested on Windows

## Required installation
```python
pip install pyautogui
pip install selenium
pip install webdriver-manager
```
## Running the Program
```python
py sudoku_solver.py x # Using selenium. x is an integer indicating the number of puzzles to solve, the default value is 1 if it is not specified.
py sudoku_pyautogui.py # Using pyautogui. This file is only used for me in learning how to use pyautogui, not recommended for automation usage. 
```
# Application usage

## sudoku_solver.py
After running the program, a new google chrome browser instance will be created, directing to a specific sudoku website

<img src = "examples/loading.png" width = 700 height = 300>

Once the page has been fully loaded, the program scraps the initial sudoku puzzle state from the website and attempts to find the solution using the custom solver.

<img src = "examples/loaded.png" width = 700 height = 500>

The program will then apply the solution to the sudoku website

<img src = "examples/solved_board_selenium.png" width = 700 height = 300>
<img src = "examples/correct_solution_selenium.png" width = 700 height = 300>

The program will be directed to a new puzzle by pressing the "Bring me a new puzzle!" button based on the remaining number of puzzles to solve

## sudoku_pyautogui.py

Initially, the user will be asked to manually enter the current board state onto the terminal based on the website. 


| Initial board state | Terminal Input|
| --------------- | --------------- |
| <img src = "examples/initial_board_pyautogui.png" width = 300 height = 300> | <img src = "examples/input_terminal_pyautogui.png" width = 300 height = 300>|

After entering the required fields, the program will attemp to find the solution using the custom solver

There will then be a delay of 2 seconds, allowing the user to move the mouse and click on the top left cell of the sudoku board. 

<img src = "examples/top_left_cell_pyautogui.png" width = 300 height = 300>

After two seconds have passed, the program will simulate key and mouse presses to apply the solution onto the sudoku board.

<img src = "examples/solved_board_pyautogui.png" width = 300 height = 300>


---
# Additional information
The website that is used for the sudoku puzzles is https://nine.websudoku.com/
