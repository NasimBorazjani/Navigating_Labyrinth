
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    visited = set([start])
    while queue:
        path, length = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in visited):
                queue.append((path + [(nx, ny)], length + matrix[nx][ny]))
                visited.add((nx, ny))

matrix = [
    [2, 2, 3, 'x', 2, 10, 'x', 8, 6, 'x'],
    [6, 11, 'x', 'x', 'x', 'x', 'x', 16, 'x', 7],
    [17, 17, 7, 12, 13, 15, 5, 6, 10, 13],
    [1, 15, 13, 3, 'x', 'x', 'x', 14, 'x', 9],
    [14, 'x', 'x', 6, 15, 2, 12, 18, 'x', 18],
    [11, 19, 1, 19, 10, 8, 'x', 14, 'x', 'x'],
    [11, 'x', 'x', 'x', 3, 'x', 'x', 7, 'x', 2],
    [16, 12, 'x', 'x', 'x', 5, 'x', 'x', 10, 'x'],
    ['x', 11, 'x', 2, 12, 'x', 8, 'x', 8, 'x'],
    ['x', 'x', 16, 'x', 'x', 'x', 16, 'x', 16, 12]
]

start = (1, 0)
end = (5, 7)
print(bfs(matrix, start, end))
