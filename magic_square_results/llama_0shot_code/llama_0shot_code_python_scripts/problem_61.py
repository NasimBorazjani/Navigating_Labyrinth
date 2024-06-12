
def solve_magic_square():
    # Initialize the grid and the list of used numbers
    grid = [[0]*4 for _ in range(4)]
    used = [False]*32

    # Fill in the numbers that must be in the grid
    grid[0][1] = 31
    grid[2][2] = 42
    grid[3][1] = 49
    grid[3][2] = 30
    grid[3][3] = 27

    # Function to try placing a number in the grid
    def try_place(row, col, num):
        # If the number has been used or the cell is already filled, return False
        if used[num-23] or grid[row][col]:
            return False

        # Place the number in the grid
        used[num-23] = True
        grid[row][col] = num

        # Check if the sums of the rows, columns, and diagonal are correct
        if (sum(grid[0]) != 156 or sum(grid[1]) != 156 or sum(grid[2]) != 135 or
            sum(grid[3]) != 149 or sum(grid[i][i] for i in range(4)) != 149):
            # If not, undo the fill
            used[num-23] = False
            grid[row][col] = 0
            return False

        return True

    # Function to solve the grid
    def solve(row=0, col=0):
        # If all cells are filled, return the solution
        if row == 4:
            return [(i, j, grid[i][j]) for i in range(4) for j in range(4) if grid[i][j]]

        # If the current cell is already filled, move to the next cell
        if grid[row][col]:
            return solve(row, col+1) if col < 3 else solve(row+1, 0)

        # Try to fill the current cell with a number from the range 23 to 54
        for num in range(23, 55):
            if try_place(row, col, num):
                # If the fill is successful, move to the next cell
                result = solve(row, col+1) if col < 3 else solve(row+1, 0)
                if result is not None:
                    return result
                # If the fill leads to a solution, return the solution

                # Undo the fill
                used[num-23] = False
                grid[row][col] = 0

        return None

    return solve()

print(solve_magic_square())
