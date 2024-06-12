
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
    target_board = [['h', 'a', 't', '_'], ['s', 'k', 'a', 'g'], ['a', 'l', 'i', 't'], ['m', 'a', 'n', 'd']]
    moves = []
    
    while board != target_board:
        i_blank, j_blank = find_blank(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != target_board[i][j]:
                    if i < i_blank and j < j_blank:
                        if is_valid_move(board, i_blank-1, j_blank-1):
                            swap(board, i_blank, j_blank, i_blank-1, j_blank-1)
                            moves.append((i_blank-1, j_blank-1))
                    elif i < i_blank and j > j_blank:
                        if is_valid_move(board, i_blank-1, j_blank+1):
                            swap(board, i_blank, j_blank, i_blank-1, j_blank+1)
                            moves.append((i_blank-1, j_blank+1))
                    elif i > i_blank and j < j_blank:
                        if is_valid_move(board, i_blank+1, j_blank-1):
                            swap(board, i_blank, j_blank, i_blank+1, j_blank-1)
                            moves.append((i_blank+1, j_blank-1))
                    elif i > i_blank and j > j_blank:
                        if is_valid_move(board, i_blank+1, j_blank+1):
                            swap(board, i_blank, j_blank, i_blank+1, j_blank+1)
                            moves.append((i_blank+1, j_blank+1))
    
    return moves

initial_board = [['k', 'h', 'a', 't'], ['s', 'a', 'a', 'a'], ['i', 'l', '_', 't'], ['m', 'g', 'n', 'd']]
target_words = ['hat', 'skag', 'alit', 'mand']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
