
import heapq


def a_star():
    # Define the initial grid with unknown values represented as 'x'
    grid = [['x', '46', 'x', 'x'],
            ['44', 'x', 'x', '53'],
            ['39', 'x', 'x', 'x'],
            ['x', 'x', 'x', '38']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 201, 190, None]
    col_sums = [None, 198, 175, None]
    diagonal_sum = 193

    # Define the range of unique integers to fill the grid
    unique_integers = list(range(34, 61))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], grid)]

    # While there are un-visited states
    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the state is valid and satisfies all constraints, return the actions taken
        if is_valid(state, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers
        for i in range(4):
            for j in range(4):
                if state[i][j] == 'x':
                    for num in unique_integers:
                        new_state = [row[:] for row in state]
                        new_state[i][j] = str(num)
                        new_cost = g + num

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))

    return None


def is_valid(grid, row_sums, col_sums, diagonal_sum):
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
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum([int(grid[i][j]) for j in range(4) if grid[i][j] != 'x']) - row_sums[i])

        if col_sums[i] is not None:
            h += abs(sum([int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']) - col_sums[i])

    h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - diagonal_sum)

    return h


print(a_star())
