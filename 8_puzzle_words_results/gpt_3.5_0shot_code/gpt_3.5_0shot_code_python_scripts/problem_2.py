
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
    target_board = [['_' if i == 0 and j == 0 else target_words[i-1][j] for j in range(len(board[0]))] for i in range(len(board))]
    
    moves = []
    while board != target_board:
        i, j = find_blank(board)
        if is_valid_move(board, i-1, j+1):
            swap(board, i, j, i-1, j+1)
            moves.append("up-right")
        elif is_valid_move(board, i+1, j+1):
            swap(board, i, j, i+1, j+1)
            moves.append("down-right")
        elif is_valid_move(board, i-1, j-1):
            swap(board, i, j, i-1, j-1)
            moves.append("up-left")
        elif is_valid_move(board, i+1, j-1):
            swap(board, i, j, i+1, j-1)
            moves.append("down-left")
    
    return moves

initial_board = [['o', 'a', 'u', 'o'], ['p', 'r', 'l', 'e'], ['f', 'a', '_', 'f'], ['m', 'k', 'd', 'd']]
target_words = ['ako', 'pole', 'raff', 'mudd']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
