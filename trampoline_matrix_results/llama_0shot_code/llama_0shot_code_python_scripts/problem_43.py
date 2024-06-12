
from collections import deque

grid = [
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
]

def generate_next_positions(pos, jumps):
    x, y = pos
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        for _ in range(3 - jumps):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                yield (nx, ny), jumps + 1
                dx, dy = 0, 0  # Stop after first valid jump in each direction

def find_shortest_path(start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            return path
        for next_pos, jumps in generate_next_positions(pos, len(path) - 1):
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))

start, end = (10, 10), (2, 1)
print(find_shortest_path(start, end))
