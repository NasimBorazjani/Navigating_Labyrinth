
from collections import deque

def is_valid(pos, visited):
    x, y = pos
    if x<0 or y<0 or x>=9 or y>=9 or graph[x][y]==1 or pos in visited:
        return False
    return True

def bfs():
    queue = deque([((8, 0), 0, [])])
    while queue:
        (x, y), diag, path = queue.popleft()
        if (x, y) == (2, 7) and diag == 3:
            return path + [(x, y)]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if is_valid((x+dx, y+dy), set(path)):
                queue.append(((x+dx, y+dy), diag+1, path + [(x, y)]))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if is_valid((x+dx, y+dy), set(path)):
                queue.append(((x+dx, y+dy), diag, path + [(x, y)]))
    return []

graph = [
    [0, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0]
]

print(bfs())
