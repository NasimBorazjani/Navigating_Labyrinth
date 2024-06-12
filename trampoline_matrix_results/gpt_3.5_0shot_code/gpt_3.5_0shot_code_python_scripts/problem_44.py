
def is_valid_move(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

def find_shortest_path(grid, start, end, diagonal_jumps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    diagonal_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    def dfs(row, col, jumps_left, path):
        if jumps_left == 0 and (row, col) == end:
            return path
        
        for i in range(len(directions)):
            new_row = row + directions[i][0]
            new_col = col + directions[i][1]
            if is_valid_move(grid, new_row, new_col):
                new_path = path + [(new_row, new_col)]
                if i % 2 == 0:
                    new_jumps_left = jumps_left
                else:
                    new_jumps_left = jumps_left - 1
                result = dfs(new_row, new_col, new_jumps_left, new_path)
                if result:
                    return result
        
        return None
    
    return dfs(start[0], start[1], diagonal_jumps, [start])

grid = [
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1]
]

start = (2, 1)
end = (10, 9)
diagonal_jumps = 3

shortest_path = find_shortest_path(grid, start, end, diagonal_jumps)
print(shortest_path)
