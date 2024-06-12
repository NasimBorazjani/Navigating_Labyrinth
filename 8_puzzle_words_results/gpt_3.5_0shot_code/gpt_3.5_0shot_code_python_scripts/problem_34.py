
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
    target_board = [[c for c in word] for word in target_words]
    target_board[0].append('_')
    
    moves = []
    
    while board != target_board:
        blank_i, blank_j = find_blank(board)
        
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = blank_i + di, blank_j + dj
            if is_valid_move(board, new_i, new_j):
                swap(board, blank_i, blank_j, new_i, new_j)
                moves.append((di, dj))
                break
    
    return moves

initial_board = [['u', 's', 'o', 'f', 't'], ['t', 'a', 'n', 'n', 'y'], ['a', 'p', '_', 'm', 'o'], ['f', 'u', 'r', 'a', 'm']]
target_words = ['soft', 'tunny', 'apama', 'forum']

moves = solve_sort_the_chars(initial_board, target_words)
print(moves)
