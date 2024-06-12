
import heapq


def a_star():
    # Define the initial state of the grid, with 'x' representing unknown values
    initial_state = [['x', 'x', '63', 'x'],
                     ['x', '44', 'x', '36'],
                     ['50', 'x', 'x', '60'],
                     ['x', '52', '38', '64']]
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 173, 208, None]
    col_sums = [None, 207, 208, None]
    diagonal_sum = 201

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
                    for num in range(30, 67):
                        new_state = [row[:] for row in state]
                        new_state[i][j] = str(num)
                        new_state_str = str(new_state)
                        new_cost = g + num

                        if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                            visited_costs[new_state_str] = new_cost
                            heappush(queue, (new_cost, new_cost, actions + [(i, j, num)], new_state))

    return None


def check_constraints(state, row_sums, col_sums, diagonal_sum):
    # Check if the state satisfies all constraints
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum([int(state[i][j]) for j in range(len(state[i])) if state[i][j] != 'x']) != row_sums[i]:
                return False

    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            if sum([int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x']) != col_sums[j]:
                return False

    if sum([int(state[i][i]) for i in range(len(state)) if state[i][i] != 'x']) != diagonal_sum:
        return False

    if sum([int(state[i][len(state)-1-i]) for i in range(len(state)) if state[i][len(state)-1-i] != 'x']) != diagonal_sum:
        return False

    return True


print(a_star())
