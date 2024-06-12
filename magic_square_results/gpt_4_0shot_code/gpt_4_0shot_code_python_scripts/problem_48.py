
import numpy as np

def is_valid(grid, row, col, num):
    for x in range(4):
        if grid[row][x] == num:
            return False
    for x in range(4):
        if grid[x][col] == num:
            return False
    return True

def solve_magic_square(grid, l):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                for num in range(34, 61):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve_magic_square(grid, l):
                            l.append((i, j, num))
                            return True
                        grid[i][j] = 'x'
                return False
    return True

def magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['x', '46', 'x', '41'],
            ['x', '57', '55', 'x'],
            ['x', '37', 'x', 'x']]
    grid = [[int(x) if x != 'x' else 'x' for x in row] for row in grid]
    l = []
    solve_magic_square(grid, l)
    return l

print(magic_square())
