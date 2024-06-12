
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    return True

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def sort_chars(board, words):
    target_board = [['s', 'u', 'p', 'e', '_'], ['c', 'a', 'd', 'u', 's'], ['n', 'u', 'c', 'a', 'l'], ['r', 'o', 'u', 's', 'e']]
    actions = []

    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != target_board[i][j]:
                    if is_valid_move(board, i_blank-1, j_blank-1) and board[i_blank-1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank-1)
                        actions.append((i_blank-1, j_blank-1))
                    elif is_valid_move(board, i_blank-1, j_blank+1) and board[i_blank-1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank+1)
                        actions.append((i_blank-1, j_blank+1))
                    elif is_valid_move(board, i_blank+1, j_blank-1) and board[i_blank+1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank-1)
                        actions.append((i_blank+1, j_blank-1))
                    elif is_valid_move(board, i_blank+1, j_blank+1) and board[i_blank+1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank+1)
                        actions.append((i_blank+1, j_blank+1))
    
    return actions

initial_board = [['a', 's', '_', 'p', 'e'], ['c', 'u', 'd', 'o', 's'], ['l', 'u', 'u', 'a', 's'], ['r', 'c', 'u', 'n', 'e']]
words = ['supe', 'cadus', 'nucal', 'rouse']

actions = sort_chars(initial_board, words)
print(actions)
