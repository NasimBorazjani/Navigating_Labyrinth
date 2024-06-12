
def magic_square():
    # The total sum of the magic square
    total_sum = 405

    # The sum of each row, column, and diagonal
    row_sum = 191
    col_sum = 200
    diag_sum = 201

    # The number of missing numbers
    missing_count = 9

    # The sum of the missing numbers
    missing_sum = total_sum - row_sum - col_sum - diag_sum

    # The range of possible numbers
    num_range = range(48, 78)

    # The result list
    result = []

    # The grid
    grid = [[0, 0, 66], [0, 0, 0], [0, 0, 0]]

    # Function to check if placing a number at a certain position violates the conditions
    def check(row, col, num):
        new_grid = [[grid[i][j] if i != row or j != col else num for j in range(3)] for i in range(3)]
        sums = [sum(new_grid[i]) for i in range(3)] + [sum(new_grid[i][j] for i in range(3)) for j in range(3)] + [new_grid[0][2] + new_grid[1][1] + new_grid[2][0]]
        return sums == [row_sum] * 3 + [col_sum] * 3 + [diag_sum]

    # Function to solve the problem
    def solve(index):
        if index == missing_count:
            return True
        for num in num_range:
            row, col = divmod(index, 3)
            if grid[row][col] == 0 and check(row, col, num):
                grid[row][col] = num
                result.append((row, col, num))
                if solve(index + 1):
                    return True
                result.pop()
                grid[row][col] = 0
        return False

    # Solve the problem
    solve(0)

    return result

print(magic_square())
