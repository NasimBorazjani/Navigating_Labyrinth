
import heapq


def a_star():
    # Define the initial state of the grid, with 'x' representing unknown values
    initial_state = [['61', 'x', '50', 'x'],
                     ['x', 'x', 'x', 'x'],
                     ['68', '40', '57', 'x'],
                     ['x', '42', 'x', 'x']]
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 247, 238, None]
    col_sums = [None, 188, 234, None]
    diagonal_sum = 215

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
                    for num in range(35, 77):
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
        # Check row sums
        if row_sums[i] is not None:
            if sum([int(state[i][j]) for j in range(4)]) != row_sums[i]:
                return False
        # Check column sums
        if col_sums[i] is not None:
            if sum([int(state[j][i]) for j in range(4)]) != col_sums[i]:
                return False
    # Check diagonal sum
    if int(state[0][3]) + int(state[1][2]) + int(state[2][1]) + int(state[3][0]) != diagonal_sum:
        return False
    return True


def heuristic(state, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that each number must be unique and presumes we can replace 'x' with any number in the given range
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the sum is 1, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        # Calculate row differences
        if row_sums[i] is not None:
            h += abs(sum([int(state[i][j]) for j in range(4)]) - row_sums[i])
        # Calculate column differences
        if col_sums[i] is not None:
            h += abs(sum([int(state[j][i]) for j in range(4)]) - col_sums[i])
    # Calculate diagonal difference
    h += abs(int(state[0][3]) + int(state[1][2]) + int(state[2][1]) + int(state[3][0]) - diagonal_sum)
    return h


print(a_star())
