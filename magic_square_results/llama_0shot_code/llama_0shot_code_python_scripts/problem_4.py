
import itertools

def magic_square():
    # Define the range of numbers and the empty grid
    num_range = range(20, 40)
    grid = [['21', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

    # Generate all possible permutations of numbers within the range
    for perm in itertools.permutations(num_range, 7):
        # Place the numbers in the grid
        grid[0][1] = perm[0]
        grid[0][2] = perm[1]
        grid[1][0] = perm[2]
        grid[1][1] = perm[3]
        grid[1][2] = perm[4]
        grid[2][0] = perm[5]
        grid[2][1] = perm[6]

        # Check if the grid fulfills the conditions of the magic square
        row_sums = [sum(map(int, row)) for row in grid]
        col_sums = [sum(map(int, col)) for col in zip(*grid)]
        diag_sum = sum(map(int, [grid[0][0], grid[1][1], grid[2][2]]))
        if row_sums == [95, 72, 72] and col_sums == [72, 95, 71] and diag_sum == 71:
            # If it does, store the number and its position as a tuple in a list
            result = [(i, j, val) for i, row in enumerate(grid) for j, val in enumerate(row) if val != 'x']
            return result

    return []

print(magic_square())
