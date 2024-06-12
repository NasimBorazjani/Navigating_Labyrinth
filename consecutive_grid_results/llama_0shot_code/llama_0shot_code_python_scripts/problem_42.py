
def solve_grid():
    grid = [['46', '80', '90'], ['51', 'x', 'x'], ['x', 'x', 'x']]
    replacements = []
    for value in reversed(range(45, 98)):  # start with the largest number
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 'x':  # if the cell is empty
                    grid[row][col] = str(value)  # try to fill it with the current value
                    if check_grid(grid):  # if the grid is valid after the replacement
                        replacements.append((row, col, value))  # store the replacement
                        break  # move to the next cell
                    else:  # if the grid is not valid
                        grid[row][col] = 'x'  # undo the replacement
            else:  # if a replacement was found and the inner loop was broken
                continue  # move to the next row
            break  # if a replacement was found, break the row loop and try with the next value
        else:  # if no replacement was found after iterating over all rows
            continue  # try with the next value
        break  # if a replacement was found, break the value loop

    return replacements

def check_grid(grid):
    for row in grid:
        if row[0] >= row[1] >= row[2]:  # if the row is not in strictly increasing order
            return False
    for col in range(len(grid)):
        if [row[col] for row in grid][0] >= [row[col] for row in grid][1] >= [row[col] for row in grid][2]:  # if the column is not in strictly increasing order
            return False
    if grid[0][0] >= grid[1][1] >= grid[2][2]:  # if the diagonal is not in strictly increasing order
        return False
    return True
