
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '46', 'x', '22'],
            ['x', 'x', '36', '15'],
            ['47', 'x', 'x', '25'],
            ['x', 'x', '53', 'x']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 118, 120, None]
    col_sums = [None, 146, 168, None]
    diagonal_sum = 91

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
                    for num in range(13, 55):
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
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences can only decrease as we get closer to the goal
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum increase in the sum of the row, column, or diagonal is 1
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
