
import itertools

def is_magic_square(grid):
    # Check if the sum of column 1 is 150
    if sum([int(grid[i][0]) for i in range(3)]) != 150:
        return False
    
    # Check if the sum of row 1 is 135
    if sum([int(grid[0][j]) for j in range(3)]) != 135:
        return False
    
    # Check if the sum of the diagonal from top right to bottom left is 119
    if int(grid[0][2]) + int(grid[1][1]) + int(grid[2][0]) != 119:
        return False
    
    return True

def find_min_sum(grid):
    min_sum = float('inf')
    min_permutation = None
    
    for permutation in itertools.permutations(range(26, 66), 6):
        temp_grid = [row.copy() for row in grid]
        temp_grid[2][1] = '32'
        
        for i, num in enumerate(permutation):
            temp_grid[i//3][i%3] = str(num)
        
        if is_magic_square(temp_grid):
            current_sum = sum([int(num) for row in temp_grid for num in row if num != 'x'])
            if current_sum < min_sum:
                min_sum = current_sum
                min_permutation = temp_grid
    
    return min_permutation

grid = [['x', 'x', 'x'],
        ['x', 'x', 'x'],
        ['x', '32', 'x']]

solution = find_min_sum(grid)

output = []
for i in range(3):
    for j in range(3):
        if solution[i][j] == 'x':
            output.append((i, j, int(grid[i][j])))

print(output)
