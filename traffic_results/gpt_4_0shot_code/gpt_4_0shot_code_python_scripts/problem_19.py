
from collections import deque

def bfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start, [start])])
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] != 'x':
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited[nx][ny] = True

    return None

matrix = [
    ['x', 16, 15, 14, 2, 12, 3, 'x', 7, 7],
    [11, 'x', 'x', 'x', 4, 10, 5, 'x', 'x', 'x'],
    [12, 'x', 3, 'x', 'x', 19, 'x', 13, 'x', 'x'],
    [16, 15, 13, 'x', 12, 'x', 'x', 1, 'x', 7],
    [2, 6, 'x', 5, 'x', 14, 7, 'x', 8, 18],
    [19, 17, 2, 11, 8, 17, 12, 8, 9, 14],
    [11, 1, 10, 11, 'x', 'x', 19, 6, 2, 18],
    [7, 'x', 10, 15, 'x', 'x', 'x', 'x', 18, 17],
    ['x', 6, 'x', 'x', 'x', 5, 'x', 7, 12, 20],
    ['x', 'x', 2, 15, 'x', 17, 'x', 'x', 10, 11]
]

start = (5, 0)
end = (3, 9)
path = bfs(matrix, start, end)
print(path)
