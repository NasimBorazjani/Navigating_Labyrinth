
from collections import deque

def bfs(grid, start, end):
    queue = deque([(start, 0, [start])])
    visited = set([start])
    while queue:
        (x, y), jumps, path = queue.popleft()
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 9 and 0 <= ny < 9 and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_jumps = jumps + (dx != 0 and dy != 0)
                if new_jumps > 3:
                    continue
                new_path = path + [(nx, ny)]
                if (nx, ny) == end and new_jumps == 3:
                    return new_path
                visited.add((nx, ny))
                queue.append(((nx, ny), new_jumps, new_path))
    return None

grid = [
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1]
]

start = (8, 1)
end = (0, 5)
print(bfs(grid, start, end))
