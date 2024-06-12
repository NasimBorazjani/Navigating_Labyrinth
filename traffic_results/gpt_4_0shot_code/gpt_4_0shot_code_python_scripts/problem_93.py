
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
    ['x', 'x', 'x', 'x', 2, 19, 'x', 'x', 15, 'x', 'x', 2, 17, 18, 18],
    ['x', 'x', 2, 18, 3, 17, 1, 'x', 'x', 'x', 6, 'x', 'x', 7, 9],
    ['x', 'x', 2, 10, 3, 'x', 6, 11, 5, 7, 8, 17, 'x', 12, 6],
    ['x', 14, 13, 9, 3, 'x', 18, 'x', 17, 16, 14, 8, 9, 'x', 13],
    ['x', 'x', 'x', 17, 'x', 16, 9, 3, 1, 'x', 5, 20, 2, 2, 6],
    [8, 'x', 8, 'x', 5, 19, 12, 19, 7, 1, 5, 4, 11, 13, 16],
    ['x', 6, 19, 17, 20, 'x', 'x', 14, 14, 'x', 'x', 3, 20, 13, 3],
    [12, 14, 7, 1, 15, 'x', 8, 8, 'x', 'x', 'x', 15, 'x', 'x', 'x'],
    ['x', 9, 'x', 'x', 4, 7, 7, 'x', 'x', 13, 7, 7, 'x', 6, 'x'],
    ['x', 'x', 'x', 11, 10, 'x', 'x', 'x', 5, 'x', 7, 14, 'x', 19, 'x'],
    ['x', 11, 18, 'x', 19, 'x', 1, 18, 1, 8, 'x', 'x', 'x', 12, 15],
    [19, 'x', 7, 'x', 9, 3, 'x', 7, 12, 13, 19, 13, 'x', 9, 'x'],
    ['x', 17, 9, 'x', 6, 'x', 6, 'x', 'x', 11, 'x', 19, 'x', 'x', 'x'],
    [4, 17, 5, 'x', 7, 5, 17, 12, 'x', 16, 8, 'x', 'x', 17, 'x'],
    [15, 2, 13, 'x', 14, 'x', 'x', 17, 'x', 'x', 1, 'x', 19, 1, 17]
]

start = (4, 14)
end = (7, 1)
path = bfs(matrix, start, end)
print(path)
