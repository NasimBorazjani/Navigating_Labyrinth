
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_chars(board, words):
    target_board = [['s', 'i', 'v', 'a', '_'], ['b', 'r', 'y', 'c', 'e'], ['b', 'i', 'r', 'n', 'y'], ['p', 'u', 'g', 'i', 'l'], ['l', 'i', 'n', 'n', 'e']]
    moves = []

    while board != target_board:
        i, j = find_blank(board)
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = i + di, j + dj
            if is_valid_move(board, new_i, new_j):
                swap(board, i, j, new_i, new_j)
                moves.append((di, dj))
                break

    return moves

initial_board = [['r', 's', 'c', 'v', 'a'], ['b', 'b', 'y', 'r', 'e'], ['u', 'i', '_', 'n', 'i'], ['p', 'n', 'g', 'i', 'l'], ['l', 'i', 'y', 'n', 'e']]
target_words = ['siva', 'bryce', 'birny', 'pugil', 'linne']

moves = solve_sort_chars(initial_board, target_words)
print(moves)
