
from collections import deque

def is_valid(x, y, map, visited):
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and map[x][y] == 0 and not visited[x][y]

def bfs(start, destination, map):
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        x, y = queue.popleft()
        if (x, y) == destination:
            return queue.popleft()[1]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -2), (0, 2), (-2, 0), (2, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, map, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), queue[-1][1] + [(nx, ny)]))
    return None

map = [
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    # ... more rows ...
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
]

start = (1, 3)
destination = (12, 11)

print(bfs(start, destination, map))
