
import numpy as np

def is_valid(grid, row, col, num):
    for i in range(4):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def find_min_sum(grid):
    min_sum = float('inf')
    min_sum_indices = None
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                for num in range(10, 65):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        current_sum = sum(grid[0]) + sum(grid[i][j] for i in range(4)) + sum(grid[i][i] for i in range(4))
                        if current_sum < min_sum:
                            min_sum = current_sum
                            min_sum_indices = (i, j, num)
                        grid[i][j] = 'x'
    return min_sum_indices

grid = np.array([['x', '21', 'x', 'x'],
                 ['18', '27', 'x', '51'],
                 ['24', '29', 'x', 'x'],
                 ['54', '33', '25', '12']])

result = []
while True:
    indices = find_min_sum(grid)
    if indices is None:
        break
    result.append(indices)
    grid[indices[0]][indices[1]] = indices[2]

print(result)
