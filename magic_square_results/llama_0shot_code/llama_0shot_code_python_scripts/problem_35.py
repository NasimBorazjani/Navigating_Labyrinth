
def solve_magic_square(grid):
    def is_valid(x, y, n):
        # Check the number has not already been used in the grid
        for i in range(3):
            for j in range(3):
                if grid[i][j] == n:
                    return False
        # Check the number does not already exist in the same row or column
        for i in range(3):
            if grid[x][i] == n or grid[i][y] == n:
                return False
        # Check the number does not exist in the same diagonal
        if x == y:
            for i in range(3):
                if grid[i][i] == n:
                    return False
        return True

    def backtrack(x, y, sum1, sum2, sum3, total):
        if x == 3:
            if sum1 == 153 and sum2 == 186 and sum3 == 188 and total == 405:
                return grid
            return None
        if y == 3:
            return backtrack(x + 1, 0, sum1 - grid[x][2], sum2 - grid[x][1], sum3 - grid[x][0], total - grid[x][2])
        if grid[x][y] == 'x':
            for n in range(40, 90):
                if is_valid(x, y, n):
                    grid[x][y] = n
                    new_sum1 = sum1 + n if y == 0 else sum1
                    new_sum2 = sum2 + n if x == 0 else sum2
                    new_sum3 = sum3 + n if x == y else sum3
                    result = backtrack(x, y + 1, new_sum1, new_sum2, new_sum3, total + n)
                    if result is not None:
                        return result
            grid[x][y] = 'x'  # Undo the choice if it leads to no solution
        else:
            result = backtrack(x, y + 1, sum1, sum2, sum3, total)
            if result is not None:
                return result

    result = backtrack(0, 0, 0, 0, 0, 0)
    return [(i, j, result[i][j]) for i in range(3) for j in range(3) if result[i][j] != 'x']

grid = [['x', 'x', 'x'], ['80', '48', 'x'], ['x', 'x', 'x']]
print(solve_magic_square(grid))
