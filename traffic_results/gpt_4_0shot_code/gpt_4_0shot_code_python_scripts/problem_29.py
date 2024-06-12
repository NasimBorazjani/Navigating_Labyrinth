
from collections import deque

def bfs(matrix, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in visited):
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

matrix = [
    ['x', 'x', 'x', 4, 6, 'x', 9, 15, 11, 2],
    [19, 'x', 14, 3, 10, 18, 'x', 'x', 'x', 1],
    ['x', 9, 'x', 11, 7, 14, 'x', 'x', 16, 18],
    ['x', 5, 4, 5, 2, 4, 7, 5, 19, 14],
    ['x', 3, 20, 'x', 5, 16, 'x', 'x', 1, 9],
    ['x', 3, 15, 9, 4, 'x', 'x', 'x', 'x', 4],
    [11, 18, 19, 8, 17, 9, 'x', 10, 10, 19],
    ['x', 'x', 'x', 17, 7, 'x', 'x', 7, 12, 8],
    ['x', 'x', 11, 19, 'x', 13, 10, 13, 'x', 'x'],
    [18, 'x', 'x', 'x', 6, 10, 7, 'x', 8, 'x']
]

start = (3, 9)
end = (6, 1)
path = bfs(matrix, start, end)
print(path)
