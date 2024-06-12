
import heapq


def a_star():
    # Define the initial grid with some numbers given and others as 'x'
    grid = [['42', '53', '43', '72'],
            ['x', '82', '54', 'x'],
            ['x', '62', '44', 'x'],
            ['x', 'x', 'x', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 253, 221, None]
    col_sums = [None, 277, 204, None]
    diagonal_sum = 252

    # Define the range of unique integers that can be placed in the grid
    unique_integers = list(range(37, 84))

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
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and presumes we can place any number in any position
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if a number is placed in a position that increases the difference, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is by 1, which is exactly the cost of reaching the successor node
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
