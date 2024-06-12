
from collections import deque

# Define the grid
grid = [
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
]

# Define the start and end points
start = (8, 6)
end = (0, 1)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the start point
queue = deque([(start, [start])])

while queue:
    # Pop the next node from the queue
    node, path = queue.popleft()

    # If this node is the end point, print the path and exit
    if node == end:
        print(path)
        break

    # Add all reachable nodes to the queue
    for move in moves:
        next_node = (node[0] + move[0], node[1] + move[1])
        if (0 <= next_node[0] < 10 and 0 <= next_node[1] < 10 and
                grid[next_node[0]][next_node[1]] == 0):
            queue.append((next_node, path + [next_node]))
            grid[next_node[0]][next_node[1]] = 1  # Mark as visited
