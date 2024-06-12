
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    initial_grid = [['x', 'x', '32', 'x'],
                    ['37', '61', 'x', '54'],
                    ['x', 'x', 'x', '62'],
                    ['x', '30', 'x', '44']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 211, 161, None]
    col_sums = [None, 143, 170, None]
    diagonal_sum = 146

    # Define the range of unique integers to fill in the grid
    unique_integers = list(range(22, 69))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[str(initial_grid)] = 0

    # Initialize a priority queue of states not yet visited, with the initial grid as the first element
    queue = [(0, 0, [], initial_grid)]

    while queue:
        _, g, actions, grid = heapq.heappop(queue)

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
                            heapq.heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))

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
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be corrected by replacing 'x' with a unique integer
    # It's consistent because the estimated cost of the next node is higher if a 'x' is replaced with a larger integer, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie the integer replaced) as the maximum value that can be added to the sum is the unique integer used to replace 'x'
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) - row_sums[i])

        if col_sums[i] is not None:
            h += abs(sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) - col_sums[i])

    h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - diagonal_sum)

    return h


print(a_star())
