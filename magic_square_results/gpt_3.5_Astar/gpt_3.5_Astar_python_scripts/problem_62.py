
import heapq


def a_star():
    # Define the initial grid with 'x' representing unknown values
    grid = [['x', 'x', 'x', 'x'],
            ['40', '39', '32', '53'],
            ['46', 'x', '58', 'x'],
            ['x', 'x', '43', '51']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 164, 210, None]
    col_sums = [None, 199, 194, None]
    diagonal_sum = 197

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(30, 67))

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid is filled and satisfies all constraints, return the actions taken
        if is_valid(grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 'x':
                    for num in unique_integers:
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def is_valid(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(4):
        # Check row sums
        if row_sums[i] is not None:
            if sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) != row_sums[i]:
                return False

        # Check column sums
        if col_sums[i] is not None:
            if sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) != col_sums[i]:
                return False

    # Check diagonal sum
    if int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum and the target sum for each row, column, and the diagonal
    # This heuristic relaxes the constraint that the sum of the numbers in the grid must be minimized
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It's consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the grid is by using the smallest unique integer that won't cause a constraint violation, which is exactly the heuristic estimate for the goal state
    h = 0
    for i in range(4):
        # Calculate the difference between the current sum and the target sum for each row
        if row_sums[i] is not None:
            h += abs(sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) - row_sums[i])

        # Calculate the difference between the current sum and the target sum for each column
        if col_sums[i] is not None:
            h += abs(sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) - col_sums[i])

    # Calculate the difference between the current sum and the target sum for the diagonal
    h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - diagonal_sum)

    return h


print(a_star())
