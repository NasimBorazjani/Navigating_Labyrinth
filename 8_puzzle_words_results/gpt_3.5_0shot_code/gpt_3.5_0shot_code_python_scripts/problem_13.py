
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
    target_board = [['l', 'a', 'g', '_'], ['a', 'b', 'a', 's'], ['n', 'u', 'm', 'a'], ['s', 'h', 'a', 'm']]
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

initial_board = [['b', 'l', '_', 'g'], ['a', 'n', 'a', 's'], ['m', 'u', 'a', 'a'], ['s', 'h', 'a', 'm']]
target_words = ['lag', 'abas', 'numa', 'sham']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
