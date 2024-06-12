
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row, column, or square
        for i in range(4):
            if grid[row][i] == str(num) or grid[i][col] == str(num):
                return False
            if grid[i][i] == str(num):
                return False
        return True

    def backtrack(row, col, num_list):
        if num_list == []:
            return True
        num = num_list[0]
        num_list = num_list[1:]
        for i in range(row, 4):
            for j in range(col, 4):
                if grid[i][j] == 'x' and is_valid(i, j, num):
                    grid[i][j] = str(num)
                    if backtrack(i, j, num_list):
                        return True
                    grid[i][j] = 'x'
        return False

    num_list = list(range(36, 93))
    backtrack(0, 0, num_list)
    result = [(i, j, int(grid[i][j])) for i in range(4) for j in range(4) if grid[i][j] != 'x']
    return result

grid = [['39', '47', 'x', 'x'], ['x', 'x', 'x', '40'], ['63', '82', '59', 'x'], ['x', '78', 'x', 'x']]
print(solve_magic_square(grid))
