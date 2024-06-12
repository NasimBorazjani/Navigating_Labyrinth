
from collections import deque

def find_blank(board):
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board = [list(row) for row in board]
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]
    return tuple(tuple(row) for row in board)

def bfs(board, target):
    queue = deque([board])
    paths = {board: []}
    while queue:
        board = queue.popleft()
        if board == target:
            return paths[board]
        i, j = find_blank(board)
        for di, dj, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                new_board = swap(board, i, j, i + di, j + dj)
                if new_board not in paths:
                    queue.append(new_board)
                    paths[new_board] = paths[board] + [direction]
    return None

board = (('a', 'r', 'o', 'f', 'n', 'y'), ('l', 'g', 'p', 'p', 'e', 'a'), ('a', 'n', 'n', 'i', '_', 'a'), ('l', 't', 'n', 'd', 's', 'e'), ('a', 'c', 'a', 'i', 'd', 'a'))
target = (('r', 'a', 'f', 't', 'y', '_'), ('l', 'a', 'p', 'p', 'e', 'd'), ('a', 'n', 'g', 'i', 'n', 'a'), ('l', 'a', 'n', 'o', 's', 'e'), ('a', 'c', 'n', 'i', 'd', 'a'))
print(bfs(board, target))
