
from collections import deque

def is_valid(i, j, visited):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1 or visited[i][j]:
        return False
    return True

def bfs(grid, start, end, k):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, 0, [])])
    while queue:
        current, count, path = queue.popleft()
        if current == end and count == k:
            return path + [current]
        for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            if is_valid(current[0] + i, current[1] + j, visited):
                visited[current[0] + i][current[1] + j] = True
                queue.append(((current[0] + i, current[1] + j), count + 1, path + [current]))
    return []

grid = [
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]
]

start = (13, 7)
end = (0, 0)
k = 4

result = bfs(grid, start, end, k)
print(result)
