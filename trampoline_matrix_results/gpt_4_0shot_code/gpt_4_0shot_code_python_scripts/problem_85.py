
from collections import deque

def shortest_path(grid, start, end):
    # Define the eight possible directions to move in the grid
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Create a queue for BFS and enqueue the start position
    queue = deque([(start, [start], 0)])
    # Create a set to store visited positions
    visited = set([start])
    while queue:
        # Dequeue a position from the queue
        (x, y), path, diagonals = queue.popleft()
        # If this is the end position, return the path to this position
        if (x, y) == end:
            return path
        # Enqueue all valid and unvisited neighboring positions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 14 and 0 <= ny < 14 and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_diagonals = diagonals + 1 if dx != 0 and dy != 0 else diagonals
                if new_diagonals <= 4:
                    queue.append(((nx, ny), path + [(nx, ny)], new_diagonals))
                    visited.add((nx, ny))
    # If there is no path to the end position, return an empty list
    return []

# Define the grid
grid = [
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1]
]

# Define the start and end positions
start = (1, 3)
end = (12, 11)

# Find the shortest path
path = shortest_path(grid, start, end)

# Print the path
print(path)
