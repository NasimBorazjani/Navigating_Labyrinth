
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
    target_board = [['k', 'e', 'n', '_'], ['k', 'h', 'a', 't'], ['k', 'i', 'l', 'l'], ['w', 'e', 'n', 't']]
    actions = []

    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_valid_move(board, i, j) and (abs(i - i_blank) == 1 or abs(j - j_blank) == 1) and abs(i - i_blank) + abs(j - j_blank) == 1:
                    swap(board, i, j, i_blank, j_blank)
                    actions.append((i, j))
                    break

    return actions

initial_board = [['h', 'k', 't', 'n'], ['k', 'e', 'a', 'k'], ['e', 'i', '_', 'l'], ['w', 'l', 'n', 't']]
target_words = ['ken', 'khat', 'kill', 'went']

actions = solve_sort_the_chars(initial_board, target_words)
print(actions)
