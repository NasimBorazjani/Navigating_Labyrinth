
def find_max(grid):
    max_val = -1
    max_pos = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '_' and grid[i][j] > max_val:
                max_val = grid[i][j]
                max_pos = (i, j)
    return max_val, max_pos

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '_':
                return (i, j)

def swap(grid, pos1, pos2):
    grid[pos1[0]][pos1[1]], grid[pos2[0]][pos2[1]] = grid[pos2[0]][pos2[1]], grid[pos1[0]][pos1[1]]

def solve_puzzle(grid):
    solution = []
    for i in range(len(grid)*len(grid[0]) - 1):
        max_val, max_pos = find_max(grid)
        empty_pos = find_empty(grid)
        swap(grid, max_pos, empty_pos)
        solution.append(max_val)
    return solution

grid = [[94, 92, 77, 88, '_'], [82, 43, 76, 85, 87], [24, 66, 17, 79, 75]]
print(solve_puzzle(grid))
