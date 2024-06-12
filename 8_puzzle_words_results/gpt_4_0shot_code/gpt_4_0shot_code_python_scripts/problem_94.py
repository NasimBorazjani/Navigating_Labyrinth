
from collections import deque

def find_blank(board):
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def neighbors(i, j):
    return [(i-1, j+1), (i+1, j+1), (i-1, j-1), (i+1, j-1)]

def bfs(board, goal):
    start = [row[:] for row in board]
    queue = deque([("", start)])
    visited = set([str(start)])

    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        i, j = find_blank(current)
        for di, dj in neighbors(i, j):
            if 0 <= di < len(board) and 0 <= dj < len(board[0]):
                swap(current, i, j, di, dj)
                state = str(current)
                if state not in visited:
                    visited.add(state)
                    queue.append((path + str((di, dj)), [row[:] for row in current]))
                swap(current, i, j, di, dj)

    return "No solution found"

board = [['_', 'd', 'a', 'u', 'n', 'k'], ['a', 'r', 'm', 'r', 'r', 'e'], ['d', 'i', 'u', 'l', 'l', 't'], ['c', 'd', 'u', 'r', 'a', 'c'], ['m', 'i', 'g', 'a', 'o', 'h']]
goal = [['d', 'r', 'u', 'n', 'k', '_'], ['a', 'r', 'm', 'u', 'r', 'e'], ['d', 'i', 'g', 'l', 'o', 't'], ['c', 'a', 'u', 'd', 'a', 'l'], ['m', 'i', 'r', 'a', 'c', 'h']]
print(bfs(board, goal))
