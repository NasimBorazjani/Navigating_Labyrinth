
from collections import deque

def is_valid(grid, row, col, end_row, end_col, visited, moves):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return False
    if grid[row][col] == 1:
        return False
    if (row, col) == (end_row, end_col):
        return True
    if moves == 0:
        return False
    if visited[row][col]:
        return False
    return True

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start, [], 4)])
    while queue:
        (row, col), path, moves = queue.popleft()
        if (row, col) == end:
            return path + [(row, col)]
        for dr, dc in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
            new_row, new_col = row + dr, col + dc
            if is_valid(grid, new_row, new_col, end[0], end[1], visited, moves-1):
                visited[new_row][new_col] = True
                queue.append(((new_row, new_col), path + [(row, col)], moves-1))
    return []

grid = [
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

start, end = (8, 12), (1, 1)
print(shortest_path(grid, start, end))
