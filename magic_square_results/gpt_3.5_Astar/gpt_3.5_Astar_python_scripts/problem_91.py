
import heapq


def a_star():
    # Define the initial state of the grid, with 'x' representing unknown values
    initial_grid = [['62', 'x', 'x', 'x'],
                    ['x', '35', '60', 'x'],
                    ['x', '39', 'x', '54'],
                    ['x', '55', '34', 'x']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 217, 193, None]
    col_sums = [None, 177, 192, None]
    diagonal_sum = 149

    visited_costs = {}
    visited_costs[str(initial_grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid satisfies all the constraints, return the actions taken
        if check_constraints(grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the given range
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(22, 69):
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all the constraints
    for i in range(4):
        if row_sums[i] is not None and sum(int(grid[i][j]) for j in range(4)) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4)) != col_sums[i]:
            return False

    if (int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0])) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It's consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum amount that can be added to the grid is 1, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])

    if (int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0])) != diagonal_sum:
        h += abs((int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0])) - diagonal_sum)

    return h


print(a_star())
