
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
    target_board = [['d', 'y', 'k', 'e', '_'], ['a', 't', 'o', 'l', 'l'], ['a', 'm', 'u', 'z', 'e'], ['n', 'i', 'u', 'a', 'n']]
    moves = []

    for word in words:
        for char in word:
            i_blank, j_blank = find_blank(board)
            i_char, j_char = -1, -1

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == char:
                        i_char, j_char = i, j
                        break

            while i_blank != i_char or j_blank != j_char:
                if i_blank < i_char and j_blank < j_char:
                    if is_valid_move(board, i_blank+1, j_blank+1):
                        swap(board, i_blank, j_blank, i_blank+1, j_blank+1)
                        moves.append("down-right")
                        i_blank, j_blank = i_blank+1, j_blank+1
                elif i_blank < i_char and j_blank > j_char:
                    if is_valid_move(board, i_blank+1, j_blank-1):
                        swap(board, i_blank, j_blank, i_blank+1, j_blank-1)
                        moves.append("down-left")
                        i_blank, j_blank = i_blank+1, j_blank-1
                elif i_blank > i_char and j_blank < j_char:
                    if is_valid_move(board, i_blank-1, j_blank+1):
                        swap(board, i_blank, j_blank, i_blank-1, j_blank+1)
                        moves.append("up-right")
                        i_blank, j_blank = i_blank-1, j_blank+1
                elif i_blank > i_char and j_blank > j_char:
                    if is_valid_move(board, i_blank-1, j_blank-1):
                        swap(board, i_blank, j_blank, i_blank-1, j_blank-1)
                        moves.append("up-left")
                        i_blank, j_blank = i_blank-1, j_blank-1

    return moves

initial_board = [['t', 'd', 'u', 'k', 'e'], ['a', 'a', 'o', 'l', 'l'], ['a', 'm', '_', 'z', 'i'], ['n', 'e', 'u', 'y', 'n']]
words = ['dyke', 'atoll', 'amuze', 'niuan']

result = sort_chars(initial_board, words)
print(result)
