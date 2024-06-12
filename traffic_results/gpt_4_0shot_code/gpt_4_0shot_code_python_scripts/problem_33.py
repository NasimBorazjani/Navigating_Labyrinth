
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
    [16, 10, 'x', 16, 1, 12, 6, 12, 3, 7, 'x'],
    ['x', 16, 10, 9, 12, 19, 7, 10, 12, 13, 7],
    [5, 'x', 9, 'x', 5, 16, 16, 8, 'x', 16, 8],
    ['x', 4, 14, 'x', 'x', 'x', 'x', 'x', 'x', 7, 18],
    [13, 12, 16, 14, 'x', 2, 4, 2, 'x', 6, 3],
    ['x', 11, 20, 'x', 'x', 'x', 1, 'x', 'x', 9, 'x'],
    ['x', 'x', 8, 10, 'x', 'x', 3, 1, 'x', 'x', 6],
    ['x', 2, 9, 'x', 8, 13, 'x', 'x', 'x', 12, 11],
    [12, 'x', 2, 'x', 'x', 1, 6, 'x', 15, 'x', 1],
    [3, 'x', 'x', 'x', 17, 'x', 18, 4, 1, 'x', 'x'],
    ['x', 'x', 6, 'x', 'x', 12, 'x', 'x', 'x', 15, 12]
]

start = (2, 10)
end = (5, 2)
print(bfs(matrix, start, end))
