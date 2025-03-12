board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True  # No empty spots, puzzle solved
    row, col = find

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num  # Place number

            if solve(bo):  # Recursively solve
                return True

            bo[row][col] = 0  # Undo move (backtrack)

    return False

def valid(bo, num, pos):
    row, col = pos

    # Check row
    if num in bo[row]:
        return False

    # Check column
    if num in [bo[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_x = col // 3 * 3
    box_y = row // 3 * 3
    for i in range(3):
        for j in range(3):
            if bo[box_y + i][box_x + j] == num:
                return False

    return True

def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            print(bo[i][j] if bo[i][j] != 0 else ".", end=" ")
        print()

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)  # Return first empty cell found
    return None

print_board(board)
solve(board)
print("\nSolved Sudoku:\n")
print_board(board)
