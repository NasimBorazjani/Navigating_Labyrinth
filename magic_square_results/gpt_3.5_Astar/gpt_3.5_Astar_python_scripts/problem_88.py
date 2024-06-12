
import heapq


def a_star():
    # Define the initial grid with the given numbers and 'x's
    grid = [['27', '48', 'x', 'x'],
            ['x', 'x', '63', 'x'],
            ['28', 'x', '33', '26'],
            ['x', 'x', 'x', '39']]

    # Define the constraints for the rows, columns, and diagonal
    row_constraints = [None, 190, 154, None]
    col_constraints = [183, 202, None, None]
    diagonal_constraint = 183

    # Define the range of unique integers to replace 'x's
    unique_integers = list(range(22, 69))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], grid)]

    # While there are un-visited states
    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the grid is filled and satisfies all constraints, return the actions taken
        if is_valid_solution(state, row_constraints, col_constraints, diagonal_constraint):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x's with unique integers
        for i in range(4):
            for j in range(4):
                if state[i][j] == 'x':
                    for num in unique_integers:
                        new_state = [row[:] for row in state]
                        new_state[i][j] = str(num)
                        new_cost = g + num

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(i, j, num)], new_state))

    return None


def is_valid_solution(grid, row_constraints, col_constraints, diagonal_constraint):
    # Check if the grid satisfies all constraints
    for i in range(4):
        # Check row constraints
        if row_constraints[i] is not None:
            if sum(int(grid[i][j]) for j in range(4)) != row_constraints[i]:
                return False

        # Check column constraints
        if col_constraints[i] is not None:
            if sum(int(grid[j][i]) for j in range(4)) != col_constraints[i]:
                return False

    # Check diagonal constraint
    diagonal_sum = sum(int(grid[i][j]) for i, j in zip(range(4), range(3, -1, -1)))
    if diagonal_sum != diagonal_constraint:
        return False

    return True


def heuristic(grid, row_constraints, col_constraints, diagonal_constraint):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and their respective constraints
    h = 0
    for i in range(4):
        if row_constraints[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_constraints[i])

        if col_constraints[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_constraints[i])

    diagonal_sum = sum(int(grid[i][j]) for i, j in zip(range(4), range(3, -1, -1)))
    h += abs(diagonal_sum - diagonal_constraint)

    return h


print(a_star())
