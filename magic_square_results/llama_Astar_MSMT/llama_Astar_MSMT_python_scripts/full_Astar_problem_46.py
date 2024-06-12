
import heapq


def initialize():
    # Define the initial state of the grid, with 'x' representing unknown numbers
    grid = [['x', 'x', 'x', 'x'],
            ['x', '37', 'x', '41'],
            ['48', 'x', 'x', 'x'],
            ['49', 'x', '46', '38']]

    # Encoding other variables given in the problem
    num_rows = 4
    num_cols = 4
    given_sums_rows = [None, 180, 176, None]
    given_sums_cols = [None, 151, 189, None]
    given_sum_diag = 184

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[grid] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
    queue = [(0, 0, [], grid)]

    return grid, num_rows, num_cols, given_sums_rows, given_sums_cols, given_sum_diag, visited_costs, queue


def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial grid, dimensions of the grid, and given sums for rows, columns, and diagonal)
    grid, num_rows, num_cols, given_sums_rows, given_sums_cols, given_sum_diag, visited_costs, queue = initialize()

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, replacements, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        # The goal state is when the sum of all numbers in the grid is as low as possible, and the sum of all rows, columns, and the diagonal equals the given amounts
        if all(sum(row) == given_sums_rows[i] for i, row in enumerate(state)) and \
           all(sum(col) == given_sums_cols[i] for i, col in enumerate(zip(*state))) and \
           sum(state[i][i] for i in range(num_rows)) == given_sum_diag:
            return replacements

        # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
        for row_ind in range(num_rows):
            for col_ind in range(num_cols):
                if state[row_ind][col_ind] == 'x':
                    # Generate the new state
                    new_state = [list(row[:]) for row in state]
                    for num in range(35, 62):
                        # Check if the new state would be valid, ie the new state must maintain the constraints on the sums of rows, columns, and the diagonal
                        new_state[row_ind][col_ind] = num
                        if all(sum(row) == given_sums_rows[i] for i, row in enumerate(new_state)) and \
                           all(sum(col) == given_sums_cols[i] for i, col in enumerate(zip(*new_state))) and \
                           sum(new_state[i][i] for i in range(num_rows)) == given_sum_diag:
                            new_state = tuple(tuple(row) for row in new_state)
                            # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                            new_cost = g + 1

                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(state, new_state), new_cost, replacements + [(row_ind, col_ind, num)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current state and the goal state, for each row, column, and diagonal
    # This heuristic relaxes the constraint that the only way to replace an 'x' is with a unique integer from the given range
    # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
    # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is equal to the goal numbers), which is equal to the cost of reaching the successor node
    # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
    h = 0
    for s_row, g_row in zip(state, goal):
        for s_num, g_num in zip(s_row, g_row):
            h += abs(s_num - g_num)
    return h


print(a_star())
