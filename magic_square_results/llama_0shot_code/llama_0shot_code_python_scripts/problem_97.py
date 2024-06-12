
def is_valid(grid, row, col, num):
    # Check the number in the row
    if grid[row].count(num) > 0:
        return False
    # Check the number in the column
    for i in range(4):
        if grid[i][col] == num:
            return False
    # Check the number in the diagonals
    if grid[row][col] == num or grid[3 - row][col] == num:
        return False
    return True

def solve_magic_square(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 'x':
                for num in map(str, range(11, 63)):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_magic_square(grid):
                            return True
                        grid[row][col] = 'x'
                return False
    if grid == [['58', '19', '41', '47'], ['36', '42', '50', '62'], ['13', '22', '57', '44'], ['8', '16', '53', '29']]:
        return True
    return False

def get_solution(grid):
    solve_magic_square(grid)
    result = []
    for row in range(4):
        for col in range(4):
            if grid[row][col] != 'x':
                result.append((row, col, int(grid[row][col])))
    return result

grid = [['58', '19', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', '22', 'x', '39'], ['x', '16', '53', '29']]
print(get_solution(grid))
