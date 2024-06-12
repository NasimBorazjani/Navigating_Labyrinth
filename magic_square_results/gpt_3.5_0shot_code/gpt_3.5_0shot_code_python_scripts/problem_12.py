
import itertools

def is_magic_square(grid):
    # Check sum of rows
    for row in grid:
        if sum(row) != 124:
            return False
    
    # Check sum of columns
    for col in range(3):
        if grid[0][col] + grid[1][col] + grid[2][col] != 126:
            return False
    
    # Check sum of diagonal
    if grid[0][2] + grid[1][1] + grid[2][0] != 136:
        return False
    
    return True

def find_min_sum_magic_square():
    grid = [['x', '46', 'x'],
            ['39', 'x', 'x'],
            ['x', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [x for x in range(28, 58) if x not in [int(val) for row in grid for val in row]]
    
    min_sum = float('inf')
    min_sum_grid = None
    
    for perm in itertools.permutations(possible_values, len(unknown_positions)):
        temp_grid = [row.copy() for row in grid]
        for i, (row, col) in enumerate(unknown_positions):
            temp_grid[row][col] = perm[i]
        
        if is_magic_square(temp_grid):
            temp_sum = sum([int(val) for row in temp_grid for val in row])
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_sum_grid = temp_grid
    
    return [(i, j, int(min_sum_grid[i][j])) for i, j in unknown_positions]

solution = find_min_sum_magic_square()
print(solution)
