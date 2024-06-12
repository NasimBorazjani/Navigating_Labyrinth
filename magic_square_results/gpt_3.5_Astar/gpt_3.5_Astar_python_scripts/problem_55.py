
import heapq


def a_star():
    # Define the initial grid with the given numbers and 'x's
    grid = [['46', 'x', '58', '45'],
            ['x', 'x', '54', 'x'],
            ['x', 'x', 'x', 'x'],
            ['28', '53', '34', 'x']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 168, 168, None]
    col_sums = [None, 162, 195, None]
    diagonal_sum = 168

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, state = heappop(queue)

        # If the grid satisfies all the constraints, return the actions taken
        if check_constraints(state, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the given range
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] == 'x':
                    for num in range(28, 60):
                        new_grid = [row[:] for row in state]
                        new_grid[row][col] = str(num)
                        new_state = str(new_grid)
                        new_cost = g + num

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(row, col, num)], new_grid))
    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all the constraints
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
    # This heuristic relaxes the constraint that the numbers must be unique and that the sum of each row, column, and diagonal must be as specified
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences is always less than or equal to the actual cost to reach the goal
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
    h = 0
    for i in range(1, 3):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])
    h += abs(sum(int(grid[i][i]) for i in range(4)) - diagonal_sum)
    return h


print(a_star())
