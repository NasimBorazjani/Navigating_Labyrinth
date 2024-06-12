
from collections import deque

# Define the grid
grid = [
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
]

# Define the start and end points
start = (0, 11)
end = (7, 1)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Define the BFS function
def bfs(start, end, grid):
    queue = deque([(start, [start], 0)])
    visited = set([start])
    while queue:
        (x, y), path, count = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])) and grid[nx][ny] == 0:
                if (nx, ny) == end and count == 3:
                    return path + [(nx, ny)]
                elif (nx, ny) not in visited and count < 4:
                    queue.append(((nx, ny), path + [(nx, ny)], count + 1))
                    visited.add((nx, ny))
    return None

# Print the shortest path
print(bfs(start, end, grid))
