
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return (i, j)

def swap(board, i1, j1, i2, j2):
    board = [list(row) for row in board]
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]
    return tuple(tuple(row) for row in board)

def bfs(board, target):
    start = tuple(tuple(row) for row in board)
    target = tuple(tuple(row) for row in target)
    queue = deque([start])
    visited = set([start])
    prev = {start: (None, None)}
    while queue:
        curr = queue.popleft()
        if curr == target:
            actions = []
            while curr != start:
                curr, action = prev[curr]
                actions.append(action)
            actions.reverse()
            return actions
        i, j = find_blank(curr)
        for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                next = swap(curr, i, j, ni, nj)
                if next not in visited:
                    queue.append(next)
                    visited.add(next)
                    prev[next] = (curr, action)
    return None

board = [['u', 's', 'o', 'f', 't'], ['t', 'a', 'n', 'n', 'y'], ['a', 'p', '_', 'm', 'o'], ['f', 'u', 'r', 'a', 'm']]
target = [['_', 's', 'o', 'f', 't'], ['t', 'u', 'n', 'n', 'y'], ['a', 'p', 'a', 'm', 'a'], ['f', 'o', 'r', 'u', 'm']]
print(bfs(board, target))
