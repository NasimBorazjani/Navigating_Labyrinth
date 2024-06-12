
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_the_chars(board, words):
    target_board = [['n', 'e', 'd', '_'], ['w', 'h', 'a', 'm'], ['r', 'o', 'y', 't'], ['h', 'e', 'l', 'l'], ['m', 'i', 'e', 'k']]
    moves = []
    
    while board != target_board:
        i, j = find_blank(board)
        if i < len(board) - 1 and board[i+1][j] == words[i+1][j]:
            swap(board, i, j, i+1, j)
            moves.append("down")
        elif i > 0 and board[i-1][j] == words[i-1][j]:
            swap(board, i, j, i-1, j)
            moves.append("up")
        elif j < len(board[0]) - 1 and board[i][j+1] == words[i][j+1]:
            swap(board, i, j, i, j+1)
            moves.append("right")
        elif j > 0 and board[i][j-1] == words[i][j-1]:
            swap(board, i, j, i, j-1)
            moves.append("left")
    
    return moves

initial_board = [['h', 'n', '_', 'd'], ['w', 'r', 'a', 'e'], ['e', 'o', 'y', 't'], ['h', 'e', 'l', 'm'], ['m', 'i', 'l', 'k']]
words = [['n', 'e', 'd', '_'], ['w', 'h', 'a', 'm'], ['r', 'o', 'y', 't'], ['h', 'e', 'l', 'l'], ['m', 'i', 'e', 'k']]

result = solve_sort_the_chars(initial_board, words)
print(result)
