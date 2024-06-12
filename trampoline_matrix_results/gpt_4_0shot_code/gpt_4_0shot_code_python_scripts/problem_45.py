
from collections import deque

# Trampoline park map
park = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
]

# BFS algorithm
def bfs(start, end):
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 11 and 0 <= ny < 11 and park[nx][ny] == 0:
                if (nx, ny) == end and len(path) == 3:
                    return path + [(nx, ny)]
                else:
                    queue.append(((nx, ny), path + [(nx, ny)]))

# Start and end points
start = (1, 0)
end = (8, 9)

# Find shortest path
path = bfs(start, end)
print(path)
