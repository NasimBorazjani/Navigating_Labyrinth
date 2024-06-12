
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', 'x', 'x', 'x'],
            ['x', '46', 'x', '41'],
            ['x', '57', '55', 'x'],
            ['x', '37', 'x', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 179, 190, None]
    col_sums = [None, 179, 194, None]
    diagonal_sum = 205

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(34, 61))

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
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(4):
        if row_sums[i] is not None and sum(int(grid[i][j]) for j in range(4) if grid[i][j] != 'x') != row_sums[i]:
            return False

        if col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4) if grid[j][i] != 'x') != col_sums[i]:
            return False

    if sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x') != diagonal_sum:
        return False

    if sum(int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x') != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and presumes we can reach the target sum by adjusting the numbers in the grid
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each difference must be adjusted to reach the target sum
    # It's consistent because the estimated cost of the next node is higher if a number is replaced with another number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4) if grid[i][j] != 'x') - row_sums[i])

        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4) if grid[j][i] != 'x') - col_sums[i])

    h += abs(sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x') - diagonal_sum)
    h += abs(sum(int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x') - diagonal_sum)

    return h


print(a_star())
