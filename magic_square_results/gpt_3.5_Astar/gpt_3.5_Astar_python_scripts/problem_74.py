
import heapq


def a_star():
    # Define the initial grid with some numbers given and others as 'x'
    grid = [['15', '20', 'x', 'x'],
            ['6', 'x', 'x', '40'],
            ['x', 'x', '29', 'x'],
            ['46', '42', '34', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 97, 107, None]
    col_sums = [None, 99, 126, None]
    diagonal_sum = 124

    # Define the range of unique integers to fill the 'x' positions
    unique_integers = list(range(6, 48))

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
    # Check if the sums of rows, columns, and diagonal match the constraints
    for i in range(4):
        if row_sums[i] is not None:
            if sum(int(grid[i][j]) for j in range(4)) != row_sums[i]:
                return False

        if col_sums[i] is not None:
            if sum(int(grid[j][i]) for j in range(4)) != col_sums[i]:
                return False

    if sum(int(grid[i][i]) for i in range(4)) != diagonal_sum:
        return False

    if sum(int(grid[i][3-i]) for i in range(4)) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum and the target sum for each row, column, and diagonal
    # This heuristic relaxes the constraint that the numbers must be unique and presumes we can fill the grid with any numbers in the given range
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum amount that can be added to the sum is 1, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])

        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])

    h += abs(sum(int(grid[i][i]) for i in range(4)) - diagonal_sum)
    h += abs(sum(int(grid[i][3-i]) for i in range(4)) - diagonal_sum)

    return h


print(a_star())
