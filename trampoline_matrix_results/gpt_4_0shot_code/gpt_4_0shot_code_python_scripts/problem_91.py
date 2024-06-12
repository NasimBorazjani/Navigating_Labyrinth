
# Define the grid
grid = [
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1]
]

# Define the start and end positions
start = (14, 2)
end = (1, 9)

# Define the possible moves
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define the DFS function
def dfs(pos, end, grid, path, jumps):
    if jumps < 0:
        return None
    if pos == end and jumps == 0:
        return path
    x, y = pos
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 15 and 0 <= ny < 15 and grid[nx][ny] == 0:
            grid[nx][ny] = 1
            result = dfs((nx, ny), end, grid, path + [(nx, ny)], jumps - 1)
            if result is not None:
                return result
            grid[nx][ny] = 0
    return None

# Call the DFS function
path = dfs(start, end, grid, [start], 5)

# Print the result
print(path)
