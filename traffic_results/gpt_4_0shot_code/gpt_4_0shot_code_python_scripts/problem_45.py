
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    seen = set([start])
    while queue:
        (path, length) = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in seen):
                queue.append((path + [(nx, ny)], length + matrix[nx][ny]))
                seen.add((nx, ny))

matrix = [
    ['x', 'x', 17, 12, 12, 10, 9, 9, 18, 'x', 1],
    ['x', 8, 'x', 9, 'x', 'x', 18, 5, 1, 12, 14],
    [2, 19, 4, 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x'],
    [17, 8, 6, 'x', 'x', 10, 15, 'x', 'x', 'x', 13],
    ['x', 'x', 'x', 9, 17, 'x', 'x', 'x', 'x', 12, 17],
    ['x', 20, 3, 1, 14, 8, 9, 20, 10, 8, 8],
    [18, 19, 4, 12, 3, 1, 'x', 'x', 20, 6, 3],
    [4, 6, 9, 'x', 8, 10, 'x', 'x', 6, 9, 6],
    [15, 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 4, 'x'],
    ['x', 'x', 'x', 4, 'x', 'x', 'x', 13, 'x', 'x', 'x'],
    ['x', 3, 'x', 'x', 'x', 'x', 1, 'x', 'x', 5, 13]
]

start = (3, 10)
end = (6, 1)
print(bfs(matrix, start, end))
