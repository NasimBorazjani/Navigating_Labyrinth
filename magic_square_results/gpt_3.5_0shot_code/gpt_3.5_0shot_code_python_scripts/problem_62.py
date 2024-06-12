
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum = sum(grid[i][i] for i in range(4))
    anti_diag_sum = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 164, 210, None] and col_sums == [None, 199, 194, None] and diag_sum == 197 and anti_diag_sum == 197

def solve_magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['40', '39', '32', '53'],
            ['46', 'x', '58', 'x'],
            ['x', 'x', '43', '51']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(30, 67) if val not in [int(cell) for row in grid for cell in row if cell != 'x']]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(perm[i])
        
        if check_sums(grid):
            current_sum = sum(int(cell) for row in grid for cell in row if cell != 'x')
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, int(grid[row][col])) for row, col in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)
