
from collections import deque

def bfs(grid):
    queue = deque([(0, 0)])
    path = {(0, 0): None}
    while queue:
        pos = queue.popleft()
        if pos == (5, 7):
            break
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = pos[0] + dx, pos[1] + dy
            if 0 <= nx < 9 and 0 <= ny < 9 and grid[nx][ny] == 0 and (nx, ny) not in path:
                queue.append((nx, ny))
                path[(nx, ny)] = pos
    else:
        return None
    # Backtrack from destination to start to find the path
    positions = []
    while pos is not None:
        positions.append(pos)
        pos = path[pos]
    return positions[::-1]

grid = [
    [0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1]
]

print(bfs(grid))
