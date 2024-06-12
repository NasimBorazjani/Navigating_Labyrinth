
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_the_chars(board, words):
    target_board = [['c', 'a', 'm', '_'], ['h', 'i', 'l', 'l'], ['p', 'r', 'a', 'y'], ['d', 'o', 'e', 'r']]
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

initial_board = [['i', 'c', 'a', 'm'], ['h', 'p', 'l', 'o'], ['_', 'r', 'a', 'y'], ['d', 'l', 'e', 'r']]
target_words = ['cam', 'hill', 'pray', 'doer']

actions = solve_sort_the_chars(initial_board, target_words)
print(actions)
