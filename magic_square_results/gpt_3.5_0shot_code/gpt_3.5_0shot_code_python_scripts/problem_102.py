
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 183, 217, None] and col_sums == [None, 260, 216, None] and diag_sum1 == 214 and diag_sum2 == 214

def solve_magic_square():
    grid = [['70', 'x', '50', 'x'],
            ['x', '39', '46', 'x'],
            ['34', '60', 'x', '51'],
            ['x', 'x', 'x', '68']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(30, 87) if val not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = values[i]
        
        if is_magic_square(grid):
            current_sum = sum(sum(row) for row in grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
