
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

def solve_sort_chars(board, words):
    target_board = [['n', 'e', 't', '_'], ['t', 'o', 's', 's'], ['f', 'l', 'i', 'p'], ['s', 'w', 'a', 'g'], ['b', 'o', 's', 'n']]
    actions = []
    
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != target_board[i][j]:
                    if i < i_blank and j < j_blank:
                        if is_valid_move(board, i_blank-1, j_blank-1):
                            swap(board, i_blank, j_blank, i_blank-1, j_blank-1)
                            actions.append("up-left")
                    elif i < i_blank and j > j_blank:
                        if is_valid_move(board, i_blank-1, j_blank+1):
                            swap(board, i_blank, j_blank, i_blank-1, j_blank+1)
                            actions.append("up-right")
                    elif i > i_blank and j < j_blank:
                        if is_valid_move(board, i_blank+1, j_blank-1):
                            swap(board, i_blank, j_blank, i_blank+1, j_blank-1)
                            actions.append("down-left")
                    elif i > i_blank and j > j_blank:
                        if is_valid_move(board, i_blank+1, j_blank+1):
                            swap(board, i_blank, j_blank, i_blank+1, j_blank+1)
                            actions.append("down-right")
    
    return actions

initial_board = [['o', 'n', 's', 't'], ['t', 'e', 's', 'w'], ['i', 'l', 's', 'p'], ['s', 'g', 'a', 'f'], ['b', 'o', '_', 'n']]
target_words = ['net', 'toss', 'flip', 'swag', 'bosn']

actions = solve_sort_chars(initial_board, target_words)
print(actions)
