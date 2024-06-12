
import heapq


def a_star():
    # Define the initial grid with 'x' representing unknown values
    grid = [['x', 'x', 'x', 'x'],
            ['x', 41, 17, 'x'],
            ['x', 'x', 13, 43],
            [9, 24, 27, 11]]

    # Define the constraints for the rows, columns, and diagonal
    row_sums = [None, 116, 124, None]
    col_sums = [None, 144, 76, None]
    diagonal_sum = 75

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(6, 48))

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
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 'x':
                    for num in unique_integers:
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = num
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the sums of rows and columns match the constraints
    for i in range(4):
        if row_sums[i] is not None and sum(grid[i]) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(row[i] for row in grid) != col_sums[i]:
            return False

    # Check if the sum of the diagonal matches the constraint
    if grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0] != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it underestimates the cost to reach the goal state, as the sum of the differences can only decrease as we replace 'x' with unique integers
    # It is consistent because the estimated cost of the next node is higher if a 'x' is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum value that can be added to the grid is the largest unique integer, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(grid[i]) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(row[i] for row in grid) - col_sums[i])

    h += abs(grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0] - diagonal_sum)

    return h


print(a_star())
