
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def sort_chars(board, target_words):
    target_board = [['s', 'n', 'o', 'g'], ['t', 'r', 'e', 'm', 'a'], ['m', 'o', 's', 'u', 'r'], ['a', 'w', 'i', 'w', 'i']]
    moves = []
    
    for word in target_words:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    while board[i][j] != word[-1]:
                        blank_i, blank_j = find_blank(board)
                        if i < blank_i and j < blank_j:
                            if is_valid_move(board, blank_i-1, blank_j-1):
                                swap(board, blank_i, blank_j, blank_i-1, blank_j-1)
                                moves.append((blank_i-1, blank_j-1))
                        elif i < blank_i and j > blank_j:
                            if is_valid_move(board, blank_i-1, blank_j+1):
                                swap(board, blank_i, blank_j, blank_i-1, blank_j+1)
                                moves.append((blank_i-1, blank_j+1))
                        elif i > blank_i and j < blank_j:
                            if is_valid_move(board, blank_i+1, blank_j-1):
                                swap(board, blank_i, blank_j, blank_i+1, blank_j-1)
                                moves.append((blank_i+1, blank_j-1))
                        elif i > blank_i and j > blank_j:
                            if is_valid_move(board, blank_i+1, blank_j+1):
                                swap(board, blank_i, blank_j, blank_i+1, blank_j+1)
                                moves.append((blank_i+1, blank_j+1))
    
    return moves

initial_board = [['r', 's', 'w', 'o', 'g'], ['t', 'n', 'e', 'm', 'a'], ['m', 'o', '_', 'u', 's'], ['a', 'w', 'i', 'r', 'i']]
target_words = ['snog', 'trema', 'mosur', 'awiwi']

moves = sort_chars(initial_board, target_words)
print(moves)
