
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '65', '49', '35'],
            ['40', 'x', '52', 'x'],
            ['x', 'x', '34', 'x'],
            ['x', 'x', '55', '61']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 192, 173, None]
    col_sums = [None, 191, 190, None]
    diagonal_sum = 180

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid satisfies all constraints, return the actions taken
        if check_constraints(grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(30, 67):
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(len(grid)):
        row_sum = sum(int(num) for num in grid[i] if num != 'x')
        if row_sums[i] is not None and row_sum != row_sums[i]:
            return False

        col_sum = sum(int(grid[j][i]) for j in range(len(grid)) if grid[j][i] != 'x')
        if col_sums[i] is not None and col_sum != col_sums[i]:
            return False

    diagonal_sum_top_right = sum(int(grid[i][j]) for i, j in zip(range(len(grid)), range(len(grid) - 1, -1, -1)) if grid[i][j] != 'x'
    diagonal_sum_bottom_left = sum(int(grid[i][j]) for i, j in zip(range(len(grid)), range(len(grid))) if grid[i][j] != 'x'
    if diagonal_sum_top_right != diagonal_sum or diagonal_sum_bottom_left != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum and the target sum for each row, column, and diagonal
    # The heuristic relaxes the constraint that the numbers must be unique and that the sum of the numbers in the grid must be minimized
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
    h = 0
    for i in range(len(grid)):
        row_sum = sum(int(num) for num in grid[i] if num != 'x')
        if row_sums[i] is not None:
            h += abs(row_sum - row_sums[i])

        col_sum = sum(int(grid[j][i]) for j in range(len(grid)) if grid[j][i] != 'x')
        if col_sums[i] is not None:
            h += abs(col_sum - col_sums[i])

    diagonal_sum_top_right = sum(int(grid[i][j]) for i, j in zip(range(len(grid)), range(len(grid) - 1, -1, -1)) if grid[i][j] != 'x'
    diagonal_sum_bottom_left = sum(int(grid[i][j]) for i, j in zip(range(len(grid)), range(len(grid))) if grid[i][j] != 'x'
    h += abs(diagonal_sum_top_right - diagonal_sum) + abs(diagonal_sum_bottom_left - diagonal_sum)

    return h


print(a_star())
