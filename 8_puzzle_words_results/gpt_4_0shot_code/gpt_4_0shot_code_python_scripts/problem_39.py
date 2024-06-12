
from collections import deque

def get_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def get_moves(i, j, n, m):
    moves = []
    if i > 0 and j < m - 1:
        moves.append((i - 1, j + 1, 'up-right'))
    if i < n - 1 and j < m - 1:
        moves.append((i + 1, j + 1, 'down-right'))
    if i > 0 and j > 0:
        moves.append((i - 1, j - 1, 'up-left'))
    if i < n - 1 and j > 0:
        moves.append((i + 1, j - 1, 'down-left'))
    return moves

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]
    return board

def is_sorted(board, words):
    for i in range(len(board)):
        if ''.join(board[i]) != words[i]:
            return False
    return True

def sort_board(board, words):
    n, m = len(board), len(board[0])
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        board, path = queue.popleft()
        if is_sorted(board, words):
            return path
        i, j = get_blank(board)
        for ni, nj, direction in get_moves(i, j, n, m):
            new_board = [row[:] for row in board]
            new_board = swap(new_board, i, j, ni, nj)
            if str(new_board) not in visited:
                queue.append((new_board, path + [direction]))
                visited.add(str(new_board))
    return []

words = ['jibby', 'entone', 'xenium', 'enwomb']
board = [['n', 'j', '_', 'b', 'e', 'y'], ['e', 'i', 't', 'u', 'n', 'o'], ['x', 'e', 'n', 'i', 'b', 'm'], ['e', 'n', 'w', 'o', 'm', 'b']]
print(sort_board(board, words))
