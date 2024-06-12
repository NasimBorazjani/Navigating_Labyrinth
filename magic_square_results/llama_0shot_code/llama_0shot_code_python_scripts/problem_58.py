
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number hasn't been used yet
        if num in used_nums:
            return False
        # Check the number satisfies the constraints of the cell
        if row in [0, 1] and sum(grid[row][col:col+2]) != 137 + 162:
            return False
        if row in [0, 2] and sum(grid[row][col:col+2]) != 141 + 135:
            return False
        if col in [0, 1] and sum(grid[row][col:row+2]) != 137 + 162:
            return False
        if col in [0, 2] and sum(grid[row][col:row+2]) != 141 + 135:
            return False
        if row == 0 and col == 0 and num + grid[1][2] + grid[2][1] + grid[3][3] != 151:
            return False
        return True

    def backtrack(row, col):
        if row == 4:
            return True
        if col == 4:
            return backtrack(row + 1, 0)
        if grid[row][col] != 'x':
            return backtrack(row, col + 1)

        for num in range(22, 54):
            if is_valid(row, col, num):
                grid[row][col] = num
                used_nums.add(num)
                if backtrack(row, col + 1):
                    return True
                used_nums.remove(num)
                grid[row][col] = 'x'
        return False

    used_nums = set()
    backtrack(0, 0)
    return [(row, col, num) for row in range(4) for col in range(4) if (num := grid[row][col]) != 'x']

grid = [['x', 'x', 'x', '40'],
        ['34', '37', 'x', 'x'],
        ['x', '43', 'x', '22'],
        ['x', 'x', 'x', '47']]

print(solve_magic_square(grid))
