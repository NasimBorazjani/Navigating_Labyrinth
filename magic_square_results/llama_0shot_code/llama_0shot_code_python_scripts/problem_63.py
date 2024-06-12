
def solve_magic_square(grid):
    def possible_numbers(cell):
        row, col = cell
        return list(range(30, 67))

    def update_grid(cell, num):
        row, col = cell
        grid[row][col] = num

    def is_valid(cell, num):
        row, col = cell
        return all(num != grid[row][c] for c in range(4)) and \
               all(num != grid[r][col] for r in range(4)) and \
               (row == col) == (num == 37)  # 37 is the middle number

    def solve(cell=None):
        if cell is None:
            cell = (0, 0)
        row, col = cell
        if row == 4:
            return grid
        if col == 4:
            return solve((row + 1, 0))
        if grid[row][col] != 'x':
            return solve((row, col + 1))
        for num in sorted(possible_numbers((row, col)), key=lambda n: (grid[row][col] != 'x', -n)):
            if is_valid((row, col), num):
                update_grid((row, col), num)
                solution = solve((row, col + 1))
                if solution:
                    return solution
                update_grid((row, col), 'x')
        return None

    return solve()

grid = [['x', 'x', '63', 'x'],
        ['x', '44', 'x', '36'],
        ['50', 'x', 'x', '60'],
        ['x', '52', '38', '64']]

print(solve_magic_square(grid))
