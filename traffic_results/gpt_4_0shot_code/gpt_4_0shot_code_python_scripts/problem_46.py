
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    visited = set([start])
    while queue:
        path, cost = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in visited):
                queue.append((path + [(nx, ny)], cost + matrix[nx][ny]))
                visited.add((nx, ny))
    return None

matrix = [
    [3, 14, 2, 'x', 'x', 'x', 19, 13, 17, 12, 8, 'x'],
    [1, 2, 13, 1, 4, 19, 'x', 'x', 16, 'x', 'x', 12],
    [9, 8, 9, 15, 'x', 12, 'x', 'x', 'x', 'x', 'x', 14],
    [11, 1, 10, 18, 'x', 16, 1, 'x', 12, 'x', 'x', 'x'],
    [7, 16, 13, 10, 13, 'x', 14, 'x', 'x', 9, 'x', 7],
    [19, 7, 7, 20, 13, 14, 18, 'x', 'x', 7, 5, 'x'],
    [4, 'x', 11, 'x', 'x', 2, 7, 1, 5, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 1, 'x'],
    [4, 'x', 'x', 9, 19, 2, 18, 8, 16, 14, 19, 7],
    ['x', 'x', 'x', 'x', 9, 'x', 17, 17, 1, 2, 2, 15],
    [18, 'x', 'x', 'x', 'x', 'x', 'x', 11, 10, 'x', 17, 'x'],
    [9, 'x', 'x', 'x', 10, 3, 'x', 'x', 13, 'x', 2, 'x']
]

start = (1, 0)
end = (8, 10)
path = bfs(matrix, start, end)
print(path)
