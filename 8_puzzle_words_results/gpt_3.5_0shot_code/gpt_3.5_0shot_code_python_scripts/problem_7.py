
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
    target_board = [['c', 'r', 'y', '_'], ['d', 'u', 'n', 'e'], ['r', 'u', 'm', 'p'], ['k', 'n', 'e', 'e']]
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

initial_board = [['u', 'c', 'r', 'y'], ['d', 'n', 'n', 'r'], ['_', 'u', 'm', 'p'], ['k', 'e', 'e', 'e']]
target_words = ['cry', 'dune', 'rump', 'knee']

actions = solve_sort_the_chars(initial_board, target_words)
print(actions)
