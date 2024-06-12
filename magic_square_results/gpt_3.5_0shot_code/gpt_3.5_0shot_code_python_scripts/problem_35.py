
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(val == 153 for val in col_sums) and all(val == 186 for val in row_sums) and diag_sum1 == 188 and diag_sum2 == 188

def find_min_sum_magic_square():
    grid = [['x', 'x', 'x'],
            ['80', '48', 'x'],
            ['x', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [val for val in range(40, 90)]
    
    min_sum = float('inf')
    min_sum_grid = None
    
    for perm in itertools.permutations(possible_values, len(unknown_positions)):
        temp_grid = [row.copy() for row in grid]
        for pos, val in zip(unknown_positions, perm):
            temp_grid[pos[0]][pos[1]] = val
        
        if is_magic_square(temp_grid):
            temp_sum = sum(sum(row) for row in temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_sum_grid = temp_grid
    
    return [(i, j, int(min_sum_grid[i][j])) for i, row in enumerate(min_sum_grid) for j, val in enumerate(row) if val == 'x']

solution = find_min_sum_magic_square()
print(solution)