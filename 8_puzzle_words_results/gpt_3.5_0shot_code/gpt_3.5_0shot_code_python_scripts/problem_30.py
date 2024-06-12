
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
    target_board = [['l', 'e', 't', 'e', '_'], ['s', 'a', 'r', 'u', 's'], ['b', 'r', 'y', 'a', 'n'], ['w', 'h', 'i', 'n', 'g']]
    moves = []
    
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != target_board[i][j]:
                    if is_valid_move(board, i_blank-1, j_blank-1) and board[i_blank-1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank-1)
                        moves.append((i_blank-1, j_blank-1))
                    elif is_valid_move(board, i_blank-1, j_blank+1) and board[i_blank-1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank+1)
                        moves.append((i_blank-1, j_blank+1))
                    elif is_valid_move(board, i_blank+1, j_blank-1) and board[i_blank+1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank-1)
                        moves.append((i_blank+1, j_blank-1))
                    elif is_valid_move(board, i_blank+1, j_blank+1) and board[i_blank+1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank+1)
                        moves.append((i_blank+1, j_blank+1))
    
    return moves

initial_board = [['a', 'l', '_', 't', 'e'], ['s', 'h', 'r', 'b', 's'], ['e', 'r', 'u', 'a', 'n'], ['w', 'y', 'i', 'n', 'g']]
target_words = ['lete', 'sarus', 'bryan', 'whing']

swap_actions = sort_chars(initial_board, target_words)
print(swap_actions)
