
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    visited = set([start])
    while queue:
        path, dist = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in visited):
                queue.append((path + [(nx, ny)], dist + matrix[nx][ny]))
                visited.add((nx, ny))

matrix = [
    [4, 13, 'x', 9, 'x', 'x', 'x', 'x', 'x'],
    [1, 11, 'x', 16, 5, 7, 12, 16, 'x'],
    [12, 11, 'x', 14, 'x', 'x', 12, 'x', 3],
    [9, 11, 'x', 9, 10, 'x', 8, 'x', 'x'],
    [20, 2, 'x', 1, 16, 12, 18, 17, 10],
    [10, 13, 4, 15, 13, 2, 20, 3, 15],
    ['x', 6, 13, 1, 8, 20, 14, 11, 3],
    [14, 'x', 9, 'x', 'x', 13, 19, 10, 'x'],
    [12, 'x', 18, 1, 'x', 'x', 9, 'x', 'x']
]

start = (3, 1)
end = (5, 8)

print(bfs(matrix, start, end))
