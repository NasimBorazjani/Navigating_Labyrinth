
def solve_magic_square(grid, constraints):
    rows, cols = 4, 4
    cells_to_fill = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 'x']
    solutions = []

    def fill_cell(i, j, num):
        grid[i][j] = num
        if (i, j) in cells_to_fill:
            cells_to_fill.remove((i, j))

    def unfill_cell(i, j):
        grid[i][j] = 'x'
        cells_to_fill.append((i, j))

    def is_valid(i, j, num):
        # Check row
        if i > 0 and sum(int(cell) for cell in grid[i] if cell != 'x') + num > constraints[i]:
            return False
        # Check column
        if j > 0 and sum(int(grid[row][j]) for row in range(rows) if grid[row][j] != 'x') + num > constraints[j]:
            return False
        # Check diagonal
        if i > 0 and j < cols - 1 and sum(grid[row][row-col+j] for row in range(rows) if grid[row][row-col+j] != 'x') + num > constraints[-1]:
            return False
        return True

    def backtrack(index=0):
        if index == len(cells_to_fill):
            if sum(int(cell) for row in grid for cell in row if cell != 'x') == constraints[-1]:
                solutions.append([(i, j, int(grid[i][j])) for i, j in cells_to_fill])
            return
        i, j = cells_to_fill[index]
        for num in range(31, 68):
            if is_valid(i, j, num):
                fill_cell(i, j, num)
                backtrack(index + 1)
                unfill_cell(i, j)

    backtrack()
    return solutions[0] if solutions else []

grid = [['43', '65', 'x', 'x'], ['42', 'x', '59', 'x'], ['54', '45', 'x', 'x'], ['x', 'x', 'x', '35']]
constraints = [None, 205, 218, None, 219, 220, None, 182]
print(solve_magic_square(grid, constraints))
