
import heapq


def a_star():
    # Define the initial state of the magic square grid, with 'x' representing unknown values
    initial_state = [['x', 'x', '37', '31'],
                     ['x', 'x', 'x', '51'],
                     ['x', 'x', '16', 'x'],
                     ['41', 'x', '43', '42']]
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 159, 114, None]
    col_sums = [None, 147, 128, None]
    diagonal_sum = 150

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
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] == 'x':
                    for num in range(13, 55):
                        new_state = [row[:] for row in state]
                        new_state[row][col] = str(num)
                        new_state_str = str(new_state)
                        new_cost = g + num

                        if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                            visited_costs[new_state_str] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(row, col, num)], new_state))
    return None


def check_constraints(state, row_sums, col_sums, diagonal_sum):
    # Check if the state satisfies all constraints
    for i in range(4):
        if row_sums[i] is not None and sum(int(state[i][j]) for j in range(4) if state[i][j] != 'x') != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(int(state[j][i]) for j in range(4) if state[j][i] != 'x') != col_sums[i]:
            return False
    if sum(int(state[i][i]) for i in range(4) if state[i][i] != 'x') != diagonal_sum:
        return False
    if sum(int(state[i][3-i]) for i in range(4) if state[i][3-i] != 'x') != diagonal_sum:
        return False
    return True


def heuristic(state, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be corrected by replacing 'x' with a unique integer
    # It's consistent because the estimated cost of the next node is higher if 'x' is replaced with a number that increases the sum, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be decreased from the sum is 1, which is exactly the decrease in the heuristic estimate for the goal state
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(int(state[i][j]) for j in range(4) if state[i][j] != 'x') - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(int(state[j][i]) for j in range(4) if state[j][i] != 'x') - col_sums[i])
    h += abs(sum(int(state[i][i]) for i in range(4) if state[i][i] != 'x') - diagonal_sum)
    h += abs(sum(int(state[i][3-i]) for i in range(4) if state[i][3-i] != 'x') - diagonal_sum)
    return h


print(a_star())
