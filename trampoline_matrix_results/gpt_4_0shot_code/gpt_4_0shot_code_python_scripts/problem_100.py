
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]
]

# Define the starting and ending points
start = (2, 2)
end = (13, 14)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the starting point
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next point from the queue
    point, jumps, path = queue.popleft()

    # If we've reached the end, print the path and break
    if point == end and jumps == 5:
        print(path)
        break

    # Otherwise, add all possible next points to the queue
    for move in moves:
        next_point = (point[0] + move[0], point[1] + move[1])
        if (0 <= next_point[0] < 15 and 0 <= next_point[1] < 15 and
                park[next_point[0]][next_point[1]] == 0):
            queue.append((next_point, jumps + 1, path + [next_point]))
