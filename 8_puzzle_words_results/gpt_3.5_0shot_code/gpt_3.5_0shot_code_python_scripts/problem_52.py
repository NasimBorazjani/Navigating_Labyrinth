
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
        return True
    return False

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_the_chars(board, target_words):
    moves = []
    target_board = [[c for c in word] for word in target_words]
    
    while board != target_board:
        i, j = find_blank(board)
        possible_moves = [(i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]
        
        for move in possible_moves:
            if is_valid_move(board, move[0], move[1]):
                swap(board, i, j, move[0], move[1])
                moves.append((move[0]-i, move[1]-j))
                break
    
    return moves

initial_board = [['i', 's', 'n', 'i', 'a', 'h'], ['l', 'p', 'e', 'a', 'r', 'c'], ['_', 'c', 'e', 'e', 'n', 'd'], ['e', 'v', 'e', 'r', 'l', 'y']]
target_words = ['saiph', 'lierre', 'accend', 'evenly']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
