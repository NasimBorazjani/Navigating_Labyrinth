
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_the_chars(board, words):
    target_board = [['a', 'k', 'u', 'l', 'e', '_'], ['m', 'e', 's', 'o', 'd', 'e'], ['c', 'a', 'l', 'l', 'i', 'd'], ['g', 'y', 'r', 'o', 'u', 's']]
    target_words = ['akule', 'mesode', 'callid', 'gyrous']
    
    actions = []
    while board != target_board:
        blank_i, blank_j = find_blank(board)
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = blank_i + di, blank_j + dj
            if is_valid_move(board, new_i, new_j):
                swap(board, blank_i, blank_j, new_i, new_j)
                actions.append((di, dj))
                break
    
    return actions

initial_board = [['e', 'a', 'y', 'u', 'i', 'e'], ['m', 'k', 's', 'o', 'd', 'l'], ['c', 'a', '_', 'l', 'e', 'd'], ['g', 'l', 'r', 'o', 'u', 's']]
target_words = ['akule', 'mesode', 'callid', 'gyrous']

actions = solve_sort_the_chars(initial_board, target_words)
print(actions)
