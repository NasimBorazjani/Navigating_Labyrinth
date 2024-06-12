
from collections import deque

# Grid map of the trampoline park
grid = [
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
]

def is_valid(x, y):
    # Check if the coordinates are within the grid and the trampoline is not broken
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def bfs():
    # Define the start and end positions
    start, end = (1, 1), (10, 8)

    # Define the eight possible diagonal moves
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]

    # Initialize the queue for BFS with the start position and the current sequence of jumps
    queue = deque([([start], 0)])

    # While there are still positions to explore
    while queue:
        current_sequence, current_jumps = queue.popleft()
        current_position = current_sequence[-1]

        # If we have reached the end position with exactly 4 diagonal jumps
        if current_position == end and current_jumps == 4:
            return current_sequence[1:]

        # If the number of diagonal jumps is less than 4
        elif current_jumps < 4:
            for direction in directions:
                next_x, next_y = current_position[0] + direction[0], current_position[1] + direction[1]
                if is_valid(next_x, next_y):
                    new_sequence = current_sequence + [(next_x, next_y)]
                    queue.append((new_sequence, current_jumps + 1))

# Print the shortest sequence of trampolines
print(bfs())
