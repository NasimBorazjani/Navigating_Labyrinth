
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]
]

# Define the starting and ending points
start = (0, 3)
end = (14, 11)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue for the BFS
queue = deque([(start, [start], 0)])

while queue:
    # Pop the next node from the queue
    node, path, diagonals = queue.popleft()

    # If we've reached the end, print the path and exit
    if node == end and diagonals == 5:
        print(path)
        break

    # Add all possible next nodes to the queue
    for move in moves:
        next_node = (node[0] + move[0], node[1] + move[1])
        if (0 <= next_node[0] < 15 and 0 <= next_node[1] < 15 and
            park[next_node[0]][next_node[1]] == 0 and
            next_node not in path):
            next_diagonals = diagonals + 1 if move in moves[:4] else diagonals
            queue.append((next_node, path + [next_node], next_diagonals))
