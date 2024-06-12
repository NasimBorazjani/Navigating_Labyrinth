
from collections import deque

# Grid of the trampoline park
grid = [
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
]

def is_valid(x, y, dx, dy, visited):
    # Check if the move is within the grid
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False

    # Check if the trampoline is broken
    if grid[x][y] == 1:
        return False

    # Check if the move is diagonal
    if dx != 0 and dy != 0:
        return True

    # Check if the move has already been visited
    if (x, y) in visited:
        return False

    return True

def bfs(start, end):
    # Initialize the queue with the starting position
    queue = deque([(start, [start])])

    # Initialize the set of visited positions
    visited = set([start])

    while queue:
        # Dequeue a position from the queue
        (x, y), path = queue.popleft()

        # If this is the destination, return the path
        if (x, y) == end:
            return path

        # Check all possible moves
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, dx, dy, visited):
                # Mark this position as visited
                visited.add((nx, ny))

                # Enqueue this position with the current path
                queue.append(((nx, ny), path + [(nx, ny)]))

# Call the function and print the result
start, end = (8, 1), (1, 11)
path = bfs(start, end)
print(path)
