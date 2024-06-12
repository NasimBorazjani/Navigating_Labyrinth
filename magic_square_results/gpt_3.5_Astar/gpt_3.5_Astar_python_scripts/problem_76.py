
import heapq


def a_star():
    # Define the initial grid with some numbers given and others as 'x'
    grid = [['26', '38', '27', 'x'],
            ['x', 'x', 'x', '19'],
            ['x', '43', 'x', 'x'],
            ['42', 'x', '34', '20']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 94, 109, None]
    col_sums = [None, 128, 80, None]
    diagonal_sum = 99

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

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 'x':
                    for num in range(6, 48):
                        new_grid = [row[:] for row in grid]
                        new_grid[row][col] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(row, col, num)], new_grid))
    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
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
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and that the sum of each row, column, and diagonal must be as specified
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences is always less than or equal to the actual cost to reach the goal
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a different number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
    h = 0
    for i in range(1, 3):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])
    h += abs(sum(int(grid[i][i]) for i in range(4)) - diagonal_sum)
    return h


print(a_star())