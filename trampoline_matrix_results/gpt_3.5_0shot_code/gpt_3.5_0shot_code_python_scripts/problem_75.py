
def is_valid_move(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

def find_shortest_path(grid, start, end, diagonal_jumps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    diagonal_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    def dfs(row, col, jumps, path):
        if (row, col) == end and jumps == diagonal_jumps:
            return path
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(grid, new_row, new_col):
                new_path = path + [(new_row, new_col)]
                if (dr, dc) in diagonal_directions:
                    new_jumps = jumps + 1
                else:
                    new_jumps = jumps
                result = dfs(new_row, new_col, new_jumps, new_path)
                if result:
                    return result
        
        return None
    
    return dfs(start[0], start[1], 0, [start])

grid = [
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
]

start = (0, 7)
end = (12, 0)
diagonal_jumps = 4

path = find_shortest_path(grid, start, end, diagonal_jumps)
print(path)
