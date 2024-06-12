
import heapq


def a_star():
    # Define the initial grid with the given numbers and 'x's
    grid = [['36', '47', 'x', 'x'],
            ['x', '28', '40', 'x'],
            ['x', '33', 'x', 'x'],
            ['50', 'x', 'x', 'x']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 152, 158, None]
    col_sums = [None, 156, 185, None]
    diagonal_sum = 165

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, state = heappop(queue)

        # If the grid is filled with unique integers and satisfies the constraints, return the actions taken
        if is_valid_solution(state, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x's with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in range(28, 65):
                        new_grid = [row[:] for row in state]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def is_valid_solution(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid is filled with unique integers
    unique_nums = set()
    for row in grid:
        for num in row:
            if num != 'x':
                unique_nums.add(int(num))
    if len(unique_nums) != 16:
        return False

    # Check if the row sums are correct
    for i in range(1, 3):
        if row_sums[i] is not None:
            if sum(int(num) for num in grid[i]) != row_sums[i]:
                return False

    # Check if the column sums are correct
    for j in range(1, 3):
        if col_sums[j] is not None:
            if sum(int(grid[i][j]) for i in range(4)) != col_sums[j]:
                return False

    # Check if the diagonal sum is correct
    if int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers must be unique and that the sums must be correct, presuming that we can adjust the numbers to reach the target sums
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be adjusted to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if the sum of a row, column, or diagonal is further from the target sum, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to a sum is 1, which is exactly the decrease in the heuristic estimate
    h = 0
    # Calculate the heuristic based on the differences between the current sums and the target sums
    for i in range(1, 3):
        if row_sums[i] is not None:
            h += abs(sum(int(num) for num in grid[i]) - row_sums[i])
    for j in range(1, 3):
        if col_sums[j] is not None:
            h += abs(sum(int(grid[i][j]) for i in range(4)) - col_sums[j])
    h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - diagonal_sum)
    return h


print(a_star())
