
import heapq


def a_star():
    # Define the initial grid with 'x's and known numbers
    grid = [['x', 'x', 'x', '60'],
            ['72', 'x', 'x', 'x'],
            ['63', '70', 'x', 'x'],
            ['61', '75', 'x', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 231, 259, None]
    col_sums = [None, 247, 236, None]
    diagonal_sum = 234

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(35, 77))

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, current_grid = heappop(queue)

        # If the grid is filled and satisfies all constraints, return the actions taken
        if is_filled(current_grid) and check_constraints(current_grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x's with unique integers
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


def is_filled(grid):
    # Check if the grid is completely filled with numbers
    for row in grid:
        if 'x' in row:
            return False
    return True


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(4):
        if row_sums[i] is not None and sum([int(num) for num in grid[i] if num != 'x']) != row_sums[i]:
            return False

        if col_sums[i] is not None and sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) != col_sums[i]:
            return False

    if sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x']) != diagonal_sum:
        return False

    if sum([int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x']) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and presumes we can fill the grid with any numbers in the given range
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences can only decrease as we replace 'x's with numbers
    # It's consistent because the estimated cost of the next node is higher if a 'x' is replaced with a number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie the number replaced) as the maximum amount that can be added to the sum is the number replaced, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum([int(num) for num in grid[i] if num != 'x']) - row_sums[i])

        if col_sums[i] is not None:
            h += abs(sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) - col_sums[i])

    h += abs(sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x']) - diagonal_sum)
    h += abs(sum([int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x']) - diagonal_sum)

    return h


print(a_star())
