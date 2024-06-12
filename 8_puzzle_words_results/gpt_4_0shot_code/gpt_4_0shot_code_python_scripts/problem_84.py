
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

def bfs(initial, target):
    queue = deque([initial])
    visited = set([initial])
    prev = {initial: (None, None)}
    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            while current != initial:
                current, action = prev[current]
                path.append(action)
            path.reverse()
            return path
        i, j = find_blank(current)
        for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            if 0 <= i + di < len(current) and 0 <= j + dj < len(current[0]):
                next = swap(current, i, j, i + di, j + dj)
                if next not in visited:
                    queue.append(next)
                    visited.add(next)
                    prev[next] = (current, action)
    return None

initial = (('e', 'r', 'p', 't', 'o'), ('s', 't', 'r', 'k', 'r'), ('e', 'a', '_', 'a', 'i'), ('d', 'o', 'n', 's', 'a'), ('d', 'e', 's', 'e', 'x'))
target = (('r', 'o', 't', 'o', '_'), ('s', 'e', 'r', 'e', 'r'), ('t', 'a', 'p', 'a', 's'), ('d', 'i', 'n', 'k', 'a'), ('d', 'e', 's', 'e', 'x'))
print(bfs(initial, target))
