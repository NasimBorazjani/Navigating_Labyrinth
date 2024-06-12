
from collections import deque

def bfs(grid, start, end):
    queue = deque([(start, [start])])
    seen = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and
                grid[nx][ny] == 0 and (nx, ny) not in seen):
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                seen.add((nx, ny))

grid = [
    [1, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1]
]
start = (3, 7)
end = (8, 0)
print(bfs(grid, start, end))
