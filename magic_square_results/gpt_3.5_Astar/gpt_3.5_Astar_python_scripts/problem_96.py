
import heapq


def a_star():
    # Define the initial state of the grid, with 'x' representing unknown values
    initial_state = [['x', 'x', 'x', 'x'],
                     ['x', 52, 20, 'x'],
                     [41, 13, 'x', 'x'],
                     [54, 'x', 16, 11]]
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 105, 115, None]
    col_sums = [None, 148, 109, None]
    diagonal_sum = 134

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # If the state satisfies all constraints, return the actions taken
        if check_constraints(state, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the given range
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in range(11, 63):
                        new_state = [row[:] for row in state]
                        new_state[i][j] = num
                        new_cost = g + num

                        if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                            visited_costs[str(new_state)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))
    return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be equal to the target sum
    # It is admissible because it underestimates the cost to reach the goal state, as the sum of the differences is always less than or equal to the actual cost to reach the goal state
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
    h = 0
    for i in range(len(state)):
        # Calculate the sum of each row and compare it to the target sum
        if row_sums[i] is not None:
            h += abs(sum(state[i]) - row_sums[i])
        # Calculate the sum of each column and compare it to the target sum
        if col_sums[i] is not None:
            col_sum = sum(row[i] for row in state)
            h += abs(col_sum - col_sums[i])
    # Calculate the sum of the diagonal from top right to bottom left and compare it to the target sum
    diagonal_sum_calculated = sum(state[i][j] for i, j in zip(range(len(state)), range(len(state) - 1, -1, -1)))
    h += abs(diagonal_sum_calculated - diagonal_sum)
    return h


def check_constraints(state, row_sums, col_sums, diagonal_sum):
    # Check if the state satisfies all constraints
    for i in range(len(state)):
        # Check if the sum of each row matches the target sum
        if row_sums[i] is not None and sum(state[i]) != row_sums[i]:
            return False
        # Check if the sum of each column matches the target sum
        col_sum = sum(row[i] for row in state)
        if col_sums[i] is not None and col_sum != col_sums[i]:
            return False
    # Check if the sum of the diagonal from top right to bottom left matches the target sum
    diagonal_sum_calculated = sum(state[i][j] for i, j in zip(range(len(state)), range(len(state) - 1, -1, -1)))
    if diagonal_sum_calculated != diagonal_sum:
        return False
    return True


print(a_star())
