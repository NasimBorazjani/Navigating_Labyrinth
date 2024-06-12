
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '35', 'x', 'x'],
            ['43', 'x', '41', '30'],
            ['x', '46', '33', 'x'],
            ['x', '49', 'x', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 158, 131, None]
    col_sums = [None, 174, 158, None]
    diagonal_sum = 156

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(24, 51))

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
    # Check row sums
    for i in range(1, 3):
        if row_sums[i] is not None and sum(int(grid[i][j]) for j in range(4)) != row_sums[i]:
            return False

    # Check column sums
    for j in range(1, 3):
        if col_sums[j] is not None and sum(int(grid[i][j]) for i in range(4)) != col_sums[j]:
            return False

    # Check diagonal sum
    if int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be corrected by replacing 'x' with a unique integer
    # It's consistent because the estimated cost of the next node is higher if 'x' is replaced with a larger integer, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum value that can be added to the grid is 50, which is exactly the decrease in the heuristic estimate
    h = 0
    # Calculate the heuristic based on row sums
    for i in range(1, 3):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])

    # Calculate the heuristic based on column sums
    for j in range(1, 3):
        if col_sums[j] is not None:
            h += abs(sum(int(grid[i][j]) for i in range(4)) - col_sums[j])

    # Calculate the heuristic based on diagonal sum
    h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - diagonal_sum)

    return h


print(a_star())
