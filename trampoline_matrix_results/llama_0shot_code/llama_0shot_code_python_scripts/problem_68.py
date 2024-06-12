
from collections import deque

def is_valid(x, y, map, visited):
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and map[x][y] == 0 and not visited[x][y]

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
            if is_valid(nx, ny, map, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))
    return []

map = [
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
]

start = (11, 5)
destination = (0, 12)
path = bfs(start, destination, map)
print(path)
