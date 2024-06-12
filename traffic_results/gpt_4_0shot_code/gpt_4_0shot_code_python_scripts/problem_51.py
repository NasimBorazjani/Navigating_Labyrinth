
from collections import deque

def bfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] != 'x':
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited[nx][ny] = True
    return None

matrix = [
    [19, 12, 'x', 'x', 2, 5, 4, 13, 17, 19, 'x', 2],
    ['x', 18, 'x', 5, 5, 'x', 'x', 8, 12, 18, 'x', 15],
    ['x', 9, 4, 10, 7, 20, 'x', 16, 20, 13, 15, 'x'],
    [8, 'x', 'x', 11, 1, 19, 'x', 14, 6, 'x', 3, 'x'],
    [10, 'x', 4, 8, 17, 'x', 18, 'x', 7, 'x', 6, 5],
    ['x', 'x', 3, 1, 8, 18, 'x', 4, 17, 'x', 'x', 13],
    ['x', 'x', 6, 'x', 'x', 'x', 14, 'x', 'x', 10, 10, 'x'],
    ['x', 'x', 15, 'x', 'x', 'x', 'x', 'x', 2, 'x', 'x', 'x'],
    ['x', 'x', 5, 11, 6, 1, 'x', 6, 14, 'x', 'x', 'x'],
    ['x', 1, 17, 10, 15, 'x', 14, 6, 'x', 'x', 'x', 'x'],
    [12, 2, 'x', 10, 'x', 'x', 7, 'x', 'x', 'x', 'x', 'x'],
    ['x', 9, 14, 'x', 9, 18, 14, 'x', 'x', 'x', 6, 'x']
]

start = (6, 2)
end = (2, 10)
path = bfs(matrix, start, end)
print(path)
