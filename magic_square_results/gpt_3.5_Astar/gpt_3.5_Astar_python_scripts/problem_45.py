
import heapq


def a_star():
    # Define the initial state of the magic square problem, with the grid represented as a 2D list of integers and 'x's
    initial_state = [['x', 50, 'x', 'x'],
                     [58, 'x', 'x', 'x'],
                     ['x', 49, 'x', 59],
                     [39, 41, 'x', 'x']]
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    row_sums = [None, 183, 190, None]
    col_sums = [None, 177, 196, None]
    diagonal_sum = 188

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

        # Generate all possible actions from the current state, which includes replacing 'x's with unique integers in the given range
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in range(35, 62):
                        new_state = [row[:] for row in state]
                        new_state[i][j] = num
                        new_cost = g + num

                        if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                            visited_costs[str(new_state)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))
    return None


def check_constraints(state, row_sums, col_sums, diagonal_sum):
    # Check if the sums of rows, columns, and diagonal match the given constraints
    for i in range(4):
        if row_sums[i] is not None and sum(state[i]) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(row[i] for row in state) != col_sums[i]:
            return False
    if state[0][3] + state[1][2] + state[2][1] + state[3][0] != diagonal_sum:
        return False
    return True


def heuristic(state, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it underestimates the cost to reach the goal state, as the sum of the differences can only decrease as we replace 'x's with numbers
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum increase in the sum is 1
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(state[i]) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(row[i] for row in state) - col_sums[i])
    h += abs(state[0][3] + state[1][2] + state[2][1] + state[3][0] - diagonal_sum)
    return h


print(a_star())
