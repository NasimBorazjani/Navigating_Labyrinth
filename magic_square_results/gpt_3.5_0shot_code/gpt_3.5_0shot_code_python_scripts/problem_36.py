
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(val == 198 for val in col_sums) and all(val == 152 for val in row_sums) and diag_sum1 == 195 and diag_sum2 == 195

def solve_magic_square():
    grid = [['x', 'x', 'x'],
            ['x', 'x', 'x'],
            ['69', '71', 'x']]
    
    possible_values = [val for val in range(40, 90) if val not in [69, 71]]
    permutations = itertools.permutations(possible_values, 3)
    
    min_sum = float('inf')
    solution = None
    
    for perm in permutations:
        grid[0][0] = perm[0]
        grid[0][1] = perm[1]
        grid[1][0] = perm[2]
        
        if is_magic_square(grid):
            total_sum = sum(sum(row) for row in grid)
            if total_sum < min_sum:
                min_sum = total_sum
                solution = [(0, 0, perm[0]), (0, 1, perm[1]), (1, 0, perm[2])]
    
    return solution

solution = solve_magic_square()
print(solution)
