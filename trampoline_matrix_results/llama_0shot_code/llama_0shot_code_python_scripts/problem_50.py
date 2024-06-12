
from collections import deque

# Grid map of the trampoline park
grid = [
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

def is_valid(x, y, visited):
    # Check if the trampoline is within the grid, not broken, and not visited
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (x, y) not in visited

def bfs(start, end):
    # Create a visited dictionary to mark visited trampolines
    visited = {start: None}

    # Create a queue and enqueue the first node
    q = deque([start])

    # Create a dictionary to store the path
    path = {}

    # Four diagonal jumps
    dx, dy = [1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]

    while q:
        node = q.popleft()
        if node == end:
            break

        for i in range(8):
            x, y = node[0] + dx[i], node[1] + dy[i]
            if is_valid(x, y, visited):
                visited[(x, y)] = node
                q.append((x, y))
                path[(x, y)] = node

    # Return the path as a list of tuples
    return [end] + [path[end]]

# Test the function
print(bfs((11, 11), (0, 6)))
