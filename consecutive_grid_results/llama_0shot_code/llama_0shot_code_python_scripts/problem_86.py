
def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 'x':
                return i, j  # row, col
    return None

def is_valid(board, num, pos):
    # Check the number in the row
    for i in range(4):
        if board[pos[0]][i] != 'x' and num == board[pos[0]][i]:
            return False

    # Check the number in the column
    for i in range(4):
        if board[i][pos[1]] != 'x' and num == board[i][pos[1]]:
            return False

    # Check the number in the diagonal
    if pos[0] == pos[1]:
        for i in range(4):
            if board[i][i] != 'x' and num == board[i][i]:
                return False

    if pos[0] + pos[1] == 3:
        for i in range(4):
            if board[i][3 - i] != 'x' and num == board[i][3 - i]:
                return False

    return True

def solve(board):
    num = 6
    empty = find_empty(board)
    if not empty:
        return board
    row, col = empty
    while num < 56:
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 'x'
        num += 1
    return False

def get_solution(board):
    solve(board)
    result = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 'x':
                result.append((i, j, num))
    return result

board = [['x', 'x', 'x', '54'],
         ['x', 'x', '44', '53'],
         ['x', '17', 'x', 'x'],
         ['18', '22', '36', 'x']]

print(get_solution(board))
