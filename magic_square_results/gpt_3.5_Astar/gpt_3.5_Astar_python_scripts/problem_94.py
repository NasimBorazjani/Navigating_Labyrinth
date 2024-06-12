
import heapq


def a_star():
    # Define the initial grid with some numbers given and others as 'x'
    grid = [['48', 'x', 'x', 'x'],
            ['54', 'x', 'x', 'x'],
            ['x', '64', '44', '83'],
            ['82', '68', '51', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 270, 234, None]
    col_sums = [None, 267, 236, None]
    diagonal_sum = 301

    # Define the range of unique integers to replace 'x' in the grid
    unique_integers = list(range(41, 93))

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
    # This heuristic relaxes the constraint that the numbers must be unique, and the sum of the numbers in the grid must match the target sums
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the grid is by using the smallest unique integer, which is exactly the heuristic estimate for the goal state
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
