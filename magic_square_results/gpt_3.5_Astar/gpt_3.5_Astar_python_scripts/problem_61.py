
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '31', 'x', 'x'],
            ['x', 'x', 'x', 'x'],
            ['x', 'x', '42', 'x'],
            ['x', '49', '30', '27']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 156, 156, None]
    col_sums = [None, 135, 149, None]
    diagonal_sum = 149

    # Define the range of unique integers to replace 'x' in the grid
    unique_integers = list(range(23, 55))

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
        for i in range(len(grid)):
            for j in range(len(grid[0])):
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
    for i in range(len(grid)):
        if row_sums[i] is not None:
            if sum(int(num) for num in grid[i] if num != 'x') != row_sums[i]:
                return False

    # Check column sums
    for j in range(len(grid[0])):
        if col_sums[j] is not None:
            if sum(int(grid[i][j]) for i in range(len(grid)) if grid[i][j] != 'x') != col_sums[j]:
                return False

    # Check diagonal sum
    diagonal_sum_calculated = sum(int(grid[i][j]) for i, j in zip(range(len(grid)), range(len(grid[0]) - 1, -1, -1)) if grid[i][j] != 'x'
    if diagonal_sum_calculated != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the missing values in the grid
    # The heuristic relaxes the constraints that the sum of rows, columns, and diagonal must be as specified, and that each number must be unique
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the missing values is the minimum possible sum to satisfy the constraints
    # It is consistent because the estimated cost of the next node is higher if a missing value is replaced with a larger number, or equal if replaced with a smaller number, which is exactly the cost of reaching the successor node
    h = 0
    for row in grid:
        for num in row:
            if num == 'x':
                h += min(range(23, 55))
    return h


print(a_star())
