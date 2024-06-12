
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
    target_board = [['s', 'o', 'n', 'g', '_'], ['a', 'm', 'i', 's', 'h'], ['h', 'i', 'p', 'e', 'r'], ['a', 'g', 'l', 'e', 'y']]
    actions = []
    
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_valid_move(board, i, j):
                    if (i == i_blank - 1 and j == j_blank + 1) or (i == i_blank + 1 and j == j_blank + 1) or (i == i_blank - 1 and j == j_blank - 1) or (i == i_blank + 1 and j == j_blank - 1):
                        swap(board, i_blank, j_blank, i, j)
                        actions.append((i_blank, j_blank, i, j))
    
    return actions

initial_board = [['m', 's', '_', 'n', 'g'], ['a', 'o', 'i', 'e', 'h'], ['h', 'i', 'p', 'e', 's'], ['a', 'g', 'l', 'r', 'y']]
words = ['song', 'amish', 'hiper', 'agley']

actions = solve_sort_the_chars(initial_board, words)
print(actions)
