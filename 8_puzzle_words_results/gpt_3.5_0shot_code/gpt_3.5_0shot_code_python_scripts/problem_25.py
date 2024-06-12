
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
    
    for i in range(len(target_board)):
        for j in range(len(target_board[0])):
            if board[i][j] != target_board[i][j]:
                target_i, target_j = i, j
                break
    
    while board != target_board:
        blank_i, blank_j = find_blank(board)
        
        if blank_i < target_i and blank_j < target_j:
            if is_valid_move(board, blank_i+1, blank_j+1):
                swap(board, blank_i, blank_j, blank_i+1, blank_j+1)
                moves.append("down-right")
        elif blank_i < target_i and blank_j > target_j:
            if is_valid_move(board, blank_i+1, blank_j-1):
                swap(board, blank_i, blank_j, blank_i+1, blank_j-1)
                moves.append("down-left")
        elif blank_i > target_i and blank_j < target_j:
            if is_valid_move(board, blank_i-1, blank_j+1):
                swap(board, blank_i, blank_j, blank_i-1, blank_j+1)
                moves.append("up-right")
        elif blank_i > target_i and blank_j > target_j:
            if is_valid_move(board, blank_i-1, blank_j-1):
                swap(board, blank_i, blank_j, blank_i-1, blank_j-1)
                moves.append("up-left")
    
    return moves

initial_board = [['i', 'g', 'u', 'h', 'a'], ['n', 'o', 's', 'u', 's'], ['c', 'n', 'g', 'a', '_'], ['j', 'u', 'u', 'p', 'h']]
target_words = ['guha', 'nisus', 'uncap', 'jough']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
