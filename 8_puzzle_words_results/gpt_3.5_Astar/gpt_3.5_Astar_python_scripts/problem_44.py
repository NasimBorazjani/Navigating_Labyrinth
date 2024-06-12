 for this is as follows:

```
from itertools import product

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def get_blank_position(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return i, j

def swap(board, i, j, new_i, new_j):
    board[i][j], board[new_i][new_j] = board[new_i][new_j], board[i][j]

def is_sorted(board, words):
    for i in range(len(board)):
        word = ''.join(board[i]).replace('_', '')
        if word != words[i]:
            return False
    return True

def is_valid(board, words):
    for i in range(len(board)):
        word = ''.join(board[i]).replace('_', '')
        if word not in words:
            return False
    return True

def is_goal(board, words):
    return is_sorted(board, words) and is_valid(board, words)

def get_possible_moves(i, j, n, m):
    moves = []
    for a, b in product([-1, 1], [-1, 1]):
        new_i, new_j = i + a, j + b
        if is_valid(new_i, new_j, n, m):
            moves.append((new_i, new_j))
    return moves

def backtracking(board, words, i, j, n, m, depth):
    if is_goal(board, words):
        return True
    if depth == 0:
        return False
    for move in get_possible_moves(i, j, n, m):
        new_i, new_j = move
        swap(board, i, j, new_i, new_j)
        if backtracking(board, words, new_i, new_j, n, m, depth - 1):
            return True
        swap(board, i, j, new_i, new_j)
    return False

def is_valid(board, words):
    for i in range(len(board)):
        word = ''.join(board[i]).replace('_', '')
        if word not in words:
            return False
    return True

def is_goal(board, words):
    return is_sorted(board, words) and is_valid(board, words)

def sort_the_chars(board, words):
    n = len(board)
    m = len(board[0])
    depth = 2
    backtracking(board, words, 0, 0, n, m, depth)

board = [['h', 'b', 'n', 's', 'i', 't'], ['t', 'e', 'r', 'k', 'v', 'e'], ['i', 'i', '_', 'c', 'o', 'b'], ['h', 'u', 'm', 'a', 't', 'e']]
words = ['besit', 'thrive', 'kincob', 'humate']

sort_the_chars(board, words)
