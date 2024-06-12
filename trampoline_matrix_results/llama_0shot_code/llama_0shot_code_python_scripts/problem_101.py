
from collections import deque

def is_valid(pos, visited, grid):
    x, y = pos
    return (0 <= x < len(grid) and 0 <= y < len(grid[0]) and 
            grid[x][y] != 1 and pos not in visited)

def get_neighbors(pos):
    x, y = pos
    return [(x+dx, y+dy) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]]

def find_path(grid):
    start, dest = (0, 3), (14, 11)
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        pos, path = queue.popleft()
        if pos == dest:
            return path[1:]    # Exclude the starting position
        for neighbor in get_neighbors(pos):
            if neighbor not in visited and len(path) - 1 == neighbor[0] - start[0] + neighbor[1] - start[1]:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

grid = [
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    # ...
    [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
]

print(find_path(grid))
