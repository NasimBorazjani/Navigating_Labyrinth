
def solve_magic_square(grid):
    def backtrack(row=0, col=0):
        if row == 4:  # all cells are filled in
            return grid
        if col == 4:  # move to the next row
            return backtrack(row + 1, 0)
        if grid[row][col] != 'x':  # this cell is already filled in
            return backtrack(row, col + 1)

        for num in range(13, 55):  # try out different numbers
            grid[row][col] = num
            if (col == 0 and sum(grid[row]) != 118) or \
               (col == 1 and sum(grid[row]) != 120) or \
               (row == 0 and sum(grid[col]) != 46) or \
               (row == 1 and sum(grid[col]) != 36) or \
               (row == 2 and sum(grid[col]) != 53) or \
               (row == 3 and sum(grid[col]) != 22) or \
               (row == 0 and col == 1 and sum(grid[i][i] for i in range(4)) != 91):
                grid[row][col] = 'x'  # undo the move
            else:
                result = backtrack(row, col + 1)
                if result:  # a solution is found
                    return result
                grid[row][col] = 'x'  # undo the move
        return None

    return [(row, col, num) for row in range(4) for col in range(4) for num in range(13, 55)
            if grid[row][col] == num and backtrack()]

grid = [['x', '46', 'x', '22'],
        ['x', 'x', '36', '15'],
        ['47', 'x', 'x', '25'],
        ['x', 'x', '53', 'x']]

print(solve_magic_square(grid))
