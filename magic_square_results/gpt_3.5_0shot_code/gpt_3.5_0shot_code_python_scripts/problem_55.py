
import itertools

def is_magic_square(grid):
    # Check if the sums of rows and columns match the given constraints
    for i in range(4):
        if sum(grid[i][j] for j in range(4) if grid[i][j] != 'x') not in [None, 168]:
            return False
        if sum(grid[j][i] for j in range(4) if grid[j][i] != 'x') not in [None, 162, 195]:
            return False
    
    # Check if the sum of the diagonal from top right to bottom left is 168
    if sum(grid[i][3-i] for i in range(4) if grid[i][3-i] != 'x') != 168:
        return False
    
    return True

def solve_magic_square():
    grid = [['46', 'x', '58', '45'],
            ['x', 'x', '54', 'x'],
            ['x', 'x', 'x', 'x'],
            ['28', '53', '34', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [str(i) for i in range(28, 60) if str(i) not in sum(grid, [])]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for pos, val in zip(unknown_positions, values):
            grid[pos[0]][pos[1]] = val
        
        if is_magic_square(grid):
            current_sum = sum(int(val) for val in sum(grid, []) if val != 'x')
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(pos[0], pos[1], int(val)) for pos, val in zip(unknown_positions, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
