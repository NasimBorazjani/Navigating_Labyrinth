
# Define the trampoline park
park = [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0]
]

# Define the start and end positions
start = (1, 8)
end = (10, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Define a function to check if a position is valid
def is_valid(pos):
    x, y = pos
    return 0 <= x < 13 and 0 <= y < 13 and park[x][y] == 0

# Define a function to find the path
def find_path(pos, end, path, jumps):
    if jumps > 4 or not is_valid(pos):
        return None
    path.append(pos)
    if pos == end and jumps == 4:
        return path
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        result = find_path(new_pos, end, path, jumps + 1)
        if result:
            return result
    path.pop()
    return None

# Find the path
path = find_path(start, end, [], 0)
print(path)
