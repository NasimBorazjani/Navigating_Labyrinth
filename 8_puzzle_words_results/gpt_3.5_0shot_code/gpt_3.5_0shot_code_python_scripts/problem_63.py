
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

def sort_chars(board, words):
    target_board = [['l', 'i', 'z', '_'], ['c', 'o', 'o', 's'], ['e', 'n', 'o', 's'], ['c', 'o', 'z', 'e'], ['g', 'a', 's', 't']]
    moves = []
    
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_valid_move(board, i, j):
                    if (i == i_blank - 1 and j == j_blank + 1) or (i == i_blank + 1 and j == j_blank + 1) or (i == i_blank - 1 and j == j_blank - 1) or (i == i_blank + 1 and j == j_blank - 1):
                        swap(board, i_blank, j_blank, i, j)
                        moves.append((i_blank, j_blank, i, j))
    
    return moves

initial_board = [['o', 'l', '_', 'z'], ['c', 'i', 'o', 's'], ['e', 'n', 'o', 's'], ['c', 'e', 'z', 'o'], ['g', 'a', 's', 't']]
target_words = ['liz', 'coos', 'enos', 'coze', 'gast']

swap_actions = sort_chars(initial_board, target_words)
print(swap_actions)
