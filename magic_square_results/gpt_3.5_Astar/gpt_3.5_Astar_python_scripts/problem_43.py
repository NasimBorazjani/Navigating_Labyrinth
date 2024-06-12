
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '51', '39', 'x'],
            ['x', 'x', '48', '37'],
            ['54', 'x', 'x', 'x'],
            ['x', 'x', 'x', '53']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 180, 202, None]
    col_sums = [None, 212, 185, None]
    diagonal_sum = 193

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(35, 62))

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
        if row_sums[i] is not None and sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) != row_sums[i]:
            return False

        if col_sums[i] is not None and sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) != col_sums[i]:
            return False

    if sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x']) != diagonal_sum:
        return False

    if sum([int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x']) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can be placed in the 'x' positions
    # This heuristic relaxes the constraints that the sum of the numbers in the rows, columns, and diagonal must be exact, and that each number must be unique
    # It is admissible because it never overestimates the cost to reach the goal, as the actual sum of the numbers in the 'x' positions will be greater than or equal to the heuristic estimate
    # It is consistent because the estimated cost of the next node is higher if a larger number is placed in an 'x' position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the minimum possible value that can be placed in an 'x' position is 35
    h = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                h += 35
    return h


print(a_star())
