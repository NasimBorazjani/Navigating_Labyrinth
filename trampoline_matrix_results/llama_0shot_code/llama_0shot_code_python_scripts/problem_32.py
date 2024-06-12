
from collections import deque

# Grid map
grid = [[1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]]

# Function to generate next positions
def generate_next_positions(pos, visited):
    row, col = pos
    next_positions = []
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        for _ in range(3):
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid) and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                next_positions.append((new_row, new_col))
                visited.add((new_row, new_col))
            else:
                break
            dr, dc = dr * 2, dc * 2  # Double the direction for next jump
    return next_positions

# BFS function
def bfs(start, end):
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        pos = path[-1]
        if pos == end:
            return path
        for next_pos in generate_next_positions(pos, set(path)):
            new_path = list(path)
            new_path.append(next_pos)
            queue.append(new_path)

# Call BFS
start, end = (0, 9), (9, 2)
print(bfs(start, end))
