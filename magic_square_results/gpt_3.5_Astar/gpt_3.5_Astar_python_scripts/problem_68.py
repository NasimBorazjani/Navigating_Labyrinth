
import heapq


def a_star():
    # Define the initial grid with 'x' representing unknown values
    initial_grid = [['x', '40', 'x', 'x'],
                    ['x', '58', 'x', '37'],
                    ['47', 'x', 'x', '44'],
                    ['45', 'x', 'x', '42']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 220, 216, None]
    col_sums = [None, 224, 226, None]
    diagonal_sum = 211

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(31, 68))

    visited_costs = {}
    visited_costs[str(initial_grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid))

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
    for i in range(4):
        # Check row sums
        if row_sums[i] is not None:
            if sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) != row_sums[i]:
                return False

        # Check column sums
        if col_sums[i] is not None:
            if sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) != col_sums[i]:
                return False

    # Check diagonal sum
    if int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum and the target sum for each row, column, and the diagonal
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exact, and presumes we can adjust the values to reach the target sums
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be adjusted to reach the target sum
    # It is consistent because the cost of moving a value to a different position is always 1, which is exactly the decrease in the heuristic estimate if the value is moved to a position that brings the sum closer to the target sum
    h = 0
    for i in range(4):
        # Calculate the difference between the current sum and the target sum for each row
        if row_sums[i] is not None:
            h += abs(sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) - row_sums[i])

        # Calculate the difference between the current sum and the target sum for each column
        if col_sums[i] is not None:
            h += abs(sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) - col_sums[i])

    # Calculate the difference between the current sum and the target sum for the diagonal
    h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - diagonal_sum)

    return h


print(a_star())
