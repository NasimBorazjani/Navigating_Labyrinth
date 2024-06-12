
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
    moves = []
    target_board = [[c for c in word] for word in target_words]

    while board != target_board:
        i, j = find_blank(board)
        possible_moves = [(i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]

        for move in possible_moves:
            if is_valid_move(board, move[0], move[1]):
                swap(board, i, j, move[0], move[1])
                moves.append((move[0], move[1]))
                break

    return moves

initial_board = [['h', 'b', 'c', 't', 'h'], ['k', 'n', 'i', 'o', 'a'], ['a', 's', '_', 'o', 'a'], ['c', 'l', 'a', 's', 't']]
target_words = ['bath', 'khila', 'ascon', 'coast']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
