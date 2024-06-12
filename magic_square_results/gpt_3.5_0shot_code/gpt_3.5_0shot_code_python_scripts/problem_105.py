
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if 'x' not in row else None for row in grid]
    col_sums = [sum(col) if 'x' not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4) if grid[i][i] != 'x')
    diag_sum2 = sum(grid[i][3-i] for i in range(4) if grid[i][3-i] != 'x')
    
    return row_sums == [None, 214, 240, None] and col_sums == [None, 300, 191, None] and diag_sum1 == 249 and diag_sum2 == 249

def solve_magic_square():
    grid = [['x', '69', 'x', 'x'],
            ['x', '62', 'x', 'x'],
            ['x', '82', '40', 'x'],
            ['x', '87', '78', '80']]
    
    possible_values = [i for i in range(36, 93)]
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = permutation[i]
        
        if is_magic_square(grid):
            total_sum = sum(sum(row) for row in grid)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, permutation)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
