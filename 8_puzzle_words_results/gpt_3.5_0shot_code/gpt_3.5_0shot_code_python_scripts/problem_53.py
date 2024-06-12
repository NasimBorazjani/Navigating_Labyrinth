
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_the_chars(board, target_words):
    moves = []
    target_board = [['l', 'i', 'm', 'e', 'n', '_'], ['s', 'o', 'm', 'e', 'r', 's'], ['s', 'p', 'o', 'o', 'k', 'y'], ['d', 'o', 'g', 't', 'i', 'e']]
    
    while board != target_board:
        blank_i, blank_j = find_blank(board)
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = blank_i + di, blank_j + dj
            if is_valid_move(board, new_i, new_j):
                swap(board, blank_i, blank_j, new_i, new_j)
                moves.append((di, dj))
                break
    
    return moves

initial_board = [['o', 'l', 's', 'm', '_', 'n'], ['s', 'o', 'm', 'e', 'r', 'k'], ['s', 'p', 'i', 'o', 'e', 'y'], ['d', 'o', 'g', 't', 'i', 'e']]
target_words = ['limen', 'somers', 'spooky', 'dogtie']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
