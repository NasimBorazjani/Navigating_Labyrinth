
from collections import deque

map = [
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1]
]

def is_valid(x, y, visited, map):
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and not visited[x][y] and map[x][y] == 0

def bfs(start, destination, map):
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        x, y = pos := queue.popleft()
        if pos == destination:
            return path
        for dx, dy in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited, map):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))
    return []

start = (3, 0)
destination = (9, 11)
path = bfs(start, destination, map)
print(path)
