
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '51', 'x', '65'],
            ['x', 'x', 'x', '68'],
            ['x', 'x', '64', '75'],
            ['x', 'x', 'x', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 255, 268, None]
    col_sums = [None, 240, 226, None]
    diagonal_sum = 264

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(43, 85))

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid is filled and satisfies all constraints, return the actions taken
        if is_filled(grid) and check_constraints(grid, row_sums, col_sums, diagonal_sum):
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


def is_filled(grid):
    # Check if the grid is completely filled with numbers
    for row in grid:
        if 'x' in row:
            return False
    return True


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(4):
        if row_sums[i] is not None and sum(int(num) for num in grid[i]) != row_sums[i]:
            return False

        if col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4)) != col_sums[i]:
            return False

    if sum(int(grid[i][i]) for i in range(4)) != diagonal_sum:
        return False

    if sum(int(grid[i][3-i]) for i in range(4)) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(int(num) for num in grid[i]) - row_sums[i])

        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])

    h += abs(sum(int(grid[i][i]) for i in range(4)) - diagonal_sum)
    h += abs(sum(int(grid[i][3-i]) for i in range(4)) - diagonal_sum)

    return h


print(a_star())
