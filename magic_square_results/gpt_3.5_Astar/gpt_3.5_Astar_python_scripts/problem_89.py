
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', 'x', 'x', 'x'],
            ['24', 'x', '27', '41'],
            ['22', '37', 'x', 'x'],
            ['29', 'x', 'x', '46']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 139, 178, None]
    col_sums = [None, 187, 186, None]
    diagonal_sum = 160

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(22, 69))

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, current_grid = heappop(queue)

        # If the current grid satisfies all constraints, return the actions taken
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
    # Check if the sums of rows, columns, and diagonal match the constraints
    for i in range(4):
        if row_sums[i] is not None:
            if sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) != row_sums[i]:
                return False

        if col_sums[i] is not None:
            if sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) != col_sums[i]:
                return False

    if sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x']) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the minimum values that can be placed in the unknown cells
    # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
    # It is admissible because it underestimates the cost to reach the goal state, as the actual sum of the numbers in the grid will be higher than the heuristic estimate
    # It is consistent because the cost of moving from one state to another is at least 1, and the heuristic estimate for the goal state is 0
    h = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                h += 22  # Minimum value that can be placed in the unknown cell
    return h


print(a_star())
