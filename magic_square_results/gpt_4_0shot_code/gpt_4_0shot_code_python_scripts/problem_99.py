
import numpy as np

def is_valid(board, row, col, num):
    # Check if the number already exists in the row or column
    for x in range(2):
        if board[row][x] == num or board[x][col] == num:
            return False

    # Check if the number already exists in the diagonal
    if row == col and board[0][1] + num != 5:
        return False

    return True

def solve_magic_square(board):
    for i in range(2):
        for j in range(2):
            if board[i][j] == 'x':
                for num in range(1, 5):
                    if is_valid(board, i, j, num):
                        board[i][j] = num

                        if solve_magic_square(board):
                            return True

                        board[i][j] = 'x'

                return False

    return True

# Initialize the board
board = np.array([['1', 'x'], ['x', 'x']], dtype='object')

if solve_magic_square(board):
    print(board)
else:
    print("No solution exists")
