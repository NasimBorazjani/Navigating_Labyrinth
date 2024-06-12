
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(x == 82 for x in col_sums) and all(x == 87 for x in row_sums) and diag_sum1 == 94 and diag_sum2 == 94

def find_min_sum_magic_square():
    grid = [['x', 'x', 'x'],
            ['30', 'x', 'x'],
            ['x', 'x', 'x']]
    
    possible_values = [i for i in range(20, 40)]
    min_sum = float('inf')
    min_grid = None
    
    for perm in itertools.permutations(possible_values, 5):
        grid[0][0] = perm[0]
        grid[0][1] = perm[1]
        grid[0][2] = perm[2]
        grid[1][1] = perm[3]
        grid[2][0] = perm[4]
        
        if is_magic_square(grid):
            current_sum = sum([x for x in perm if x != 'x'])
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = grid.copy()
    
    return min_grid

solution = find_min_sum_magic_square()
print(solution)
