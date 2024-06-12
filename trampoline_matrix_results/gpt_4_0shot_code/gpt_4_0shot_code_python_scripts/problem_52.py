
from collections import deque

# Define the trampoline park
park = [
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

# Define the starting and ending positions
start = (8, 1)
end = (1, 11)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue for the BFS
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next node from the queue
    node, jumps, path = queue.popleft()

    # If we have reached the end, print the path and exit
    if node == end and jumps == 4:
        print(path)
        break

    # If we have made too many jumps, skip this node
    if jumps > 4:
        continue

    # Add all possible next nodes to the queue
    for move in moves:
        next_node = (node[0] + move[0], node[1] + move[1])
        if (0 <= next_node[0] < 12 and 0 <= next_node[1] < 12 and
                park[next_node[0]][next_node[1]] == 0):
            queue.append((next_node, jumps + 1, path + [next_node]))
