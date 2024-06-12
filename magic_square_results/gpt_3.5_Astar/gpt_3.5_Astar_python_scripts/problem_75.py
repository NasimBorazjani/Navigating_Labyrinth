
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', 'x', 'x', 'x'],
            [28, 33, 'x', 'x'],
            [16, 'x', 'x', 37],
            [36, 18, 7, 23]]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 101, 108, None]
    col_sums = [125, 51, None, None]
    diagonal_sum = 90

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(6, 48))

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, current_grid = heappop(queue)

        # If the grid satisfies all constraints, return the actions taken
        if is_valid_grid(current_grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers
        for i in range(4):
            for j in range(4):
                if current_grid[i][j] == 'x':
                    for num in unique_integers:
                        new_grid = [row[:] for row in current_grid]
                        new_grid[i][j] = num
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def is_valid_grid(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(4):
        if row_sums[i] is not None and sum(grid[i]) != row_sums[i]:
            return False

        col_sum = sum(grid[j][i] for j in range(4))
        if col_sums[i] is not None and col_sum != col_sums[i]:
            return False

    diagonal_sum_top_right = sum(grid[i][i] for i in range(4))
    diagonal_sum_bottom_left = sum(grid[i][3-i] for i in range(4))
    if diagonal_sum_top_right != diagonal_sum or diagonal_sum_bottom_left != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraints that the numbers must be unique and within a specific range, and that the grid must satisfy all constraints
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences can only decrease as we replace 'x' with unique integers
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
    h = 0
    for i in range(4):
        row_sum_diff = abs(sum(grid[i]) - row_sums[i]) if row_sums[i] is not None else 0
        col_sum_diff = abs(sum(grid[j][i] for j in range(4)) - col_sums[i]) if col_sums[i] is not None else 0
        h += row_sum_diff + col_sum_diff

    diagonal_sum_top_right = sum(grid[i][i] for i in range(4))
    diagonal_sum_bottom_left = sum(grid[i][3-i] for i in range(4))
    diagonal_sum_diff = abs(diagonal_sum_top_right - diagonal_sum) + abs(diagonal_sum_bottom_left - diagonal_sum)
    h += diagonal_sum_diff

    return h


print(a_star())
