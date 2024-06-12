
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
    [16, 'x', 5, 6, 'x', 14, 12, 'x', 'x', 'x', 6, 'x'],
    [17, 'x', 'x', 'x', 5, 'x', 5, 7, 'x', 'x', 8, 'x'],
    [3, 19, 'x', 'x', 'x', 'x', 18, 'x', 13, 7, 'x', 'x'],
    [13, 'x', 4, 'x', 'x', 8, 7, 4, 'x', 15, 'x', 'x'],
    [5, 17, 18, 12, 3, 'x', 14, 2, 4, 18, 'x', 1],
    [4, 10, 1, 19, 10, 'x', 'x', 17, 'x', 17, 16, 4],
    [7, 'x', 16, 'x', 'x', 1, 3, 'x', 13, 13, 'x', 'x'],
    ['x', 'x', 9, 1, 7, 18, 16, 3, 'x', 4, 'x', 'x'],
    [2, 'x', 13, 10, 'x', 4, 'x', 'x', 'x', 'x', 'x', 12],
    ['x', 'x', 'x', 18, 8, 4, 'x', 11, 'x', 14, 18, 'x'],
    ['x', 19, 2, 'x', 2, 6, 5, 18, 'x', 5, 'x', 'x'],
    ['x', 2, 'x', 7, 'x', 'x', 8, 7, 'x', 11, 16, 'x']
]

start = (3, 0)
end = (9, 7)
path = bfs(matrix, start, end)
print(path)
