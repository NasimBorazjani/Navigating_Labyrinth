
from collections import deque

def is_valid(pos, grid, visited, start, dest):
    x, y = pos
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and pos not in visited):
        return False
    diagonal_jumps = sum(abs(a-b) for a, b in [(x, y), start, dest]) // 2
    return diagonal_jumps == 4

def find_path(grid, start, dest):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        pos, path = queue.popleft()
        if pos == dest:
            return path
        for x, y in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_pos = (pos[0]+x, pos[1]+y)
            if is_valid(next_pos, grid, visited, start, dest):
                queue.append((next_pos, path+[next_pos]))
                visited.add(next_pos)

grid = [
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
]

start = (12, 0)
dest = (3, 8)

path = find_path(grid, start, dest)
print(path)
