
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

matrix = [
    [8, 15, 3, 10, 6, 15, 'x', 4, 'x', 'x', 'x', 'x', 'x', 4],
    [3, 'x', 14, 8, 16, 19, 'x', 18, 4, 'x', 2, 'x', 6, 'x'],
    [18, 18, 'x', 4, 'x', 17, 11, 10, 17, 9, 'x', 4, 1, 5],
    ['x', 2, 'x', 12, 1, 'x', 13, 17, 14, 15, 17, 'x', 15, 'x'],
    ['x', 'x', 'x', 15, 'x', 2, 2, 11, 7, 'x', 5, 7, 4, 18],
    [16, 'x', 5, 'x', 19, 12, 5, 9, 13, 16, 9, 'x', 3, 'x'],
    ['x', 'x', 'x', 'x', 14, 18, 'x', 16, 13, 'x', 1, 5, 10, 'x'],
    [3, 11, 'x', 1, 8, 'x', 'x', 'x', 18, 8, 11, 'x', 'x', 6],
    [19, 2, 'x', 19, 5, 'x', 'x', 'x', 9, 'x', 6, 'x', 'x', 4],
    ['x', 2, 'x', 10, 9, 15, 'x', 'x', 'x', 16, 'x', 8, 'x', 'x'],
    [18, 8, 10, 'x', 3, 'x', 11, 'x', 17, 'x', 17, 'x', 'x', 'x'],
    [14, 12, 'x', 2, 'x', 19, 2, 19, 14, 'x', 'x', 'x', 3, 'x'],
    [7, 'x', 'x', 'x', 'x', 'x', 'x', 9, 8, 7, 'x', 15, 2, 'x'],
    ['x', 'x', 15, 'x', 'x', 15, 16, 'x', 'x', 'x', 19, 'x', 13, 1]
]

start = (2, 0)
end = (6, 11)
print(bfs(matrix, start, end))
