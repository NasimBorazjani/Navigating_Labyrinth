
def solve_grid(grid):
    replacements = []
    numbers = list(range(40, 88))

    # Step 1: Fill in the missing values
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                grid[i][j] = numbers.pop(0)

    # Step 2: Ensure the numbers are increasing or decreasing
    for i in range(3):
        if grid[i][0] > grid[i][1] > grid[i][2]:
            grid[i][0], grid[i][2] = grid[i][2], grid[i][0]
        elif grid[i][0] < grid[i][1] < grid[i][2]:
            pass
        else:
            grid[i][1], grid[i][2] = grid[i][2], grid[i][1]

    for j in range(3):
        if grid[0][j] > grid[1][j] > grid[2][j]:
            grid[0][j], grid[2][j] = grid[2][j], grid[0][j]
        elif grid[0][j] < grid[1][j] < grid[2][j]:
            pass
        else:
            grid[1][j], grid[2][j] = grid[2][j], grid[1][j]

    # Step 3: Calculate the initial sum
    initial_sum = sum(grid[0]) + sum(grid[i][2] for i in range(3)) + grid[0][0] + grid[2][2]

    # Step 4: Find better replacements
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in numbers:
                    grid[i][j] = num
                    new_sum = sum(grid[0]) + sum(grid[i][2] for i in range(3)) + grid[0][0] + grid[2][2]
                    if new_sum < initial_sum:
                        replacements.append((i, j, num))
                        initial_sum = new_sum
                    else:
                        grid[i][j] = 'x'

    # Step 5: Return the replacements
    return replacements

# Test the function
grid = [['x', 'x', '65'], ['x', '47', '56'], ['48', '44', 'x']]
print(solve_grid(grid))
