
from collections import deque

map_data = [
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
]

def is_valid(x, y, visited):
    return 0 <= x < len(map_data) and 0 <= y < len(map_data[0]) and map_data[x][y] == 0 and (x, y) not in visited

def bfs(start, end):
    queue = deque([(start, None)])
    visited = set([start])
    while queue:
        point, parent = queue.popleft()
        if point == end:
            path = []
            while parent is not None:
                path.append(parent)
                point, parent = parent
            return path[::-1]
        for i, j in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
            next_point = (point[0] + i, point[1] + j)
            if is_valid(next_point[0], next_point[1], visited):
                queue.append((next_point, point))
                visited.add(next_point)

print(bfs((0, 1), (6, 9)))
