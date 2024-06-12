
from collections import deque

def is_valid(pos, grid, visited):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1 and not visited[x][y]

def get_neighbors(pos):
    x, y = pos
    return [(x+dx, y+dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]

def find_path(grid, start, dest):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [])])
    while queue:
        pos, sequence = queue.popleft()
        if pos == dest:
            return [(pos[0]-i%2, pos[1]-i//2) for i in range(len(sequence), -1, -1)]
        for dx, dy in get_neighbors(pos):
            if abs(pos[0]-dx) + abs(pos[1]-dy) == 1:
                continue
            if is_valid((dx, dy), grid, visited):
                visited[dx][dy] = True
                queue.append(((dx, dy), [pos[0]-dx, pos[1]-dy] + sequence))
    return []

grid = [
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
]

start = (14, 13)
dest = (2, 5)
print(find_path(grid, start, dest))
