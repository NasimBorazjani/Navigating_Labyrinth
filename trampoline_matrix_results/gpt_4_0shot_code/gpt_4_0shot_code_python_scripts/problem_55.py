
from collections import deque

# Define the grid
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
]

# Define the start and end points
start = (1, 11)
end = (9, 0)

# Define the possible moves
moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next point from the queue
    point, diagonals, path = queue.popleft()

    # If this point is the end point, return the path
    if point == end and diagonals == 4:
        print(path)
        break

    # Add all valid adjacent points to the queue
    for move in moves:
        next_point = (point[0] + move[0], point[1] + move[1])
        next_diagonals = diagonals + 1 if abs(move[0]) == abs(move[1]) else diagonals
        if (0 <= next_point[0] < 12 and 0 <= next_point[1] < 12 and
            grid[next_point[0]][next_point[1]] == 0 and
            next_diagonals <= 4):
            queue.append((next_point, next_diagonals, path + [next_point]))
