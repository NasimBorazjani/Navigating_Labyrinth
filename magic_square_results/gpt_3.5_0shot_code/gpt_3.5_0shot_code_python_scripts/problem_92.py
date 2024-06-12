
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 298, 222, None] and col_sums == [None, 240, 266, None] and diag_sum1 == 299 and diag_sum2 == 299

def solve_magic_square():
    grid = [['x', '41', '67', 'x'],
            ['x', '73', 'x', '91'],
            ['x', '43', 'x', '76'],
            ['80', 'x', 'x', '86']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [num for num in range(41, 93) if num not in [41, 67, 73, 91, 43, 76, 80, 86]]
    
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
