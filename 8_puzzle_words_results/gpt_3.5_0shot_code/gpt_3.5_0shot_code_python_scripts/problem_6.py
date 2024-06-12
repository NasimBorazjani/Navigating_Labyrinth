
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
            if target_board[i][j] == ' ':
                target_board[i][j] = '_'
    
    while board != target_board:
        i, j = find_blank(board)
        
        if is_valid_move(board, i-1, j+1) and board[i-1][j+1] == target_board[i][j]:
            swap(board, i, j, i-1, j+1)
            moves.append("up-right")
        elif is_valid_move(board, i+1, j+1) and board[i+1][j+1] == target_board[i][j]:
            swap(board, i, j, i+1, j+1)
            moves.append("down-right")
        elif is_valid_move(board, i-1, j-1) and board[i-1][j-1] == target_board[i][j]:
            swap(board, i, j, i-1, j-1)
            moves.append("up-left")
        elif is_valid_move(board, i+1, j-1) and board[i+1][j-1] == target_board[i][j]:
            swap(board, i, j, i+1, j-1)
            moves.append("down-left")
    
    return moves

initial_board = [['l', 'c', '_', 'o'], ['s', 'c', 'o', 'h'], ['d', 'y', 'a', 'e'], ['h', 's', 'l', 't']]
target_words = ['cho', 'slod', 'syce', 'halt']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
