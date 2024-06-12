
import heapq


def a_star():
    # Define the initial grid with some numbers given and others as 'x'
    grid = [['55', 'x', '53', 'x'],
            ['x', '50', '52', 'x'],
            ['x', 'x', 'x', '35'],
            ['x', '62', 'x', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 186, 174, None]
    col_sums = [None, 218, 203, None]
    diagonal_sum = 221

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(28, 65))

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4

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
        for i in range(num_rows):
            for j in range(num_cols):
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
    # Check if the sums of rows, columns, and diagonal match the given constraints
    for i in range(1, 3):
        if row_sums[i] is not None and sum(int(grid[i][j]) for j in range(4)) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4)) != col_sums[i]:
            return False

    if sum(int(grid[i][i]) for i in range(4)) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and that the sum of each row, column, and diagonal must match the given constraints
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences is always less than or equal to the actual cost to reach the goal
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum increase in the sum of a row, column, or diagonal is 1
    h = 0
    for i in range(1, 3):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])

    h += abs(sum(int(grid[i][i]) for i in range(4)) - diagonal_sum)

    return h


print(a_star())
