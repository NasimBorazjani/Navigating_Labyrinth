
def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 'x':
                return i, j  # row, col
    return None

def is_valid(board, num, pos):
    # Check the number in the row
    for i in range(4):
        if board[pos[0]][i] != 'x' and int(board[pos[0]][i]) > num:
            return False

    # Check the number in the column
    for i in range(4):
        if board[i][pos[1]] != 'x' and int(board[i][pos[1]]) > num:
            return False

    # Check the number in the diagonal
    if pos[0] == pos[1]:
        for i in range(4):
            if board[i][i] != 'x' and int(board[i][i]) > num:
                return False

    return True

def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(7, 47):  # range from 7 to 46
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 'x'

    return False

def get_solution(board):
    solve_sudoku(board)
    result = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 'x':
                result.append((i, j, int(board[i][j])))
    return result

grid = [['11', '14', 'x', 'x'],
        ['12', 'x', 'x', '38'],
        ['x', 'x', 'x', '36'],
        ['25', 'x', 'x', '34']]

print(get_solution(grid))
