
from collections import deque

# Define the trampoline park
park = [
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the starting and ending points
start = (4, 0)
end = (12, 12)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue for BFS
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next node from the queue
    node, jumps, path = queue.popleft()

    # If we've reached the end, print the path and exit
    if node == end and jumps == 4:
        print(path)
        break

    # Otherwise, add all possible next nodes to the queue
    for move in moves:
        next_node = (node[0] + move[0], node[1] + move[1])
        next_jumps = jumps + (move[0] != 0 and move[1] != 0)
        if (0 <= next_node[0] < 13 and 0 <= next_node[1] < 13 and
            park[next_node[0]][next_node[1]] == 0 and
            next_jumps <= 4):
            queue.append((next_node, next_jumps, path + [next_node]))
