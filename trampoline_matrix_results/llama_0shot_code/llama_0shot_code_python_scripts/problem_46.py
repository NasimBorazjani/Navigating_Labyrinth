
from collections import deque

def is_valid(pos, jumps):
    x, y = pos
    return 0 <= x < 12 and 0 <= y < 12 and grid[x][y] == 0 and (abs(x - 1) + abs(y - 0) == 4 + len(jumps) * 2)

grid = [
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
]

start, end = (1, 0), (7, 11)
queue = deque([(start, [start])])
while queue:
    pos, jumps = queue.popleft()
    if pos == end:
        print(jumps)
        break
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (0, -2), (0, 2), (2, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]:
        next_pos = (pos[0] + dx, pos[1] + dy)
        if is_valid(next_pos, jumps):
            queue.append((next_pos, jumps + [next_pos]))
else:
    print("No solution found")
