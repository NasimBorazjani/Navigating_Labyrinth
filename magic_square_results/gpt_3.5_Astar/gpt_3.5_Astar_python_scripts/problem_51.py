
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', 'x', '27', '9'],
            ['21', 'x', 'x', '15'],
            ['x', '16', '31', 'x'],
            ['11', 'x', '32', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 72, 97, None]
    col_sums = [None, 102, 100, None]
    diagonal_sum = 46

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4

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
    # Check if the grid satisfies all constraints
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum(int(grid[i][j]) for j in range(len(grid[i])) if grid[i][j] != 'x') != row_sums[i]:
                return False

    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            if sum(int(grid[i][j]) for i in range(len(grid)) if grid[i][j] != 'x') != col_sums[j]:
                return False

    if sum(int(grid[i][i]) for i in range(len(grid)) if grid[i][i] != 'x') != diagonal_sum:
        return False

    if sum(int(grid[i][len(grid)-1-i]) for i in range(len(grid)) if grid[i][len(grid)-1-i] != 'x') != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the missing values in the grid
    # The heuristic relaxes the constraints that the sum of rows, columns, and diagonal must be exact, and presumes we can fill the missing values with the minimum possible values
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a missing value is replaced with a higher value, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the minimum possible value that can be placed in the missing position is 9, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                h += 9
    return h


print(a_star())
