
def is_valid_move(grid, visited, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 0 and not visited[row][col]

def find_shortest_path(grid, start, end):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    diagonal_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    
    queue = [(start, [start])]
    
    while queue:
        current, path = queue.pop(0)
        
        if current == end and len(path) == 10:
            return path
        
        for direction in directions:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]
            
            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
        
        for diagonal_direction in diagonal_directions:
            new_row = current[0] + diagonal_direction[0]
            new_col = current[1] + diagonal_direction[1]
            
            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None

grid = [
    [0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0]
]

start = (8, 6)
end = (0, 0)

path = find_shortest_path(grid, start, end)
print(path)