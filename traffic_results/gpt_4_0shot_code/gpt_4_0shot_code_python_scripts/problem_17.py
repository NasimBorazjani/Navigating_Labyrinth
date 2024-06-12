
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
            if (0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]
                    and matrix[nx][ny] != 'x'):
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited[nx][ny] = True
    return None

matrix = [
    [16, 2, 16, 'x', 4, 'x', 'x', 1, 16, 'x'],
    ['x', 'x', 19, 'x', 3, 'x', 5, 'x', 'x', 'x'],
    ['x', 'x', 'x', 3, 'x', 'x', 2, 'x', 10, 'x'],
    [11, 5, 20, 'x', 1, 3, 1, 'x', 9, 'x'],
    ['x', 'x', 8, 19, 'x', 16, 9, 'x', 16, 15],
    ['x', 3, 5, 10, 'x', 'x', 'x', 4, 1, 'x'],
    [9, 18, 10, 17, 5, 6, 'x', 'x', 'x', 5],
    ['x', 'x', 14, 5, 18, 'x', 'x', 1, 15, 1],
    [13, 'x', 13, 13, 14, 2, 19, 12, 'x', 1],
    [9, 6, 'x', 4, 12, 1, 13, 8, 2, 13]
]

start = (7, 9)
end = (3, 2)
path = bfs(matrix, start, end)
print(path)
