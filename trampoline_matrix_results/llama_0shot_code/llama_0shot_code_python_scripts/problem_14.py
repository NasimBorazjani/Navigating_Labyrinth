
from collections import deque

grid = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0]
]

def is_valid(pos, visited):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and pos not in visited

def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            next_pos = (pos[0] + dx, pos[1] + dy)
            if is_valid(next_pos, visited):
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))

start, end = (0, 7), (7, 0)
path = bfs(start, end)
print(path)
