
import itertools

def is_magic_square(grid):
    # Check rows and columns sums
    for i in range(4):
        if sum(grid[i][j] for j in range(4) if grid[i][j] != 'x') not in [None, 89, 103]:
            return False
        if sum(grid[j][i] for j in range(4) if grid[j][i] != 'x') not in [None, 121, 107]:
            return False
    
    # Check diagonal sum
    if sum(grid[i][i] for i in range(4) if grid[i][i] != 'x') != 102:
        return False
    
    if sum(grid[i][3-i] for i in range(4) if grid[i][3-i] != 'x') != 102:
        return False
    
    return True

def solve_magic_square():
    grid = [['14', '35', 'x', 'x'],
            ['x', 'x', 'x', '18'],
            ['x', '31', '27', '21'],
            ['30', 'x', 'x', '19']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    
    possible_values = [str(i) for i in range(9, 41)]
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = permutation[i]
        
        if is_magic_square(grid):
            current_sum = sum(int(grid[i][j]) for i in range(4) for j in range(4))
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, int(val)) for (row, col), val in zip(unknown_positions, permutation)]
    
    return min_solution

solution = solve_magic_square()
print(solution)
