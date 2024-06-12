
from collections import deque

map_data = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
]

def is_valid(x, y, visited, diagonal_moves):
    if x < 0 or y < 0 or x >= len(map_data) or y >= len(map_data[0]):
        return False
    if map_data[x][y] == 1 or visited[x][y]:
        return False
    if x != 0 and y != 0 and x != len(map_data)-1 and y != len(map_data[0])-1:
        if abs(x-y) == abs(x+y-13):
            diagonal_moves += 1
        if diagonal_moves > 4:
            return False
    return True

def bfs(start, end, diagonal_moves):
    visited = [[False]*len(map_data[0]) for _ in range(len(map_data))]
    queue = deque([(start, [start], diagonal_moves)])
    while queue:
        x, y, path, diagonal_moves = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited, diagonal_moves):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)], diagonal_moves))

path = bfs((0, 4), (13, 12), 0)
print(path)
