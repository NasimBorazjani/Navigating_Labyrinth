
from collections import deque

# Define the grid
grid = [
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0]
]

# Define the start and end points
start = (0, 4)
end = (9, 8)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Define the BFS function
def bfs(start, end, grid):
    queue = deque([(start, [start])])
    seen = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and
                grid[nx][ny] == 0 and (nx, ny) not in seen):
                if (nx, ny) == end and len(path) == 3:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                seen.add((nx, ny))
    return None

# Print the shortest path
print(bfs(start, end, grid))
