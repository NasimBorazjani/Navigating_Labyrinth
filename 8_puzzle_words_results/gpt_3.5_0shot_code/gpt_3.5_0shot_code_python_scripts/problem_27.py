
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
    target_board = [list(word) for word in target_words]
    moves = []

    while board != target_board:
        i, j = find_blank(board)
        if i < len(board) - 1 and j < len(board[0]) - 1 and board[i+1][j+1] != '_':
            swap(board, i, j, i+1, j+1)
            moves.append("down-right")
        elif i > 0 and j < len(board[0]) - 1 and board[i-1][j+1] != '_':
            swap(board, i, j, i-1, j+1)
            moves.append("up-right")
        elif i < len(board) - 1 and j > 0 and board[i+1][j-1] != '_':
            swap(board, i, j, i+1, j-1)
            moves.append("down-left")
        elif i > 0 and j > 0 and board[i-1][j-1] != '_':
            swap(board, i, j, i-1, j-1)
            moves.append("up-left")

    return moves

initial_board = [['_', 'b', 'p', 'i', 's'], ['d', 'u', 'r', 'n', 'c'], ['l', 'i', 'o', 'e', 'n'], ['s', 'n', 'e', 'o', 't']]
target_words = ['bois', 'duroc', 'linen', 'spent']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
