
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def sort_chars(board, target_words):
    target_board = [list(word) for word in target_words]
    actions = []

    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_valid_move(board, i, j) and (abs(i - i_blank) == 1 or abs(j - j_blank) == 1) and (abs(i - i_blank) == 1) != (abs(j - j_blank) == 1):
                    swap(board, i, j, i_blank, j_blank)
                    actions.append((i, j))
                    break

    return actions

initial_board = [['_', 'm', 'u', 'p'], ['c', 'e', 'r', 'a'], ['d', 'r', 'e', 'b'], ['v', 'e', 'l', 'o']]
target_words = ['map', 'cere', 'drub', 'velo']

actions = sort_chars(initial_board, target_words)
print(actions)
