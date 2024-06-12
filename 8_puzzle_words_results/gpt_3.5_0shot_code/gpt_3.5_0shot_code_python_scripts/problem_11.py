
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def is_valid_move(board, i, j):
    if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
        return True
    return False

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_the_chars(board, target_words):
    moves = []
    for word in target_words:
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

initial_board = [['o', 'b', 'e', 'd'], ['c', 'o', 'd', 'u'], ['w', 'a', '_', 'p'], ['y', 'u', 'l', 'p']]
target_words = ['bud', 'codo', 'waup', 'yelp']

result = solve_sort_the_chars(initial_board, target_words)
print(result)
