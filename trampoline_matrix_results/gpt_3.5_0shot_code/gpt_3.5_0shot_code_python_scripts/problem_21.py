
def is_valid_move(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

def find_shortest_path(grid, start, end, diagonal_jumps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    queue = [(start, [start])]
    
    while queue:
        current, path = queue.pop(0)
        if current == end and len(path) == diagonal_jumps + 1:
            return path
        
        for dx, dy in directions:
            for i in range(1, 3):
                new_row = current[0] + i * dx
                new_col = current[1] + i * dy
                if is_valid_move(grid, new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None

grid = [
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
]

start = (1, 9)
end = (5, 0)
diagonal_jumps = 3

shortest_path = find_shortest_path(grid, start, end, diagonal_jumps)
print(shortest_path)
