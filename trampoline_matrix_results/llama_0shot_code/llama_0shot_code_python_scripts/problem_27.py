
# Map of the trampoline park
map = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
]

def is_valid(x, y, visited):
    # Check if the move is within the grid, it's not a broken trampoline,
    # and it's different from the current position
    return (0 <= x < len(map) and 0 <= y < len(map[0]) and
            map[x][y] != 1 and (x, y) != (current[0], current[1]) and (x, y) not in visited)

def bfs(start, dest, diag_jumps):
    # Initialize a queue with the start position and a dictionary to save the path
    queue = [(start, [])]
    visited = {start: []}

    while queue:
        current, path = queue.pop(0)
        path = path + [current]

        # Check if we have found the destination
        if current == dest:
            return path[1:]  # We return the path without the start position

        # Check if we can make a diagonal jump
        if diag_jumps > 0:
            for dx, dy in [(-2, 2), (-2, -2), (2, 2), (2, -2)]:
                x, y = current[0] + dx, current[1] + dy
                if is_valid(x, y, visited):
                    queue.append(((x, y), path))
                    visited[(x, y)] = path

        # Make the other possible jumps
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = current[0] + dx, current[1] + dy
            if is_valid(x, y, visited):
                queue.append(((x, y), path))
                visited[(x, y)] = path

    # If we have explored all possible moves and haven't found the destination,
    # there is no solution
    return None

# Test the function with the given problem
start = (7, 9)
dest = (3, 0)
diag_jumps = 3
solution = bfs(start, dest, diag_jumps)
print(solution)
