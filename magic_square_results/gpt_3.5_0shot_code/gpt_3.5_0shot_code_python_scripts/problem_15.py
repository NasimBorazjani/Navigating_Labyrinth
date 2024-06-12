
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(x == 190 for x in col_sums) and all(x == 167 for x in row_sums) and diag_sum1 == 172 and diag_sum2 == 172

def solve_magic_square():
    grid = [['x', 'x', 'x'],
            ['x', 'x', 55],
            ['x', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [x for x in range(48, 78) if x != 55]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (x, y) in enumerate(unknown_positions):
            grid[x][y] = perm[i]
        
        if is_magic_square(grid):
            current_sum = sum(sum(row) for row in grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(x, y, grid[x][y]) for x, y in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)
