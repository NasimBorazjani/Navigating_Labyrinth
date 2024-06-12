
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def sort_chars(board, words):
    target_board = [['h', 'e', 'l', 'e', 'n', '_'], ['a', 'd', 'e', 'l', 'e', 'a'], ['b', 'u', 'm', 'b', 'l', 'e'], ['i', 'o', 'd', 'i', 's', 'm'], ['t', 'r', 'u', 'l', 'l', 'o']]
    actions = []

    while board != target_board:
        i, j = find_blank(board)
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = i + di, j + dj
            if is_valid_move(board, new_i, new_j):
                swap(board, i, j, new_i, new_j)
                actions.append((di, dj))
                break

    return actions

initial_board = [['d', 'h', '_', 'l', 'e', 'n'], ['a', 'a', 'e', 'b', 'e', 'u'], ['m', 'u', 'i', 'b', 'e', 'e'], ['i', 'o', 'd', 'm', 's', 'l'], ['t', 'r', 'l', 'l', 'l', 'o']]
target_words = ['helen', 'adelea', 'bumble', 'iodism', 'trullo']

actions = sort_chars(initial_board, target_words)
print(actions)
