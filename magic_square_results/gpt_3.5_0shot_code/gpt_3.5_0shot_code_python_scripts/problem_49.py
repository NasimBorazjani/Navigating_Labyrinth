
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 169, 190, None] and col_sums == [None, 165, 155, None] and diag_sum1 == 201 and diag_sum2 == 201

def solve_magic_square():
    grid = [['37', 'x', 'x', '56'],
            ['52', 'x', 'x', 'x'],
            ['x', '50', 'x', 'x'],
            ['x', 'x', 'x', '46']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(34, 61) if val not in [int(cell) for row in grid for cell in row]]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for pos, val in zip(unknown_positions, values):
            grid[pos[0]][pos[1]] = str(val)
        
        if is_magic_square(grid):
            current_sum = sum(int(cell) for row in grid for cell in row)
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(pos[0], pos[1], val) for pos, val in zip(unknown_positions, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
