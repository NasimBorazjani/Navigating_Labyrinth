
from collections import deque

def is_valid(i, j, visited):
    if i<0 or j<0 or i>=11 or j>=11 or visited[i][j] or grid[i][j]==1:
        return False
    return True

def bfs(start, end, grid):
    visited = [[False for _ in range(11)] for _ in range(11)]
    visited[start[0]][start[1]] = True
    queue = deque([(start, 0, [])])
    while queue:
        current, jump_count, path = queue.popleft()
        if current == end and jump_count == 3:
            return path + [current]
        for i, j in ((-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)):
            next_node = (current[0]+i, current[1]+j)
            if is_valid(next_node[0], next_node[1], visited):
                visited[next_node[0]][next_node[1]] = True
                queue.append((next_node, jump_count+1, path + [current]))
    return None

grid = [
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

start = (10, 9)
end = (3, 1)

result = bfs(start, end, grid)
print(result)
