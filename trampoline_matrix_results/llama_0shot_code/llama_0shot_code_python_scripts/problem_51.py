
from collections import deque

# Grid map of the trampoline park
grid = [
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]

def is_valid(x, y, visited):
    # Check if the trampoline is within the grid, not broken, and not visited
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (x, y) not in visited

def bfs(start, end):
    # Create a visited dictionary to mark trampolines as visited using their coordinates as keys
    visited = {start: None}

    # Create a queue for BFS and enqueue the first trampoline
    queue = deque([start])

    # Define the eight possible movements from a trampoline
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Keep track of the number of diagonal jumps
    diagonal_jumps = {start: 0}

    while queue:
        x, y = queue.popleft()

        # If the current trampoline is the destination, return the path
        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = visited[(x, y)]
            return path[::-1]

        # Check the eight possible movements from the current trampoline
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # If the movement is diagonal and within the allowed number of jumps, update the number of jumps
            if (dx, dy) in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if diagonal_jumps[x, y] + 1 <= 4:
                    if is_valid(nx, ny, visited):
                        visited[(nx, ny)] = (x, y)
                        diagonal_jumps[(nx, ny)] = diagonal_jumps[x, y] + 1
                        queue.append((nx, ny))

            # If the movement is not diagonal, update the number of jumps to zero
            else:
                if is_valid(nx, ny, visited):
                    visited[(nx, ny)] = (x, y)
                    diagonal_jumps[(nx, ny)] = 0
                    queue.append((nx, ny))

    # If there is no path to the destination, return an empty list
    return []

# Test the function with the given start and end positions
start = (1, 11)
end = (11, 3)
print(bfs(start, end))
