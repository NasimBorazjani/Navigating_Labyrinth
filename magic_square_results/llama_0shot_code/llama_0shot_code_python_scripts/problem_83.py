
def magic_square():
    numbers = list(range(43, 85))
    grid = [['x', 51, 'x', 65], ['x', 'x', 'x', 68], ['x', 'x', 64, 75], ['x', 'x', 'x', 'x']]
    sums = [(None, 240, 226, None), (None, 255, 268, None), (None, 264, None, None)]
    solution = []
    
    def backtrack(row, col):
        if row == len(grid):
            return True
        if col == len(grid[row]):
            return backtrack(row + 1, 0)
        if grid[row][col] != 'x':
            return backtrack(row, col + 1)
        
        for num in numbers:
            grid[row][col] = num
            if check_sums(row, col, num):
                solution.append((row, col, num))
                if backtrack(row, col + 1):
                    return True
                solution.pop()
                grid[row][col] = 'x'
        return False
    
    def check_sums(row, col, num):
        grid[row][col] = num
        for i in range(len(grid)):
            row_sum += num if i == row else grid[i][col]
            col_sum += num if i == col else grid[row][i]
            if row == col:
                diag_sum += num if row == col else grid[i][i]
            if row == len(grid) - 1 - col:
                anti_diag_sum += num if row == len(grid) - 1 - col else grid[i][len(grid) - 1 - i]
        if row_sum != sums[0][row] or col_sum != sums[1][col] or diag_sum != sums[2][0] or anti_diag_sum != sums[2][1]:
            grid[row][col] = 'x'
            return False
        grid[row][col] = num
        return True
    
    backtrack(0, 0)
    return solution

print(magic_square())
