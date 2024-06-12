
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def swap(board, pos, direction):
    i, j = pos
    if direction == 'up-right' and i > 0 and j < len(board[0]) - 1:
        board[i][j], board[i-1][j+1] = board[i-1][j+1], board[i][j]
    elif direction == 'down-right' and i < len(board) - 1 and j < len(board[0]) - 1:
        board[i][j], board[i+1][j+1] = board[i+1][j+1], board[i][j]
    elif direction == 'up-left' and i > 0 and j > 0:
        board[i][j], board[i-1][j-1] = board[i-1][j-1], board[i][j]
    elif direction == 'down-left' and i < len(board) - 1 and j > 0:
        board[i][j], board[i+1][j-1] = board[i+1][j-1], board[i][j]

def is_sorted(board, target):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != target[i][j]:
                return False
    return True

def sort_board(board, target):
    queue = deque([(board, [])])
    visited = set()
    while queue:
        board, path = queue.popleft()
        if str(board) in visited:
            continue
        visited.add(str(board))
        if is_sorted(board, target):
            return path
        blank = find_blank(board)
        for direction in ['up-right', 'down-right', 'up-left', 'down-left']:
            new_board = [row[:] for row in board]
            swap(new_board, blank, direction)
            queue.append((new_board, path + [direction]))

board = [['r', 'p', '_', 'n', 'n', 'o'], ['u', 'o', 'c', 'o', 'i', 'n'], ['l', 'n', 'h', 'i', 'g', 'e'], ['b', 'd', 'i', 'n', 'k', 's']]
target = [['p', 'o', 'n', 'g', 'o', '_'], ['u', 'r', 'c', 'h', 'i', 'n'], ['o', 'n', 'd', 'i', 'n', 'e'], ['b', 'l', 'i', 'n', 'k', 's']]
print(sort_board(board, target))
