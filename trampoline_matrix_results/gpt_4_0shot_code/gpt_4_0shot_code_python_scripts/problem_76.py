
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
]

# Define the starting and ending positions
start = (2, 12)
end = (10, 1)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Perform a breadth-first search
queue = deque([(start, [start], 0)])
while queue:
    (x, y), path, diagonals = queue.popleft()
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 14 and 0 <= ny < 14 and park[nx][ny] == 0 and (nx, ny) not in path:
            new_diagonals = diagonals + 1 if dx != 0 and dy != 0 else diagonals
            if new_diagonals <= 4:
                new_path = path + [(nx, ny)]
                if (nx, ny) == end and new_diagonals == 4:
                    print(new_path)
                    exit(0)
                queue.append(((nx, ny), new_path, new_diagonals))
