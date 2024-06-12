
from collections import deque

def bfs(start, end, grid):
    queue = deque([(start, 0, [start])])
    visited = set([start])
    while queue:
        (x, y), jumps, path = queue.popleft()
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 9 and 0 <= ny < 9 and grid[nx][ny] == 0:
                if (nx, ny) not in visited:
                    if jumps < 3:
                        queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
                        visited.add((nx, ny))
                    elif jumps == 3 and (nx, ny) == end:
                        return path + [(nx, ny)]
    return None

grid = [
    [1, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start = (8, 2)
end = (0, 7)
print(bfs(start, end, grid))
