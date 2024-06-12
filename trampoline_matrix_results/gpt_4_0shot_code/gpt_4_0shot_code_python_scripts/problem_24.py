
# Define the map of the park
park_map = [
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 0]
]

# Define the start and end positions
start = (9, 9)
end = (4, 1)

# Define the possible moves
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define a function to check if a position is valid
def is_valid(pos):
    x, y = pos
    return 0 <= x < 10 and 0 <= y < 10 and park_map[x][y] == 0

# Define a function to find the shortest path
def find_path(pos, end, path, jumps):
    if jumps < 0 or not is_valid(pos):
        return None
    path = path + [pos]
    if pos == end:
        return path if jumps == 0 else None
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        new_path = find_path(new_pos, end, path, jumps - 1)
        if new_path is not None:
            return new_path
    return None

# Find the shortest path
path = find_path(start, end, [], 3)
print(path)
