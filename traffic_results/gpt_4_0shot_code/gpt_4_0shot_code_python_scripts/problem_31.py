
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
    [10, 'x', 19, 11, 'x', 'x', 6, 12, 'x', 'x', 'x'],
    [2, 9, 10, 'x', 'x', 10, 17, 'x', 'x', 11, 5],
    ['x', 15, 8, 9, 'x', 7, 17, 20, 'x', 'x', 13],
    [1, 9, 15, 14, 9, 9, 13, 7, 12, 'x', 10],
    [9, 'x', 17, 'x', 'x', 7, 'x', 'x', 1, 'x', 14],
    [16, 18, 11, 'x', 14, 18, 9, 13, 'x', 'x', 'x'],
    [9, 3, 5, 8, 17, 15, 19, 'x', 3, 'x', 14],
    [2, 13, 'x', 'x', 17, 13, 14, 18, 9, 'x', 6],
    [3, 'x', 18, 6, 'x', 14, 'x', 'x', 'x', 8, 19],
    [2, 4, 'x', 'x', 'x', 'x', 3, 4, 'x', 19, 'x'],
    ['x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 5, 5]
]

start = (3, 7)
end = (7, 0)
path = bfs(matrix, start, end)
print(path)
