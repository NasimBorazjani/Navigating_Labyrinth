
from collections import deque

def is_valid(i, j, visited):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0 and not visited[i][j]

def bfs(start, end):
    queue = deque([(start, [start])])
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    while queue:
        i, j = queue.popleft()
        if (i, j) == end:
            return queue.popleft()[1]
        for x, y in [(i-2, j-1), (i-2, j+1), (i+2, j-1), (i+2, j+1), (i-1, j-2), (i-1, j+2), (i+1, j-2), (i+1, j+2)]:
            if is_valid(x, y, visited):
                visited[x][y] = True
                queue.append(((x, y), queue[-1][1] + [(x, y)]))

grid = [[1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1]]
start, end = (1, 9), (8, 0)
print(bfs(start, end))
