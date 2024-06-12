
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
    target_board = [['_' for _ in range(len(board[0]))] for _ in range(len(board))]
    for i, word in enumerate(words):
        for j, char in enumerate(word):
            target_board[i][j] = char

    actions = []
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i = i_blank + di
            new_j = j_blank + dj
            if is_valid_move(board, new_i, new_j):
                swap(board, i_blank, j_blank, new_i, new_j)
                actions.append((di, dj))
                break

    return actions

initial_board = [['e', 'l', 'u', 'w'], ['k', 'k', 'c', 'e'], ['f', 'l', '_', 'a'], ['s', 'r', 's', 'e'], ['h', 'e', 'u', 'b']]
target_words = ['lew', 'keck', 'flea', 'susu', 'herb']

actions = sort_chars(initial_board, target_words)
print(actions)
