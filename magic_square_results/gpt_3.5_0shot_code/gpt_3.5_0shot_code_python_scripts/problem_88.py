
import itertools

def is_magic_square(grid):
    # Check if the sums of rows and columns match the given constraints
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    
    if row_sums == [None, 190, 154, None] and col_sums == [None, 183, 202, None]:
        # Check if the diagonal sum is correct
        diagonal_sum = sum(grid[i][j] for i, j in zip(range(4), range(3, -1, -1)))
        if diagonal_sum == 183:
            return True
    return False

def solve_magic_square(grid):
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(22, 69) if val not in itertools.chain(*grid)]
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        new_grid = [row.copy() for row in grid]
        for (i, j), val in zip(unknown_positions, values):
            new_grid[i][j] = val
        if is_magic_square(new_grid):
            return [(i, j, val) for (i, j), val in zip(unknown_positions, values)]

# Given grid
grid = [['27', '48', 'x', 'x'],
        ['x', 'x', '63', 'x'],
        ['28', 'x', '33', '26'],
        ['x', 'x', 'x', '39']]

solution = solve_magic_square(grid)
print(solution)
