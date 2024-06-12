
def magic_square():
    grid = [['45', '53', 'x', 'x'],
            ['x', 'x', 'x', 'x'],
            ['47', 'x', 'x', 'x'],
            ['35', 'x', '52', 'x']]
    sums = [(173, 166, None), (None, 165, None)]
    total_sum = 131
    solution = []

    def check_number(row, col, num):
        for i in range(4):
            if grid[row][i] == str(num) or grid[i][col] == str(num):
                return False
        if row == col:
            for i in range(4):
                if grid[i][i] == str(num):
                    return False
        if row + col == 3:
            for i in range(4):
                if grid[i][3 - i] == str(num):
                    return False
        return True

    def backtrack(row=0, col=0):
        if row == 4:
            row, col = 0, 0
            while col < 4:
                if grid[row][col] == 'x':
                    break
                col += 1
            else:
                return True
        if col == 4:
            col = 0
            row += 1
        if grid[row][col] != 'x':
            return backtrack(row, col + 1)
        for num in range(23, 55):
            if check_number(row, col, num):
                grid[row][col] = str(num)
                if backtrack(row, col + 1):
                    return True
                grid[row][col] = 'x'
        return False

    if backtrack():
        for row in range(4):
            for col in range(4):
                if grid[row][col] != 'x':
                    solution.append((row, col, int(grid[row][col])))
    return solution

print(magic_square())
