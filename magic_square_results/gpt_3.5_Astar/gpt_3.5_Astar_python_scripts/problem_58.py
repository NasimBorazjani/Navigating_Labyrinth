
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', 'x', 'x', '40'],
            ['34', '37', 'x', 'x'],
            ['x', '43', 'x', '22'],
            ['x', 'x', 'x', '47']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 141, 135, None]
    col_sums = [None, 137, 162, None]
    diagonal_sum = 151

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid satisfies all the constraints, return the actions taken
        if check_constraints(grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers in the given range
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(22, 54):
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the sums of rows and columns match the given constraints
    for i in range(4):
        if row_sums[i] is not None:
            if sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) != row_sums[i]:
                return False
        if col_sums[i] is not None:
            if sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) != col_sums[i]:
                return False

    # Check if the sum of the diagonal matches the given constraint
    diagonal_sum_calculated = sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x'])
    if diagonal_sum_calculated != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and presumes we can replace 'x' with any number in the given range
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) - col_sums[i])
    h += abs(sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x']) - diagonal_sum)

    return h


print(a_star())
