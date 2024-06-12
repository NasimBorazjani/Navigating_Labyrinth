
from collections import deque

def bfs(matrix, start, end):
    queue = deque([(start, [start], {get_district(start)} )])
    while queue:
        (x, y), path, districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != 'x':
                if (nx, ny) == end and len(districts | {get_district((nx, ny))}) == 3:
                    return path + [(nx, ny)]
                else:
                    queue.append(((nx, ny), path + [(nx, ny)], districts | {get_district((nx, ny))}))
    return []

def get_district(position):
    x, y = position
    if 0 <= x <= 3:
        return 1
    elif 4 <= x <= 6:
        return 2
    elif 7 <= x <= 11:
        return 3

matrix = [
    [12, 17, 10, 'x', 'x', 'x', 'x', 9, 15, 5, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 12, 20, 9, 19, 8, 12, 11],
    [9, 'x', 'x', 2, 'x', 2, 1, 9, 8, 14, 16, 'x'],
    [19, 'x', 1, 20, 7, 9, 18, 'x', 18, 7, 'x', 'x'],
    [5, 2, 11, 9, 'x', 5, 4, 16, 'x', 1, 'x', 10],
    [10, 8, 8, 4, 11, 11, 'x', 'x', 5, 'x', 'x', 'x'],
    [15, 15, 'x', 'x', 13, 5, 19, 'x', 'x', 15, 'x', 'x'],
    [15, 16, 9, 18, 'x', 'x', 16, 'x', 'x', 'x', 5, 12],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 14, 14, 'x', 'x', 15, 6, 6, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 8, 14, 'x', 5, 'x', 'x', 15],
    ['x', 6, 15, 'x', 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x']
]

start = (3, 9)
end = (7, 1)
print(bfs(matrix, start, end))
