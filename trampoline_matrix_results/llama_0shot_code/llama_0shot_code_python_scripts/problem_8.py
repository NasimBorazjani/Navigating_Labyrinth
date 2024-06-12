
from collections import deque

grid = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1]
]

def is_valid(x, y, px, py):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (abs(x - px) + abs(y - py)) != 3

def bfs(start, end):
    queue = deque([(start, None)])
    prev = {start: None}
    while queue:
        x, y = pos = queue.popleft()
        if pos == end:
            path = []
            while pos is not None:
                path.append(pos)
                pos = prev[pos]
            return path[::-1]
        for x, y in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if is_valid(x, y, pos[0], pos[1]):
                queue.append(((x, y), pos))
                if (x, y) not in prev:
                    prev[(x, y)] = pos

start, end = (0, 8), (8, 3)
path = bfs(start, end)
print(path)
