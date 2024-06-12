
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
    target_board = [['f', 'a', '_', 'e'], ['t', 'r', 'a', 'h'], ['f', 'e', 'a', 't'], ['f', 'i', 'n', 'e'], ['d', 'a', 'f', 'f']]
    actions = []
    
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != target_board[i][j]:
                    if is_valid_move(board, i_blank-1, j_blank+1) and board[i_blank-1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank+1)
                        actions.append((i_blank-1, j_blank+1))
                    elif is_valid_move(board, i_blank+1, j_blank+1) and board[i_blank+1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank+1)
                        actions.append((i_blank+1, j_blank+1))
                    elif is_valid_move(board, i_blank-1, j_blank-1) and board[i_blank-1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank-1)
                        actions.append((i_blank-1, j_blank-1))
                    elif is_valid_move(board, i_blank+1, j_blank-1) and board[i_blank+1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank-1)
                        actions.append((i_blank+1, j_blank-1))
    
    return actions

initial_board = [['r', 'f', '_', 'e'], ['t', 'a', 'a', 'f'], ['a', 'e', 'f', 't'], ['f', 'i', 'n', 'h'], ['d', 'a', 'e', 'f']]
target_words = ['fae', 'trah', 'feat', 'fine', 'daff']

actions = sort_chars(initial_board, target_words)
print(actions)
