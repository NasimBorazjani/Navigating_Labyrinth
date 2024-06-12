
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_the_chars(board, target_words):
    target_board = [['k', 'e', 'x', '_'], ['t', 'u', 'r', 'd'], ['w', 'a', 'b', 'i'], ['t', 'e', 's', 't']]
    actions = []

    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            i_new, j_new = i_blank + di, j_blank + dj
            if is_valid_move(board, i_new, j_new):
                swap(board, i_blank, j_blank, i_new, j_new)
                actions.append((di, dj))
                break

    return actions

initial_board = [['u', 'k', 'd', 'x'], ['t', 'e', 'r', 'b'], ['w', 'a', '_', 'i'], ['t', 'e', 's', 't']]
target_words = ['kex', 'turd', 'wabi', 'test']

actions = solve_sort_the_chars(initial_board, target_words)
print(actions)
