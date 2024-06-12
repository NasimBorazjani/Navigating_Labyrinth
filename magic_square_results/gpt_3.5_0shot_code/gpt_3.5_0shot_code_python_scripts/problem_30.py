
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(val == 172 for val in col_sums) and all(val == 212 for val in row_sums) and diag_sum1 == 165 and diag_sum2 == 165

def solve_magic_square():
    grid = [['x', 'x', 59],
            ['x', 'x', 'x'],
            [38, 'x', 'x']]
    
    possible_values = [val for val in range(34, 79) if val not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in itertools.permutations(possible_values, 3):
        new_grid = [row.copy() for row in grid]
        new_grid[0][0] = perm[0]
        new_grid[0][1] = perm[1]
        new_grid[1][0] = perm[2]
        
        if is_magic_square(new_grid):
            total_sum = sum(itertools.chain(*new_grid))
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(0, 0, perm[0]), (0, 1, perm[1]), (1, 0, perm[2])]
    
    return min_solution

solution = solve_magic_square()
print(solution)
