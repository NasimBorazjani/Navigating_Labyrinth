
# Define the grid
grid = [
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
]

# Define the start and end positions
start = (11, 1)
end = (2, 12)

# Define the possible moves
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Initialize the stack with the start position
stack = [(start, [start])]

while stack:
    (vertex, path) = stack.pop()
    for next in (vertex[0] + move[0], vertex[1] + move[1]) for move in moves:
        if (0 <= next[0] < 15 and 0 <= next[1] < 15 and grid[next[0]][next[1]] == 0):
            if next == end and len(path) == 6:
                print(path + [next])
            else:
                stack.append((next, path + [next]))
