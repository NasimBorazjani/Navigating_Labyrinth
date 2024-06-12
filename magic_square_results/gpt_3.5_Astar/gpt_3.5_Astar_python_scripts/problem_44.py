
import heapq


def a_star():
    # Define the initial grid with the given constraints
    initial_grid = [['x', 'x', '39', 'x'],
                    ['x', 'x', 'x', '43'],
                    ['x', 'x', 'x', '47'],
                    ['46', '49', 'x', '53']]
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 177, 160, None]
    col_sums = [None, 188, 188, None]
    diagonal_sum = 173

    visited_costs = {}
    visited_costs[str(initial_grid)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid))

    while queue:
        _, g, actions, grid = heappop(queue)

        # If the grid satisfies all the constraints, return the actions taken
        if check_constraints(grid, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers in the given range
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(35, 62):
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num

                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))
    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all the constraints
    # Check row sums
    for i in range(1, 3):
        if row_sums[i] is not None:
            if sum(int(grid[i][j]) for j in range(4) if grid[i][j] != 'x') != row_sums[i]:
                return False

    # Check column sums
    for j in range(1, 3):
        if col_sums[j] is not None:
            if sum(int(grid[i][j]) for i in range(4) if grid[i][j] != 'x') != col_sums[j]:
                return False

    # Check diagonal sum
    diagonal_sum_calculated = sum(int(grid[i][j]) for i in range(4) for j in range(4) if i + j == 3 and grid[i][j] != 'x')
    if diagonal_sum_calculated != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and within the given range
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences is always less than or equal to the actual cost to reach the goal
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a different number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
    h = 0
    # Calculate the difference between the current sum and the target sum for each row
    for i in range(1, 3):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4) if grid[i][j] != 'x') - row_sums[i])

    # Calculate the difference between the current sum and the target sum for each column
    for j in range(1, 3):
        if col_sums[j] is not None:
            h += abs(sum(int(grid[i][j]) for i in range(4) if grid[i][j] != 'x') - col_sums[j])

    # Calculate the difference between the current sum and the target sum for the diagonal
    diagonal_sum_calculated = sum(int(grid[i][j]) for i in range(4) for j in range(4) if i + j == 3 and grid[i][j] != 'x')
    h += abs(diagonal_sum_calculated - diagonal_sum)

    return h


print(a_star())
