
from collections import deque

def get_neighbors(position, grid):
    row, col = position
    neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1),
                 (row, col-1),                 (row, col+1),
                 (row+1, col-1), (row+1, col), (row+1, col+1)]
    valid_neighbors = []
    for neighbor in neighbors:
        r, c = neighbor
        if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and (grid[r][c] == 0) and (neighbor != position):
            valid_neighbors.append(neighbor)
    return valid_neighbors

def bfs(start, end, grid):
    queue = deque([start])
    previous_positions = {start: None}
    while queue:
        position = queue.popleft()
        if position == end:
            break
        for neighbor in get_neighbors(position, grid):
            if neighbor not in previous_positions:
                queue.append(neighbor)
                previous_positions[neighbor] = position
    path = []
    while end is not None:
        path.append(end)
        end = previous_positions[end]
    return path[::-1]

grid = [[1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1]]

start = (2, 11)
end = (8, 1)

path = bfs(start, end, grid)

print(path)
