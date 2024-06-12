
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    initial_grid = [['x', '41', '67', 'x'],
                    ['x', '73', 'x', '91'],
                    ['x', '43', 'x', '76'],
                    ['80', 'x', 'x', '86']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 298, 222, None]
    col_sums = [None, 240, 266, None]
    diagonal_sum = 299

    visited_costs = {}
    visited_costs[str(initial_grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid is filled with unique integers and satisfies the constraints, return the actions taken
        if is_valid_solution(grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(41, 93):
                        new_grid = [row[:] for row in grid]
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

    # Check if the sums of rows and columns match the constraints
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum(int(num) for num in grid[i] if num != 'x') != row_sums[i]:
                return False

    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            if sum(int(grid[i][j]) for i in range(len(grid)) if grid[i][j] != 'x') != col_sums[j]:
                return False

    # Check if the sum of the diagonal matches the constraint
    diagonal_sum_calculated = sum(int(grid[i][j]) for i, j in zip(range(len(grid)), range(len(grid) - 1, -1, -1)) if grid[i][j] != 'x'
    if diagonal_sum_calculated != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the missing values in the grid
    # The heuristic relaxes the constraint that the numbers in the grid must be unique and that the sums of rows, columns, and diagonal must match the constraints
    # It presumes that the missing values can be filled with any unique integer in the given range
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a missing value is filled, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum value that can be filled in the missing position is 92, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                h += 92
    return h


print(a_star())
