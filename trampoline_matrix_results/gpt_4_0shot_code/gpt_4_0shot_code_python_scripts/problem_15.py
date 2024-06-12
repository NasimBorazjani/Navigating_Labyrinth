
from collections import deque

def bfs(grid, start, end):
    queue = deque([(start, 0, [start])])
    visited = set([start])
    while queue:
        (x, y), jumps, path = queue.popleft()
        if (x, y) == end and jumps == 3:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 9 and 0 <= ny < 9 and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                new_jumps = jumps + 1 if dx != 0 and dy != 0 else jumps
                if new_jumps <= 3:
                    queue.append(((nx, ny), new_jumps, path + [(nx, ny)]))
    return None

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
start = (0, 7)
end = (7, 1)
print(bfs(grid, start, end))
