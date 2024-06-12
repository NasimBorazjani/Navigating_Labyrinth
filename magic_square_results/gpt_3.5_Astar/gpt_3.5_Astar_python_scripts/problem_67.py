
import heapq


def a_star():
    # Define the initial grid with 'x's and given numbers
    grid = [['x', '59', '52', '54'],
            ['x', 'x', 'x', '62'],
            ['x', '58', 'x', 'x'],
            ['x', 'x', '63', '42']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 187, 203, None]
    col_sums = [None, 204, 206, None]
    diagonal_sum = 199

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

        # Generate all possible actions from the current grid, which includes replacing 'x's with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(31, 68):
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the sums of rows, columns, and diagonal match the given constraints
    for i in range(4):
        if row_sums[i] is not None:
            if sum(int(grid[i][j]) for j in range(4) if grid[i][j] != 'x') != row_sums[i]:
                return False

        if col_sums[i] is not None:
            if sum(int(grid[j][i]) for j in range(4) if grid[j][i] != 'x') != col_sums[i]:
                return False

    if sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x') != diagonal_sum:
        return False

    if sum(int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x') != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the minimum values that can be placed in the 'x' positions
    # This heuristic relaxes the constraints that the sum of rows, columns, and diagonal must match the given constraints
    # It is admissible because it underestimates the cost to reach the goal, as the actual cost will be higher than the heuristic cost
    # It is consistent because the cost of moving from one state to another is always at least 1, which is the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                h += 31
    return h


print(a_star())
