
def check_number(grid, number, row, col):
    for i in range(4):
        if grid[row][i] == number or grid[i][col] == number:
            return False

    if row == col:
        for i in range(4):
            if grid[i][i] == number:
                return False

    if row == 3 - col:
        for i in range(4):
            if grid[i][3 - i] == number:
                return False

    return True

def solve_magic_square(grid, row=0, col=0):
    if row == 4:
        return grid

    if col == 4:
        return solve_magic_square(grid, row + 1, 0)

    if grid[row][col] != 'x':
        return solve_magic_square(grid, row, col + 1)

    for number in range(41, 93):
        if check_number(grid, number, row, col):
            grid[row][col] = number
            solution = solve_magic_square(grid, row, col + 1)
            if solution:
                return [(row, col, number)] + solution
            grid[row][col] = 'x'

    return None

given_grid = [['53', '57', 'x', 'x'], ['77', '78', 'x', '56'], ['51', '62', '88', 'x'], ['x', 'x', 'x', 'x']]
solution = solve_magic_square(given_grid)
print(solution)
