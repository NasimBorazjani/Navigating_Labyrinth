
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 186, 174, None] and col_sums == [None, 218, 203, None] and diag_sum1 == 221 and diag_sum2 == 221

def solve_magic_square():
    grid = [['55', 'x', '53', 'x'],
            ['x', '50', '52', 'x'],
            ['x', 'x', 'x', '35'],
            ['x', '62', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(28, 65) if x not in [int(num) for row in grid for num in row]]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(values[i])
        
        if is_magic_square(grid):
            current_sum = sum(int(num) for row in grid for num in row)
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, int(grid[row][col])) for row, col in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)
