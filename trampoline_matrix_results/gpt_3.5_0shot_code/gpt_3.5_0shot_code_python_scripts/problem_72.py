
def is_valid_move(grid, visited, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0 and visited[row][col] == 0

def find_shortest_path(grid, start, end):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = [(start, [start])]
    
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        
        for direction in directions:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]
            
            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = 1
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None

grid = [
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

start = (8, 12)
end = (1, 1)

shortest_path = find_shortest_path(grid, start, end)
print(shortest_path)