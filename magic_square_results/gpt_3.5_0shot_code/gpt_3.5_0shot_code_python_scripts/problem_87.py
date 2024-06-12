
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 233, 237, None] and col_sums == [None, 258, 247, None] and diag_sum1 == 242 and diag_sum2 == 242

def solve_magic_square():
    grid = [[72, 76, 68, 69],
            [56, 'x', 'x', 'x'],
            [49, 'x', 'x', 43],
            ['x', 'x', 61, 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [i for i in range(37, 84)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if is_magic_square(grid):
            total_sum = sum(sum(row) for row in grid)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
