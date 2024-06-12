
def is_valid_move(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

def find_shortest_path(grid, start, end, diagonal_jumps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    diagonal_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    def dfs(row, col, jumps_left, path):
        if jumps_left == 0 and (row, col) == end:
            return path
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(grid, new_row, new_col):
                new_path = path + [(new_row, new_col)]
                if (new_row, new_col) == end:
                    return new_path
                for ddr, ddc in diagonal_directions:
                    new_row2, new_col2 = new_row + ddr, new_col + ddc
                    if is_valid_move(grid, new_row2, new_col2):
                        result = dfs(new_row2, new_col2, jumps_left - 1, new_path)
                        if result:
                            return result
        return None
    
    return dfs(start[0], start[1], diagonal_jumps, [start])

grid = [
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]
]

start = (8, 1)
end = (1, 9)
diagonal_jumps = 3

shortest_path = find_shortest_path(grid, start, end, diagonal_jumps)
print(shortest_path)
