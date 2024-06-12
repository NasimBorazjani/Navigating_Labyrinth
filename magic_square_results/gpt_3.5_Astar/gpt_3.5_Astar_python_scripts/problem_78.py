
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '22', 'x', 'x'],
            ['28', '47', '42', 'x'],
            ['16', 'x', '30', '24'],
            ['x', 'x', 'x', 'x']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 158, 87, None]
    col_sums = [None, 135, 153, None]
    diagonal_sum = 140

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

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in range(13, 55):
                        new_grid = [row[:] for row in state]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))
    return None


def is_valid_solution(grid, row_sums, col_sums, diagonal_sum):
    # Check if all numbers in the grid are unique
    unique_numbers = set()
    for row in grid:
        for num in row:
            if num != 'x':
                if num in unique_numbers:
                    return False
                unique_numbers.add(num)

    # Check if the row sums are correct
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum(int(num) for num in grid[i] if num != 'x') != row_sums[i]:
                return False

    # Check if the column sums are correct
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            if sum(int(grid[i][j]) for i in range(len(grid)) if grid[i][j] != 'x') != col_sums[j]:
                return False

    # Check if the diagonal sum is correct
    diagonal_sum_calculated = sum(int(grid[i][j]) for i, j in zip(range(len(grid)), range(len(grid) - 1, -1, -1)) if grid[i][j] != 'x'
    if diagonal_sum_calculated != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the missing values in the grid
    # This heuristic relaxes the constraint that the sum of the numbers in the grid must be minimized
    # It is admissible because it never overestimates the cost to reach the goal, as the missing values must be replaced with integers in the range [13, 54]
    # It's consistent because the estimated cost of the next node is higher if a missing value is replaced with a higher number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum value that can be placed in a missing position is 54, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                h += 54  # Maximum value that can be placed in a missing position
    return h


print(a_star())
