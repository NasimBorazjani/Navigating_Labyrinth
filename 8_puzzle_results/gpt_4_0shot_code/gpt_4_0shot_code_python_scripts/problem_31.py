
def find_max(grid):
    max_val = -1
    max_pos = (-1, -1)
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
                return i, j

def swap(grid, pos1, pos2):
    grid[pos1[0]][pos1[1]], grid[pos2[0]][pos2[1]] = grid[pos2[0]][pos2[1]], grid[pos1[0]][pos1[1]]

def solve_puzzle(grid):
    solution = []
    for i in range(len(grid)*len(grid[0])-1, -1, -1):
        max_val, max_pos = find_max(grid)
        empty_pos = find_empty(grid)
        swap(grid, max_pos, empty_pos)
        solution.append(max_val)
    return solution

grid = [[75, 53, 73, 62], ['_', 14, 90, 43], [21, 17, 51, 27]]
print(solve_puzzle(grid))
