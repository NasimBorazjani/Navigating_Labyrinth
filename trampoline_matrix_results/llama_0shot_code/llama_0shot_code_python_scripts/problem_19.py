
from collections import deque

def get_neighbors(pos, grid):
    x, y = pos
    neighbors = [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    valid_neighbors = [n for n in neighbors if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] == 0 and n != pos]
    return valid_neighbors

def is_valid(pos, grid, visited):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == 0 and pos not in visited

def bfs(start, dest, grid):
    queue = deque([(start, [], 0)])
    visited = set([start])
    while queue:
        pos, path, diagonal_jumps = queue.popleft()
        if pos == dest:
            return path, diagonal_jumps
        for n in get_neighbors(pos, grid):
            if n not in visited:
                visited.add(n)
                new_path = path + [n]
                new_diagonal_jumps = diagonal_jumps + (abs(n[0] - pos[0]) != abs(n[1] - pos[1]))
                if len(new_path) <= 8 and new_diagonal_jumps <= 3:
                    queue.append((n, new_path, new_diagonal_jumps))
    return None

def solve_puzzle(start, dest, grid):
    path, _ = bfs(start, dest, grid)
    return path[::-1]

grid = [
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
]

start = (1, 9)
dest = (7, 1)

print(solve_puzzle(start, dest, grid))
