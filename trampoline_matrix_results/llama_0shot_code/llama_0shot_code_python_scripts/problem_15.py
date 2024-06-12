
from collections import deque

def is_valid(i, j, visited):
    if i<0 or j<0 or i>=9 or j>=9 or visited[i][j] or grid[i][j]==1:
        return False
    return True

def bfs(grid, start, end):
    visited = [[False for _ in range(9)] for _ in range(9)]
    visited[start[0]][start[1]] = True
    q = deque([(start, 0, [])])
    while q:
        node, step, path = q.popleft()
        if step == 3:
            if node == end:
                return path + [node]
            continue
        for i, j in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            x, y = node[0] + i, node[1] + j
            if is_valid(x, y, visited):
                visited[x][y] = True
                q.append(((x, y), step + 1, path + [node]))
    return []

grid = [
    [1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0]
]

start, end = (0, 7), (7, 1)
print(bfs(grid, start, end))
