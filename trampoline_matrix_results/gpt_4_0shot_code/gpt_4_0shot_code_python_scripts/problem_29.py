
from collections import deque

def bfs(grid, start, end):
    queue = deque([(start, 0, 0, [start])])
    visited = set([start])
    while queue:
        (x, y), d, jumps, path = queue.popleft()
        if (x, y) == end and jumps == 3:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and grid[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append(((nx, ny), d + 1, jumps + 1, path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

grid = [
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
]

start = (9, 0)
end = (1, 5)
print(bfs(grid, start, end))
