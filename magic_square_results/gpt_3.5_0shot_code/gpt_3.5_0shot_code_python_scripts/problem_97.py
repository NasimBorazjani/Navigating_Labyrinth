
import itertools

def is_magic_square(grid):
    # Check if the sums of rows, columns, and diagonal are correct
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 175, 114, None] and col_sums == [None, 117, 160, None] and diag_sum1 == 114 and diag_sum2 == 114

def solve_magic_square():
    grid = [['58', '19', 'x', 'x'],
            ['x', 'x', 'x', 'x'],
            ['x', '22', 'x', '39'],
            ['x', '16', '53', '29']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [num for num in range(11, 63) if str(num) not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(values[i])
        
        if is_magic_square(grid):
            total_sum = sum(int(num) for row in grid for num in row if num != 'x')
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, int(grid[row][col])) for row, col in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)
