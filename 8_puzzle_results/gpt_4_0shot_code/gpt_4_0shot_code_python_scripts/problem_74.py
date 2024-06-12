
def find_position(grid, item):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == item:
                return i, j
    return None

def swap_positions(grid, pos1, pos2):
    grid[pos1[0]][pos1[1]], grid[pos2[0]][pos2[1]] = grid[pos2[0]][pos2[1]], grid[pos1[0]][pos1[1]]
    return grid

def solve_puzzle(grid):
    swaps = []
    while grid != sorted(grid, reverse=True):
        empty_pos = find_position(grid, '_')
        max_num = max([item for sublist in grid for item in sublist if item != '_'])
        max_pos = find_position(grid, max_num)
        grid = swap_positions(grid, empty_pos, max_pos)
        swaps.append(max_num)
    return swaps

grid = [[49, 20, 77, 78, 57], [41, '_', 52, 44, 72], [27, 81, 45, 16, 46]]
print(solve_puzzle(grid))
