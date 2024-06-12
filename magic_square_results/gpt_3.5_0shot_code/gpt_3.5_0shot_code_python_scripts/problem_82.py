
import itertools

def is_magic_square(grid):
    # Check rows and columns sums
    for i in range(4):
        row_sum = sum([int(grid[i][j]) if grid[i][j] != 'x' else 0 for j in range(4)])
        col_sum = sum([int(grid[j][i]) if grid[j][i] != 'x' else 0 for j in range(4)])
        if (row_sum != None and row_sum != [None, 227, 250, None][i]) or (col_sum != None and col_sum != [None, 209, 265, None][i]):
            return False
    
    # Check diagonal sum
    diagonal_sum = sum([int(grid[i][i]) if grid[i][i] != 'x' else 0 for i in range(4)])
    if diagonal_sum != 260:
        return False
    
    return True

def solve_magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['53', '43', 'x', 'x'],
            ['72', 'x', 'x', 'x'],
            ['63', 'x', 'x', '50']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [str(num) for num in range(43, 85)]
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = permutation[i]
        
        if is_magic_square(grid):
            total_sum = sum([int(num) for row in grid for num in row if num != 'x'])
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, int(num)) for (row, col), num in zip(unknown_positions, permutation)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
