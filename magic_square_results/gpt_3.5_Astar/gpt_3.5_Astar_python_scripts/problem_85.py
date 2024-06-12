
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', 'x', '80', '72'],
            ['44', 'x', '39', 'x'],
            ['x', '70', '64', 'x'],
            ['x', '67', 'x', '42']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 221, 257, None]
    col_sums = [None, 252, 238, None]
    diagonal_sum = 221

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(37, 84))

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, current_grid = heappop(queue)

        # If the grid satisfies all constraints, return the actions taken
        if check_constraints(current_grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers
        for i in range(4):
            for j in range(4):
                if current_grid[i][j] == 'x':
                    for num in unique_integers:
                        new_grid = [row[:] for row in current_grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
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
    if sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x']) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the minimum values that can be placed in the 'x' positions
    # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
    # It is admissible because it underestimates the cost to reach the goal state, as the actual cost will be higher than the heuristic value
    # It is consistent because the cost of moving from one state to another is always at least 1, which is the decrease in the heuristic value
    h = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                h += 37  # Minimum value that can be placed in the 'x' positions
    return h


print(a_star())
