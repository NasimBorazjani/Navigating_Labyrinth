
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def sort_chars(board, words):
    target_board = [['_' if j == 0 else words[i][j-1] for j in range(len(board[0]))] for i in range(len(words))]
    actions = []

    while board != target_board:
        blank_i, blank_j = find_blank(board)
        for di, dj in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            new_i, new_j = blank_i + di, blank_j + dj
            if is_valid_move(board, new_i, new_j):
                swap(board, blank_i, blank_j, new_i, new_j)
                actions.append((di, dj))
                break

    return actions

initial_board = [['u', 'a', '_', 'r'], ['h', 'e', 'm', 'e'], ['m', 'i', 'i', 'p'], ['v', 'a', 'v', 'j'], ['f', 'i', 'm', 'i']]
target_words = ['aer', 'hume', 'mimp', 'viva', 'fiji']

actions = sort_chars(initial_board, target_words)
print(actions)
