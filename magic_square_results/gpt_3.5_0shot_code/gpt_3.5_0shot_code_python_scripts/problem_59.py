
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum = sum(grid[i][i] for i in range(4))
    anti_diag_sum = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 138, 149, None] and col_sums == [None, 148, 157, None] and diag_sum == 133 and anti_diag_sum == 133

def solve_magic_square():
    grid = [['35', 'x', '51', 'x'],
            ['x', 'x', 'x', '23'],
            ['x', '32', '31', '52'],
            ['x', 'x', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [str(num) for num in range(22, 54)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            total_sum = sum(int(num) for row in grid for num in row)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, int(val)) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
