
from collections import deque

def bfs(grid, start, dest, max_diagonal_jumps):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0, 0, [start])])
    visited = set([start])
    while queue:
        pos, diagonal_jumps, steps, path = queue.popleft()
        if pos == dest and diagonal_jumps == max_diagonal_jumps:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x, y = pos[0] + dx, pos[1] + dy
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and (x, y) not in visited:
                visited.add((x, y))
                queue.append(((x, y), diagonal_jumps + 1, steps + 1, path + [(x, y)]))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = pos[0] + dx, pos[1] + dy
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and (x, y) not in visited:
                visited.add((x, y))
                queue.append(((x, y), diagonal_jumps, steps + 1, path + [(x, y)]))

grid = [
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 1]
]

start, dest = (8, 0), (0, 6)
print(bfs(grid, start, dest, 3))
