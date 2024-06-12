
from itertools import permutations

def check_sums(grid):
    row_sums = [sum([int(num) for num in row if num != 'x']) for row in grid]
    col_sums = [sum([int(grid[i][j]) for i in range(4) if grid[i][j] != 'x']) for j in range(4)]
    diag_sum1 = sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x'])
    diag_sum2 = sum([int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x'])
    
    return row_sums[1] == 255 and row_sums[2] == 268 and col_sums[1] == 240 and col_sums[2] == 226 and diag_sum1 == 264 and diag_sum2 == 264

def solve_magic_square():
    grid = [['x', '51', 'x', '65'],
            ['x', 'x', 'x', '68'],
            ['x', 'x', '64', '75'],
            ['x', 'x', 'x', 'x']]
    
    possible_nums = [str(num) for num in range(43, 85)]
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_nums, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            total_sum = sum([int(num) for row in grid for num in row if num != 'x'])
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, int(num)) for (row, col), num in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
