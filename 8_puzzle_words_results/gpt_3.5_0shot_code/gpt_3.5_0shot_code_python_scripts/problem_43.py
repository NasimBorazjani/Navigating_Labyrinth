
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

def solve_sort_the_chars(board, target_words):
    moves = []
    target_board = [[c for c in word] for word in target_words]
    
    for i in range(len(target_board)):
        for j in range(len(target_board[0])):
            if target_board[i][j] == ' ':
                target_board[i][j] = '_'
    
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != target_board[i][j]:
                    if is_valid_move(board, i_blank-1, j_blank-1) and board[i_blank-1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank-1)
                        moves.append("up-left")
                    elif is_valid_move(board, i_blank-1, j_blank+1) and board[i_blank-1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank-1, j_blank+1)
                        moves.append("up-right")
                    elif is_valid_move(board, i_blank+1, j_blank-1) and board[i_blank+1][j_blank-1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank-1)
                        moves.append("down-left")
                    elif is_valid_move(board, i_blank+1, j_blank+1) and board[i_blank+1][j_blank+1] == target_board[i][j]:
                        swap(board, i_blank, j_blank, i_blank+1, j_blank+1)
                        moves.append("down-right")
    
    return moves

initial_board = [['a', 'd', 'a', 'o', 'n', 'e'], ['p', 'm', 'l', 'n', 'a', 'i'], ['_', 'n', 'c', 'o', 'd', 'a'], ['s', 'a', 'l', 't', 'l', 'y']]
target_words = ['dione', 'palmad', 'ancona', 'saltly']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
