
from queue import Queue

def is_valid_move(grid, visited, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 0 and not visited[row][col]

def bfs(grid, start, end):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    diagonal_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    
    q = Queue()
    q.put((start, []))
    
    while not q.empty():
        (curr_row, curr_col), path = q.get()
        
        if (curr_row, curr_col) == end:
            return path + [(curr_row, curr_col)]
        
        for dr, dc in directions:
            new_row, new_col = curr_row + dr, curr_col + dc
            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = True
                q.put(((new_row, new_col), path + [(curr_row, curr_col)]))
        
        for dr, dc in diagonal_directions:
            new_row, new_col = curr_row + dr, curr_col + dc
            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = True
                q.put(((new_row, new_col), path + [(curr_row, curr_col)]))
    
    return None

grid = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
]

start = (8, 8)
end = (0, 0)

path = bfs(grid, start, end)
print(path)
