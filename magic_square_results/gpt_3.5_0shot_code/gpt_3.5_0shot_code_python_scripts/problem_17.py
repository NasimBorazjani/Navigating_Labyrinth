
from itertools import permutations

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(sum == 166 for sum in col_sums) and all(sum == 192 for sum in row_sums) and diag_sum1 == 184 and diag_sum2 == 184

def find_minimal_magic_square():
    grid = [['x', '52', 'x'],
            ['x', 'x', 'x'],
            ['x', 'x', 'x']]
    
    possible_values = [str(i) for i in range(48, 78)]
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    
    min_sum = float('inf')
    min_square = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if is_magic_square(grid):
            current_sum = sum(int(val) for row in grid for val in row)
            if current_sum < min_sum:
                min_sum = current_sum
                min_square = [tuple([row, col, int(val)]) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_square

solution = find_minimal_magic_square()
print(solution)
