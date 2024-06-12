
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', 'x', 'x', '67'],
            ['62', 'x', '32', '77'],
            ['66', 'x', '34', 'x'],
            ['x', 'x', '73', '35']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 220, 184, None]
    col_sums = [None, 239, 192, None]
    diagonal_sum = 199

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid satisfies all the constraints, return the actions taken
        if is_valid(grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers in the given range
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(30, 87):
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def is_valid(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all the constraints
    # Check row sums
    for i in range(1, 3):
        if row_sums[i] is not None:
            if sum(int(grid[i][j]) for j in range(4)) != row_sums[i]:
                return False

    # Check column sums
    for j in range(1, 3):
        if col_sums[j] is not None:
            if sum(int(grid[i][j]) for i in range(4)) != col_sums[j]:
                return False

    # Check diagonal sum
    if int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers must be unique and that the sum of the numbers in the grid must be minimized
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It's consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the sum is 1
    h = 0
    # Check row sums
    for i in range(1, 3):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])

    # Check column sums
    for j in range(1, 3):
        if col_sums[j] is not None:
            h += abs(sum(int(grid[i][j]) for i in range(4)) - col_sums[j])

    # Check diagonal sum
    h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - diagonal_sum)

    return h


print(a_star())
