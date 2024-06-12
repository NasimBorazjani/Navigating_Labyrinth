
import heapq


def a_star():
    # Define the initial state of the grid, with 'x' representing unknown values
    initial_state = [['x', 'x', 'x', '40'],
                     ['x', 'x', 'x', 'x'],
                     ['49', '61', 'x', 'x'],
                     ['33', '48', 'x', '54']]
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 269, 234, None]
    col_sums = [None, 259, 252, None]
    diagonal_sum = 178

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
                    for num in range(33, 85):
                        new_state = [row[:] for row in state]
                        new_state[i][j] = str(num)
                        new_cost = g + num

                        if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                            visited_costs[str(new_state)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))
    return None


def check_constraints(state, row_sums, col_sums, diagonal_sum):
    # Check if the state satisfies all constraints
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum([int(num) for num in state[i] if num != 'x']) != row_sums[i]:
                return False

    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            col_sum = sum([int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x'])
            if col_sum != col_sums[j]:
                return False

    diagonal_sum_calculated = sum([int(state[i][j]) for i, j in zip(range(len(state)), range(len(state) - 1, -1, -1)) if state[i][j] != 'x'])
    if diagonal_sum_calculated != diagonal_sum:
        return False

    return True


def heuristic(state, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it underestimates the cost to reach the goal state, as the sum of the differences can only decrease as we replace 'x' with numbers
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum value that can be added to the grid is 84, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            row_sum_calculated = sum([int(num) for num in state[i] if num != 'x'])
            h += abs(row_sums[i] - row_sum_calculated)

    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            col_sum_calculated = sum([int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x'])
            h += abs(col_sums[j] - col_sum_calculated)

    diagonal_sum_calculated = sum([int(state[i][j]) for i, j in zip(range(len(state)), range(len(state) - 1, -1, -1)) if state[i][j] != 'x'])
    h += abs(diagonal_sum - diagonal_sum_calculated)

    return h


print(a_star())
