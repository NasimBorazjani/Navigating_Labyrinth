
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if 'x' not in row else None for row in grid]
    col_sums = [sum(col) if 'x' not in col else None for col in zip(*grid)]
    diag_sum = sum(grid[i][i] for i in range(4))
    anti_diag_sum = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 220, 216, None] and col_sums == [None, 224, 226, None] and diag_sum == 211 and anti_diag_sum == 211

def solve_magic_square():
    grid = [['x', '40', 'x', 'x'],
            ['x', '58', 'x', '37'],
            ['47', 'x', 'x', '44'],
            ['45', 'x', 'x', '42']]
    
    possible_values = [i for i in range(31, 68)]
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            total_sum = sum(sum(row) for row in grid)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
