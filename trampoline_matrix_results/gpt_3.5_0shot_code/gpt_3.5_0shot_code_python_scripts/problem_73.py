
def is_valid_move(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

def find_shortest_path(grid, start, end, diagonal_jumps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    diagonal_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    def dfs(row, col, jumps, path):
        if (row, col) == end and jumps == diagonal_jumps:
            return path
        
        for i in range(4):
            new_row = row + directions[i][0]
            new_col = col + directions[i][1]
            if is_valid_move(grid, new_row, new_col):
                new_path = path + [(new_row, new_col)]
                if i % 2 == 0:
                    new_jumps = jumps
                else:
                    new_jumps = jumps + 1
                result = dfs(new_row, new_col, new_jumps, new_path)
                if result:
                    return result
        
        return None
    
    return dfs(start[0], start[1], 0, [start])

grid = [
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
]

start = (1, 12)
end = (8, 2)
diagonal_jumps = 4

path = find_shortest_path(grid, start, end, diagonal_jumps)
print(path)
