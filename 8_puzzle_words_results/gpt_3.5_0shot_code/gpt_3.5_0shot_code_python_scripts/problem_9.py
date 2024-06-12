
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid_move(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def sort_chars(board, words):
    target_board = [['_' if i == 0 and j == 0 else words[i-1][j-1] for j in range(len(board[0]))] for i in range(len(board))]
    actions = []

    while board != target_board:
        i, j = find_blank(board)
        if i > 0 and j > 0 and board[i-1][j-1] == target_board[i][j]:
            swap(board, i, j, i-1, j-1)
            actions.append("up-left")
        elif i > 0 and j < len(board[0])-1 and board[i-1][j+1] == target_board[i][j]:
            swap(board, i, j, i-1, j+1)
            actions.append("up-right")
        elif i < len(board)-1 and j > 0 and board[i+1][j-1] == target_board[i][j]:
            swap(board, i, j, i+1, j-1)
            actions.append("down-left")
        elif i < len(board)-1 and j < len(board[0])-1 and board[i+1][j+1] == target_board[i][j]:
            swap(board, i, j, i+1, j+1)
            actions.append("down-right")

    return actions

initial_board = [['_', 's', 'a', 'n'], ['q', 'u', 'o', 'u'], ['c', 'h', 'u', 't'], ['l', 't', 'r', 'e']]
words = ['sun', 'quot', 'chat', 'lure']

actions = sort_chars(initial_board, words)
print(actions)
