
import heapq


def a_star():
    # Define the initial grid with the given numbers and 'x's
    grid = [['45', '53', 'x', 'x'],
            ['x', 'x', 'x', 'x'],
            ['47', 'x', 'x', 'x'],
            ['35', 'x', '52', 'x']]

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 166, 165, None]
    col_sums = [None, 173, 166, None]
    diagonal_sum = 131

    visited_costs = {}
    visited_costs[str(grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))

    while queue:
        _, g, actions, state = heappop(queue)

        # If the grid is filled with unique integers and satisfies the given constraints, return the actions taken
        if is_valid_solution(state, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x's with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in range(23, 55):
                        new_grid = [row[:] for row in state]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

    return None


def is_valid_solution(grid, row_sums, col_sums, diagonal_sum):
    # Check if all numbers in the grid are unique
    flat_grid = [num for row in grid for num in row]
    if len(set(flat_grid)) != len(flat_grid):
        return False

    # Check if the row sums are correct
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum([int(num) for num in grid[i] if num != 'x']) != row_sums[i]:
                return False

    # Check if the column sums are correct
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            if sum([int(grid[i][j]) for i in range(len(grid)) if grid[i][j] != 'x']) != col_sums[j]:
                return False

    # Check if the diagonal sum is correct
    if sum([int(grid[i][i]) for i in range(len(grid)) if grid[i][i] != 'x']) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and that the sums of rows, columns, and diagonal must be correct
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum amount that can be added to the sum is 1
    h = 0
    # Calculate the heuristic based on the differences between the current sum and the target sum for each row
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            h += abs(sum([int(num) for num in grid[i] if num != 'x']) - row_sums[i])
    # Calculate the heuristic based on the differences between the current sum and the target sum for each column
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            h += abs(sum([int(grid[i][j]) for i in range(len(grid)) if grid[i][j] != 'x']) - col_sums[j])
    # Calculate the heuristic based on the differences between the current sum and the target sum for the diagonal
    h += abs(sum([int(grid[i][i]) for i in range(len(grid)) if grid[i][i] != 'x']) - diagonal_sum)

    return h


print(a_star())
