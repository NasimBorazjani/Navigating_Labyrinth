
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
    target_board = [['j', 'e', 'h', 'u', '_'], ['w', 'o', 'r', 'm', 'y'], ['l', 'i', 'n', 't', 'y'], ['i', 'l', 'i', 'a', 'l']]
    moves = []
    
    while board != target_board:
        i, j = find_blank(board)
        if i < len(board) - 1 and board[i+1][j] == target_board[i][j]:
            swap(board, i, j, i+1, j)
            moves.append("down")
        elif i > 0 and board[i-1][j] == target_board[i][j]:
            swap(board, i, j, i-1, j)
            moves.append("up")
        elif j < len(board[0]) - 1 and board[i][j+1] == target_board[i][j]:
            swap(board, i, j, i, j+1)
            moves.append("right")
        elif j > 0 and board[i][j-1] == target_board[i][j]:
            swap(board, i, j, i, j-1)
            moves.append("left")
    
    return moves

initial_board = [['o', 'j', '_', 'h', 'u'], ['w', 'l', 'r', 'e', 'y'], ['n', 'i', 'l', 't', 'a'], ['i', 'y', 'i', 'm', 'l']]
target_words = ['jehu', 'wormy', 'linty', 'ilial']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
