
import itertools

def is_magic_square(grid):
    # Check rows and columns sums
    for i in range(4):
        if sum(grid[i][j] for j in range(4) if grid[i][j] != 'x') not in [None, 269]:
            return False
        if sum(grid[j][i] for j in range(4) if grid[j][i] != 'x') not in [None, 259]:
            return False
    
    # Check diagonal sum
    if sum(grid[i][i] for i in range(4) if grid[i][i] != 'x') != 178:
        return False
    
    # Check anti-diagonal sum
    if sum(grid[i][3-i] for i in range(4) if grid[i][3-i] != 'x') != 178:
        return False
    
    return True

def solve_magic_square():
    grid = [['x', 'x', 'x', '40'],
            ['x', 'x', 'x', 'x'],
            ['49', '61', 'x', 'x'],
            ['33', '48', 'x', '54']]
    
    unknowns = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(33, 85) if x not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknowns)):
        for i, (row, col) in enumerate(unknowns):
            grid[row][col] = values[i]
        
        if is_magic_square(grid):
            total_sum = sum(sum(x for x in row if x != 'x') for row in grid)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, value) for (row, col), value in zip(unknowns, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
