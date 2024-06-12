
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    initial_grid = [['x', 'x', 'x', '39'],
                    ['28', 'x', 'x', 'x'],
                    ['x', '11', '33', 'x'],
                    ['18', '20', '38', '35']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 114, 84, None]
    col_sums = [None, 77, 110, None]
    diagonal_sum = 98

    visited_costs = {}
    visited_costs[str(initial_grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid satisfies all the constraints, return the actions taken
        if check_constraints(grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(9, 41):
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it underestimates the cost to reach the goal state, as the sum of the differences is always less than or equal to the actual cost to reach the goal
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a different number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum difference that can be reduced is 1
    h = 0
    for i in range(len(grid)):
        # Calculate the sum of each row and compare it to the target sum
        if row_sums[i] is not None:
            row_sum = sum(int(num) for num in grid[i])
            h += abs(row_sum - row_sums[i])

        # Calculate the sum of each column and compare it to the target sum
        if col_sums[i] is not None:
            col_sum = sum(int(grid[row][i]) for row in range(len(grid)))
            h += abs(col_sum - col_sums[i])

    # Calculate the sum of the diagonal from top right to bottom left and compare it to the target sum
    diagonal_sum_calculated = sum(int(grid[i][3 - i]) for i in range(len(grid)))
    h += abs(diagonal_sum_calculated - diagonal_sum)

    return h


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all the constraints
    for i in range(len(grid)):
        # Check if the sum of each row matches the target sum
        if row_sums[i] is not None:
            row_sum = sum(int(num) for num in grid[i])
            if row_sum != row_sums[i]:
                return False

        # Check if the sum of each column matches the target sum
        if col_sums[i] is not None:
            col_sum = sum(int(grid[row][i]) for row in range(len(grid)))
            if col_sum != col_sums[i]:
                return False

    # Check if the sum of the diagonal from top right to bottom left matches the target sum
    diagonal_sum_calculated = sum(int(grid[i][3 - i]) for i in range(len(grid)))
    if diagonal_sum_calculated != diagonal_sum:
        return False

    return True


print(a_star())
