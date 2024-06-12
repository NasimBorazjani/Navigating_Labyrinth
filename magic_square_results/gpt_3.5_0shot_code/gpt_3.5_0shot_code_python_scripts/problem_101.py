
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 244, 251, None] and col_sums == [None, 295, 204, None] and diag_sum1 == 237 and diag_sum2 == 237

def solve_magic_square():
    grid = [[32, 75, 36, 'x'],
            ['x', 83, 'x', 'x'],
            ['x', 77, 58, 44],
            ['x', 60, 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(30, 87) if val not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = values[i]
        
        if is_magic_square(grid):
            total_sum = sum(itertools.chain(*grid))
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)