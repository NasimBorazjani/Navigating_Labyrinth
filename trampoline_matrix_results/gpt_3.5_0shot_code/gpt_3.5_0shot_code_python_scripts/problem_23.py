
def is_valid_move(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

def find_shortest_path(grid, start, end, diagonal_jumps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    diagonal_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    def dfs(row, col, jumps):
        if jumps == diagonal_jumps and (row, col) == end:
            return [(row, col)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(grid, new_row, new_col):
                for ddr, ddc in diagonal_directions:
                    new_row2, new_col2 = new_row + ddr, new_col + ddc
                    if is_valid_move(grid, new_row2, new_col2):
                        path = dfs(new_row2, new_col2, jumps + 1)
                        if path:
                            return [(row, col)] + path
        
        return []
    
    return dfs(start[0], start[1], 0)

grid = [
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 0]
]

start = (1, 9)
end = (8, 3)
diagonal_jumps = 3

path = find_shortest_path(grid, start, end, diagonal_jumps)
print(path)
