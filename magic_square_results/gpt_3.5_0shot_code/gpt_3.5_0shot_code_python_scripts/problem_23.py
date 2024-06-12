
import itertools

def is_magic_square(grid):
    # Check if the sum of column 1 is 71
    if sum([grid[i][0] for i in range(3)]) != 71:
        return False
    
    # Check if the sum of row 1 is 82
    if sum(grid[0]) != 82:
        return False
    
    # Check if the sum of the diagonal from top right to bottom left is 70
    if grid[0][2] + grid[1][1] + grid[2][0] != 70:
        return False
    
    return True

def find_unique_integers():
    possible_integers = [i for i in range(12, 47)]
    grid = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 19]]
    
    min_sum = float('inf')
    min_positions = []
    
    for perm in itertools.permutations(possible_integers, 6):
        grid[0][0] = perm[0]
        grid[1][0] = perm[1]
        grid[2][0] = perm[2]
        grid[0][1] = perm[3]
        grid[1][1] = perm[4]
        grid[2][1] = perm[5]
        
        if is_magic_square(grid):
            current_sum = sum([sum(row) for row in grid if 'x' not in row])
            if current_sum < min_sum:
                min_sum = current_sum
                min_positions = [(i, j, grid[i][j]) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    
    return min_positions

solution = find_unique_integers()
print(solution)
