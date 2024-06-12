
from collections import deque

def bfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start, [start], 0, {1, 2, 3})])
    while queue:
        (x, y), path, time, districts = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] != 'x':
                visited[nx][ny] = True
                new_time = time + matrix[nx][ny]
                new_path = path + [(nx, ny)]
                new_districts = districts - {get_district(nx)}
                if not new_districts:
                    queue.append(((nx, ny), new_path, new_time, new_districts))
    return None

def get_district(row):
    if row <= 1:
        return 1
    elif row <= 5:
        return 2
    else:
        return 3

matrix = [
    [13, 'x', 10, 17, 'x', 4, 8, 'x', 7, 'x', 12, 19, 4],
    [17, 'x', 8, 11, 7, 'x', 'x', 19, 'x', 11, 'x', 13, 18],
    [15, 6, 2, 12, 16, 7, 'x', 14, 'x', 2, 'x', 14, 4],
    ['x', 18, 4, 'x', 'x', 'x', 13, 14, 2, 4, 20, 10, 7],
    [7, 2, 19, 16, 'x', 'x', 'x', 18, 'x', 'x', 'x', 2, 2],
    [10, 17, 14, 7, 17, 3, 3, 19, 'x', 19, 'x', 'x', 9],
    [9, 'x', 'x', 'x', 5, 18, 13, 6, 'x', 'x', 'x', 19, 10],
    ['x', 'x', 'x', 'x', 'x', 2, 7, 4, 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 6, 3, 'x', 1, 'x', 'x', 14, 'x', 18, 'x', 1],
    [14, 'x', 4, 18, 14, 12, 'x', 'x', 'x', 'x', 2, 'x', 13],
    [12, 'x', 3, 1, 12, 9, 'x', 6, 'x', 'x', 16, 'x', 18],
    [13, 'x', 11, 5, 3, 4, 'x', 'x', 'x', 'x', 'x', 'x', 18],
    [15, 9, 9, 1, 'x', 6, 'x', 'x', 14, 'x', 'x', 1, 14]
]

start = (5, 1)
end = (2, 11)
print(bfs(matrix, start, end))
