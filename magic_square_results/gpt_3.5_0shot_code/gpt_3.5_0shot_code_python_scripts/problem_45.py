
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 183, 190, None] and col_sums == [None, 177, 196, None] and diag_sum1 == 188 and diag_sum2 == 188

def solve_magic_square():
    grid = [['x', '50', 'x', 'x'],
            ['58', 'x', 'x', 'x'],
            ['x', '49', 'x', '59'],
            ['39', '41', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(35, 62) if val not in [int(cell) for row in grid for cell in row if cell != 'x']]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            total_sum = sum([val for val in perm])
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
