# Sudoku Solver

This is a simple Python program that solves a 9x9 Sudoku puzzle using the backtracking algorithm.

## Features
- Uses a **backtracking algorithm** to find a valid solution.
- Efficiently checks rows, columns, and 3x3 subgrids for validity.
- Displays the board before and after solving.

## Requirements
- Python 3.x

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/sudoku-solver.git
   cd sudoku-solver
   ```
2. Run the script:
   ```sh
   python sudoku_solver.py
   ```

## Code Overview
- `solve(board)`: Recursively solves the Sudoku puzzle.
- `valid(board, num, pos)`: Checks if a number can be placed at a given position.
- `find_empty(board)`: Finds the next empty cell (0) in the board.
- `print_board(board)`: Displays the Sudoku board in a readable format.

## Example Output
```
7 8 . | 4 . . | 1 2 .
6 . . | . 7 5 | . . 9
. . . | 6 . 1 | . 7 8
---------------------
. . 7 | . 4 . | 2 6 .
. . 1 | . 5 . | 9 3 .
9 . 4 | . 6 . | . . 5
---------------------
. 7 . | 3 . . | . 1 2
1 2 . | . . 7 | 4 . .
. 4 9 | 2 . 6 | . . 7

Solved Sudoku:

7 8 5 | 4 3 9 | 1 2 6
6 1 2 | 8 7 5 | 3 4 9
4 9 3 | 6 2 1 | 5 7 8
---------------------
8 5 7 | 9 4 3 | 2 6 1
2 6 1 | 7 5 8 | 9 3 4
9 3 4 | 1 6 2 | 7 8 5
---------------------
5 7 8 | 3 9 4 | 6 1 2
1 2 6 | 5 8 7 | 4 9 3
3 4 9 | 2 1 6 | 8 5 7
```





