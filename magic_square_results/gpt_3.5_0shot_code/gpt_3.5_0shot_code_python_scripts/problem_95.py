
import itertools

def is_magic_square(grid):
    # Check column sums
    for j in range(4):
        if sum(grid[i][j] for i in range(4) if grid[i][j] != 'x') not in [None, 262, 272]:
            return False
    
    # Check row sums
    for i in range(4):
        if sum(grid[i][j] for j in range(4) if grid[i][j] != 'x') not in [None, 291, 301]:
            return False
    
    # Check diagonal sum
    if sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x') != 256:
        return False
    
    return True

def solve_magic_square():
    grid = [['68', '50', '47', '65'],
            ['x', '91', 'x', '71'],
            ['x', 'x', 'x', '60'],
            ['x', 'x', 'x', '84']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [str(num) for num in range(41, 93)]
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for idx, (i, j) in enumerate(unknown_positions):
            grid[i][j] = permutation[idx]
        
        if is_magic_square(grid):
            current_sum = sum(int(num) for row in grid for num in row if num != 'x')
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(i, j, int(grid[i][j])) for i, j in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)
