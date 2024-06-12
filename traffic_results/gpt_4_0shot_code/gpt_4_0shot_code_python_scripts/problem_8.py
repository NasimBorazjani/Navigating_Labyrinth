
from collections import deque

def bfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end and set(i//3 for i, _ in path) == {0, 1, 2}:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] != 'x':
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited[nx][ny] = True

matrix = [
    ['x', 'x', 'x', 'x', 13, 'x', 'x', 3, 8],
    ['x', 18, 19, 19, 2, 9, 'x', 'x', 'x'],
    [15, 'x', 6, 'x', 'x', 'x', 13, 13, 4],
    [7, 'x', 4, 10, 'x', 11, 10, 17, 'x'],
    [2, 7, 'x', 'x', 8, 16, 4, 1, 4],
    ['x', 'x', 'x', 5, 16, 15, 'x', 17, 10],
    ['x', 'x', 'x', 5, 14, 9, 3, 15, 'x'],
    ['x', 6, 4, 'x', 'x', 'x', 18, 'x', 'x'],
    [17, 'x', 19, 'x', 1, 4, 8, 'x', 8]
]

start = (2, 8)
end = (6, 3)
print(bfs(matrix, start, end))
