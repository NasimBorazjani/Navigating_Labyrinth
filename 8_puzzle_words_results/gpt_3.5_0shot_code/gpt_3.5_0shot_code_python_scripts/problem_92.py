
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def is_valid_move(board, i, j):
    return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_sort_the_chars(board, target_words):
    moves = []
    directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

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
                for direction in directions:
                    new_i_blank, new_j_blank = i_blank + direction[0], j_blank + direction[1]
                    if is_valid_move(board, new_i_blank, new_j_blank):
                        swap(board, i_blank, j_blank, new_i_blank, new_j_blank)
                        moves.append((new_i_blank, new_j_blank))
                        i_blank, j_blank = new_i_blank, new_j_blank
                        break

    return moves

target_words = ['shrew', 'bedark', 'curcas', 'bender', 'hocker']
initial_board = [['e', 's', '_', 'r', 'k', 'w'], ['b', 'c', 'd', 'd', 'r', 'a'], ['c', 'u', 'e', 'c', 'e', 's'], ['b', 'r', 'n', 'h', 'e', 'a'], ['h', 'o', 'e', 'k', 'r', 'r']]

moves = solve_sort_the_chars(initial_board, target_words)
print(moves)
