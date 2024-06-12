
from collections import deque

def bfs(grid, start, end):
    num_rows, num_cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    queue = deque([(start, [start])])
    visited = {start: [start]}

    while queue:
        position, path = queue.popleft()
        if position == end:
            return path
        for direction in directions:
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if (0 <= next_position[0] < num_rows and 0 <= next_position[1] < num_cols and
                    grid[next_position[0]][next_position[1]] == 0 and
                    len(path) + 1 <= 4 + len(path) // 2):
                if next_position not in visited or len(visited[next_position]) > len(path) + 1:
                    queue.append((next_position, path + [next_position]))
                    visited[next_position] = path + [next_position]

    return []

grid = [[1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]]

start, end = (12, 0), (1, 6)
path = bfs(grid, start, end)
print(path)
