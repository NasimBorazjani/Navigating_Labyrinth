
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board = [list(row) for row in board]
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]
    return tuple(tuple(row) for row in board)

def bfs(target, start):
    queue = deque([(start, None, None)])
    seen = set([start])
    parent = {start: (None, None)}
    while queue:
        board, _, _ = queue.popleft()
        if board == target:
            path = []
            while board:
                board, direction = parent[board]
                if direction:
                    path.append(direction)
            return path[::-1]
        i, j = find_blank(board)
        for di, dj, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                new_board = swap(board, i, j, i + di, j + dj)
                if new_board not in seen:
                    queue.append((new_board, board, direction))
                    seen.add(new_board)
                    parent[new_board] = (board, direction)
    return []

target = (('l', 'i', 'z', '_'), ('c', 'o', 'o', 's'), ('e', 'n', 'o', 's'), ('c', 'o', 'z', 'e'), ('g', 'a', 's', 't'))
start = (('o', 'l', '_', 'z'), ('c', 'i', 'o', 's'), ('e', 'n', 'o', 's'), ('c', 'o', 'z', 'e'), ('g', 'a', 's', 't'))
print(bfs(target, start))
