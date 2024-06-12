
import heapq


def a_star():
    # Define the initial state of the magic square problem, with the grid as a 2D list and the constraints on the sums of rows, columns, and diagonal
    initial_grid = [['30', 'x', 'x', '37'],
                    ['41', '56', 'x', 'x'],
                    ['x', 'x', '29', '55'],
                    ['x', 'x', 'x', '42']]
    row_sums = [None, 196, 162, None]
    col_sums = [None, 208, 157, None]
    diagonal_sum = 166

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    num_values = 32

    visited_costs = {}
    visited_costs[str(initial_grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # Unpack the grid to check if it meets the constraints
        grid_values = [int(val) if val != 'x' else None for row in grid for val in row]

        # Check if the grid meets the constraints
        if check_constraints(grid_values, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the given range
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 'x':
                    for val in range(28, 60):
                        new_grid = [row[:] for row in grid]
                        new_grid[row][col] = str(val)
                        new_cost = g + val

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(grid_values), new_cost, actions + [(row, col, val)], new_grid))

    return None


def check_constraints(grid_values, row_sums, col_sums, diagonal_sum):
    # Check if the grid values meet the constraints on row sums, column sums, and diagonal sum
    for i in range(1, 3):
        if row_sums[i] is not None and sum(grid_values[i*num_cols:(i+1)*num_cols]) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(grid_values[i:num_values:num_cols]) != col_sums[i]:
            return False
    if sum(grid_values[0:num_values:num_cols+1]) != diagonal_sum:
        return False
    return True


def heuristic(grid_values):
    # An admissible and consistent heuristic is the sum of the differences between the current value and the closest constraint value for each unknown value
    # This heuristic relaxes the constraint that the sum of the numbers in the grid must meet the constraints, and presumes we can adjust the unknown values to meet the constraints
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if the value is further from the constraint value, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum value that can be added to the value is 1, which is exactly the decrease in the heuristic estimate
    h = 0
    for i, val in enumerate(grid_values):
        if val is None:
            closest_row_sum = min([abs(row_sum - sum(grid_values[j*num_cols:(j+1)*num_cols]) if row_sum is not None else 0 for j, row_sum in enumerate(row_sums) if j != 0])
            closest_col_sum = min([abs(col_sum - sum(grid_values[j:num_values:num_cols]) if col_sum is not None else 0 for j, col_sum in enumerate(col_sums) if j != 0])
            closest_diagonal_sum = abs(diagonal_sum - sum(grid_values[0:num_values:num_cols+1]))
            h += min(closest_row_sum, closest_col_sum, closest_diagonal_sum)
    return h


print(a_star())
