
from collections import deque

def bfs(matrix, start, end):
    queue = deque([(start, [start], 0, {get_district(start)} )])
    visited = set()
    while queue:
        (x, y), path, time, districts = queue.popleft()
        if (x, y) == end and len(districts) == 3:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != 'x' and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)], time + matrix[nx][ny], districts | {get_district((nx, ny))}))
                visited.add((nx, ny))
    return None

def get_district(pos):
    x, y = pos
    if 0 <= x <= 3:
        return 1
    elif x == 4:
        return 2
    else:
        return 3

matrix = [
    [19, 7, 11, 'x', 3, 18, 8, 'x', 'x', 'x', 'x'],
    [12, 18, 6, 1, 13, 12, 14, 11, 13, 5, 19],
    [11, 10, 10, 18, 15, 'x', 12, 'x', 4, 17, 10],
    [4, 3, 3, 7, 'x', 19, 'x', 'x', 'x', 12, 9],
    ['x', 'x', 6, 19, 'x', 4, 14, 'x', 9, 4, 15],
    [4, 7, 6, 5, 8, 'x', 15, 3, 'x', 16, 3],
    [13, 'x', 'x', 1, 9, 1, 9, 'x', 'x', 'x', 'x'],
    [2, 13, 5, 9, 5, 'x', 6, 'x', 18, 'x', 3],
    [19, 'x', 2, 9, 4, 13, 'x', 'x', 'x', 16, 6],
    ['x', 'x', 'x', 12, 'x', 7, 9, 3, 9, 8, 1],
    ['x', 10, 'x', 12, 3, 6, 'x', 4, 12, 4, 'x']
]

start = (5, 10)
end = (3, 0)
print(bfs(matrix, start, end))
