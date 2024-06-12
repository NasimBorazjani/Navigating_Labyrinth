
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(val == 82 for val in row_sums + col_sums + [diag_sum1, diag_sum2])

def solve_magic_square():
    grid = [['x', 'x', 'x'],
            ['x', 'x', 'x'],
            ['22', 'x', 'x']]
    
    possible_values = [val for val in range(20, 40) if val != 22]
    min_sum = float('inf')
    min_config = None
    
    for perm in itertools.permutations(possible_values, 6):
        temp_grid = [row.copy() for row in grid]
        temp_grid[2][0] = 22
        temp_grid[0][0], temp_grid[0][1], temp_grid[0][2] = perm[:3]
        temp_grid[1][0], temp_grid[1][1], temp_grid[1][2] = perm[3:]
        
        if is_magic_square(temp_grid):
            temp_sum = sum(val for row in temp_grid for val in row if val != 'x')
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_config = [(i, j, temp_grid[i][j]) for i in range(3) for j in range(3) if temp_grid[i][j] != 'x']
    
    return min_config

solution = solve_magic_square()
print(solution)
