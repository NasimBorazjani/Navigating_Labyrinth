
from collections import deque

# Grid of the trampoline park
grid = [
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
]

# Function to check if a move is valid
def is_valid(x, y, visited, diagonals):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False
    if grid[x][y] == 1:
        return False
    if visited[x][y]:
        return False
    if diagonals == 0 and (x != y and x != len(grid) - 1 - y):
        return False
    return True

# BFS to find the shortest path
def bfs(start, end):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, 0, [])])
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == end:
            return path + [(x, y)]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited, 1):
                visited[nx][ny] = True
                queue.append(((nx, ny), 1, path + [(x, y)]))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited, 0):
                visited[nx][ny] = True
                queue.append(((nx, ny), 0, path + [(x, y)]))

# Main function
def main():
    start = (10, 12)
    end = (1, 1)
    path = bfs(start, end)
    print(path)

if __name__ == "__main__":
    main()
