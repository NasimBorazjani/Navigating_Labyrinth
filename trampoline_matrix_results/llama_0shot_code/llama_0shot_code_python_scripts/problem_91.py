
from collections import deque

def is_valid(i, j, visited):
    if i<0 or j<0 or i>=15 or j>=15 or visited[i][j] or grid[i][j]==1:
        return False
    return True

def bfs(start, end):
    visited = [[False]*15 for _ in range(15)]
    visited[start[0]][start[1]] = True
    q = deque([(start, [start])])
    while q:
        node, path = q.popleft()
        if node == end:
            return path
        for i, j in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            ni, nj = node[0]+i, node[1]+j
            if is_valid(ni, nj, visited):
                visited[ni][nj] = True
                q.append(((ni, nj), path + [(ni, nj)]))

grid = [
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]

start, end = (14, 2), (1, 9)
path = bfs(start, end)
print(path)
