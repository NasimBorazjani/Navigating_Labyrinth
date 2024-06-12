
from collections import deque

map = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
]

def is_valid(x, y, visited):
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and map[x][y] == 0 and not visited[x][y]

def bfs(start, end, diagonals):
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        x, y = pos := queue.popleft()
        if pos == end:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            for _ in range(diagonals):
                x, y = x + dx, y + dy
                if is_valid(x, y, visited):
                    visited[x][y] = True
                    queue.append(((x, y), path + [(x, y)]))
                else:
                    break
            else:
                continue
            break
    return []

start, end = (0, 9), (10, 0)
path = bfs(start, end, 4)
print(path)
