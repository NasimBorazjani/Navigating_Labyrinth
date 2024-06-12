
import itertools

def is_magic_square(grid):
    # Check if the sum of column 1 is 180
    if sum([int(grid[i][0]) for i in range(3)]) != 180:
        return False
    
    # Check if the sum of row 1 is 156
    if sum([int(grid[0][j]) for j in range(3)]) != 156:
        return False
    
    # Check if the sum of the diagonal from top right to bottom left is 127
    if int(grid[0][2]) + int(grid[1][1]) + int(grid[2][0]) != 127:
        return False
    
    return True

def find_min_sum(grid):
    min_sum = float('inf')
    min_permutation = None
    
    for permutation in itertools.permutations(range(34, 79), 5):
        temp_grid = [row.copy() for row in grid]
        temp_grid[0][0] = str(permutation[0])
        temp_grid[0][2] = str(permutation[1])
        temp_grid[1][1] = str(permutation[2])
        temp_grid[1][2] = str(permutation[3])
        temp_grid[2][0] = str(permutation[4])
        
        if is_magic_square(temp_grid):
            temp_sum = sum([int(num) for row in temp_grid for num in row if num.isdigit()])
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_permutation = [(0, 0, permutation[0]), (0, 2, permutation[1]), (1, 1, permutation[2]), (1, 2, permutation[3]), (2, 0, permutation[4])]
    
    return min_permutation

grid = [['x', '77', 'x'],
        ['49', 'x', 'x'],
        ['x', 'x', 'x']]

solution = find_min_sum(grid)
print(solution)
