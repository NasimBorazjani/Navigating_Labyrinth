
from collections import deque

def get_neighbors(pos, grid):
    x, y = pos
    neighbors = [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    valid_neighbors = [n for n in neighbors if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] == 0 and n != pos]
    return valid_neighbors

def is_valid(pos, grid, visited):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == 0 and pos not in visited

def bfs(start, destination, grid):
    queue = deque([(start, [], 0)])
    visited = set([start])
    while queue:
        pos, path, diagonal_jumps = queue.popleft()
        if pos == destination:
            return path, diagonal_jumps
        for neighbor in get_neighbors(pos, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                new_diagonal_jumps = diagonal_jumps + (abs(pos[0] - neighbor[0]) != abs(pos[1] - neighbor[1]))
                if len(new_path) <= 8 and new_diagonal_jumps <= 3:
                    queue.append((neighbor, new_path, new_diagonal_jumps))
    return None

def solve_puzzle(start, destination, grid):
    path, _ = bfs(start, destination, grid)
    return path[::-1]

grid = [
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]

start = (8, 2)
destination = (1, 8)

print(solve_puzzle(start, destination, grid))
