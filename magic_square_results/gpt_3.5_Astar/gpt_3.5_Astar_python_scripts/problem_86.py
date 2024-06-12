
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '48', '64', '67'],
            ['x', '50', '61', 'x'],
            ['42', 'x', 'x', '74'],
            ['x', 'x', '72', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 213, 197, None]
    col_sums = [None, 214, 240, None]
    diagonal_sum = 215

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(37, 84))

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid satisfies all constraints, return the actions taken
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
        if row_sums[i] is not None and sum(int(grid[i][j]) for j in range(4)) != row_sums[i]:
            return False

        if col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4)) != col_sums[i]:
            return False

    if sum(int(grid[i][i]) for i in range(4)) != diagonal_sum:
        return False

    if sum(int(grid[i][3-i]) for i in range(4)) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences can only decrease as we replace 'x' with unique integers
    # It is consistent because the estimated cost of the next node is higher if a 'x' is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum value that can be added to the grid is the largest unique integer, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])

        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])

    h += abs(sum(int(grid[i][i]) for i in range(4)) - diagonal_sum)
    h += abs(sum(int(grid[i][3-i]) for i in range(4)) - diagonal_sum)

    return h


print(a_star())
