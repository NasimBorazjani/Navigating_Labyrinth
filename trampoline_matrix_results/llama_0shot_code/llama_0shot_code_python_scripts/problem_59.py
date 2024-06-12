
from collections import deque

def get_neighbors(position, grid):
    row, col = position
    neighbors = []
    for r, c in [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]:
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
            neighbors.append((r, c))
    return neighbors

def is_valid(position, grid, visited, diagonals):
    row, col = position
    if position in visited:
        return False
    if grid[row][col] == 1:
        return False
    diagonal_count = 0
    for r, c in [(row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]:
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
            diagonal_count += 1
    if diagonal_count != diagonals:
        return False
    return True

def bfs(start, destination, grid, diagonals):
    queue = deque([(start, None)])
    visited = set([start])
    while queue:
        position, parent = queue.popleft()
        if position == destination:
            path = []
            while parent is not None:
                path.append(parent)
                position, parent = visited[parent]
            path.append(start)
            path.reverse()
            return path
        for neighbor in get_neighbors(position, grid):
            if is_valid(neighbor, grid, visited, diagonals):
                queue.append((neighbor, position))
                visited.add(neighbor)
    return None

grid = [
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

start = (0, 9)
destination = (11, 2)
diagonals = 4

path = bfs(start, destination, grid, diagonals)
print(path)
