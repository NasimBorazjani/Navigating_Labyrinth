
from collections import deque

def bfs(matrix, start, end):
    queue = deque([(start, [start], set())])
    while queue:
        (x, y), path, districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != 'x':
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                else:
                    new_districts = districts.copy()
                    if nx < 2:
                        new_districts.add(1)
                    elif nx < 6:
                        new_districts.add(2)
                    else:
                        new_districts.add(3)
                    if len(new_districts) < 3:
                        continue
                    queue.append(((nx, ny), path + [(nx, ny)], new_districts))
    return None

matrix = [
    [17, 'x', 'x', 'x', 5, 'x', 'x', 12, 16, 'x', 'x', 5, 16],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 12, 4, 6],
    [9, 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 13, 6, 11, 19],
    [1, 'x', 'x', 'x', 13, 'x', 'x', 'x', 3, 2, 7, 4, 3],
    ['x', 'x', 'x', 14, 19, 20, 10, 13, 14, 2, 'x', 9, 3],
    [15, 'x', 11, 7, 'x', 11, 6, 16, 'x', 'x', 'x', 8, 19],
    [19, 16, 4, 8, 5, 5, 5, 11, 10, 17, 9, 'x', 5],
    ['x', 3, 17, 'x', 'x', 6, 17, 19, 'x', 'x', 14, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 14, 'x', 10, 14, 13, 'x', 13, 'x'],
    [15, 5, 4, 'x', 'x', 'x', 'x', 2, 12, 6, 'x', 16, 14],
    [10, 'x', 'x', 'x', 9, 'x', 'x', 'x', 'x', 'x', 13, 2, 'x'],
    ['x', 'x', 17, 'x', 'x', 'x', 'x', 7, 'x', 'x', 16, 'x', 'x'],
    [12, 10, 'x', 15, 16, 'x', 'x', 7, 11, 7, 'x', 17, 'x']
]

start = (1, 12)
end = (6, 3)
print(bfs(matrix, start, end))
