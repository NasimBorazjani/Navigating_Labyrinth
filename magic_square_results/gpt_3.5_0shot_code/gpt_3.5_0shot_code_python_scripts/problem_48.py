
from itertools import permutations

def check_sums(grid):
    row_sums = [sum([int(num) if num != 'x' else 0 for num in row]) for row in grid]
    col_sums = [sum([int(grid[i][j]) if grid[i][j] != 'x' else 0 for i in range(4)]) for j in range(4)]
    diag_sum = sum([int(grid[i][i]) if grid[i][i] != 'x' else 0 for i in range(4)])
    anti_diag_sum = sum([int(grid[i][3-i]) if grid[i][3-i] != 'x' else 0 for i in range(4)])
    
    return row_sums[1] == 179 and row_sums[2] == 190 and col_sums[1] == 179 and col_sums[2] == 194 and diag_sum == 205 and anti_diag_sum == 205

def solve_magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['x', '46', 'x', '41'],
            ['x', '57', '55', 'x'],
            ['x', '37', 'x', 'x']]
    
    possible_nums = [num for num in range(34, 61)]
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_nums, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(perm[i])
        
        if check_sums(grid):
            total_sum = sum([int(num) for row in grid for num in row if num != 'x'])
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, int(grid[row][col])) for row, col in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)
