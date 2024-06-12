
from collections import deque

# Define the grid
grid = [
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
]

# Define the start and end points
start = (11, 8)
end = (1, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the start point
queue = deque([(start, [start], 0)])

# While there are nodes to visit
while queue:
    # Get the current node and path
    node, path, jumps = queue.popleft()

    # If this is the end node
    if node == end and jumps == 4:
        # Print the path and stop
        print(path)
        break

    # For each possible move
    for dx, dy in moves:
        # Calculate the new position
        x, y = node[0] + dx, node[1] + dy

        # If the new position is valid
        if 0 <= x < 13 and 0 <= y < 13 and grid[x][y] == 0 and (x, y) not in path:
            # Add the new position to the queue
            queue.append(((x, y), path + [(x, y)], jumps + 1))
