
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', 'x', '22', '23'],
            ['x', 'x', '15', '25'],
            ['31', 'x', 'x', 'x'],
            ['12', '36', 'x', '13']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 94, 111, None]
    col_sums = [None, 116, 78, None]
    diagonal_sum = 70

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


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all the constraints
    # Check row sums
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum([int(grid[i][j]) for j in range(len(grid[i]) if grid[i][j] != 'x']) != row_sums[i]:
                return False

    # Check column sums
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            if sum([int(grid[i][j]) for i in range(len(grid) if grid[i][j] != 'x']) != col_sums[j]:
                return False

    # Check diagonal sum
    diagonal_sum_calculated = sum([int(grid[i][i]) for i in range(len(grid) if grid[i][i] != 'x'])
    if diagonal_sum_calculated != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be corrected by replacing 'x' with a unique integer
    # It's consistent because the estimated cost of the next node is higher if 'x' is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum value that can be placed in a position is 40, which is exactly the decrease in the heuristic estimate
    h = 0
    # Calculate the heuristic based on row sums
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            current_sum = sum([int(grid[i][j]) for j in range(len(grid[i]) if grid[i][j] != 'x'])
            h += abs(row_sums[i] - current_sum)

    # Calculate the heuristic based on column sums
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            current_sum = sum([int(grid[i][j]) for i in range(len(grid) if grid[i][j] != 'x'])
            h += abs(col_sums[j] - current_sum)

    # Calculate the heuristic based on diagonal sum
    diagonal_sum_calculated = sum([int(grid[i][i]) for i in range(len(grid) if grid[i][i] != 'x'])
    h += abs(diagonal_sum - diagonal_sum_calculated)

    return h


print(a_star())
