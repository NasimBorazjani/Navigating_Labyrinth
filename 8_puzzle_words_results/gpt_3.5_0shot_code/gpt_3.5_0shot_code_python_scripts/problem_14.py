
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
    target_board = [['_' if i == 0 and j == 0 else words[i-1][j-1] for j in range(len(board[0]))] for i in range(len(board))]
    actions = []
    
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = i_blank + di, j_blank + dj
            if is_valid_move(board, new_i, new_j):
                swap(board, i_blank, j_blank, new_i, new_j)
                actions.append((di, dj))
                break
    
    return actions

initial_board = [['_', 'a', 't', 'n'], ['b', 'i', 'r', 'n'], ['k', 'r', 'e', 'y'], ['b', 'a', 'l', 'i']]
target_words = ['ann', 'birk', 'trey', 'bali']

actions = sort_chars(initial_board, target_words)
print(actions)
