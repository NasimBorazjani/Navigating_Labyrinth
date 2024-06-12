
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

def solve_sort_the_chars(board, words):
    target_board = [['w', 'o', 'l', 'f', '_'], ['s', 't', 'u', 'n', 't'], ['l', 'a', 'm', 'm', 'y'], ['f', 'a', 'd', 'e', 'd']]
    actions = []

    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != target_board[i][j]:
                    if is_valid_move(board, i_blank-1, j_blank-1) and board[i_blank-1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank-1)
                        actions.append("up-left")
                    elif is_valid_move(board, i_blank-1, j_blank+1) and board[i_blank-1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank+1)
                        actions.append("up-right")
                    elif is_valid_move(board, i_blank+1, j_blank-1) and board[i_blank+1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank-1)
                        actions.append("down-left")
                    elif is_valid_move(board, i_blank+1, j_blank+1) and board[i_blank+1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank+1)
                        actions.append("down-right")
    
    return actions

initial_board = [['t', 'w', 'y', 'l', '_'], ['s', 'a', 'u', 'f', 't'], ['o', 'a', 'e', 'm', 'n'], ['f', 'l', 'd', 'm', 'd']]
target_words = ['wolf', 'stunt', 'lammy', 'faded']

actions = solve_sort_the_chars(initial_board, target_words)
print(actions)
