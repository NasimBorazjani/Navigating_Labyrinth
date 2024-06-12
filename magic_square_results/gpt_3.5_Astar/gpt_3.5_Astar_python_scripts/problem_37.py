
import heapq


def a_star():
    # Define the initial state of the grid, with unknown values represented as 'x'
    initial_state = [['48', 'x', 'x'], ['x', 'x', 'x'], ['x', '49', 'x']]
    # Define the goal sums for each row, column, and diagonal
    goal_sums = [209, 150, 169]
    # Define the range of unique integers that can be placed in the grid
    unique_integers = list(range(40, 90))

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # If the sum of each row, column, and diagonal matches the goal sums, return the actions taken
        if check_sums(state, goal_sums):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers
        for i in range(3):
            for j in range(3):
                if state[i][j] == 'x':
                    for num in unique_integers:
                        new_state = [row[:] for row in state]
                        new_state[i][j] = str(num)
                        new_cost = g + num

                        if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                            visited_costs[str(new_state)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, num)], new_state))

    return None


def check_sums(state, goal_sums):
    # Check if the sum of each row, column, and diagonal in the grid matches the goal sums
    row_sums = [sum([int(num) for num in row if num != 'x']) for row in state]
    col_sums = [sum([int(state[i][j]) for i in range(3) if state[i][j] != 'x']) for j in range(3)]
    diag_sum1 = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
    diag_sum2 = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])

    return row_sums == goal_sums[0] and col_sums == goal_sums[1] and diag_sum1 == diag_sum2 == goal_sums[2]


def heuristic(state, goal_sums):
    # An admissible and consistent heuristic is the sum of the differences between the current sum and the goal sum for each row, column, and diagonal
    # This heuristic relaxes the constraint that each number must be unique and presumes we can place any number in any position
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the goal
    # It is consistent because the estimated cost of the next node is higher if a number is placed in a position that increases the difference, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum decrease in the difference is 1
    row_sums = [sum([int(num) for num in row if num != 'x']) for row in state]
    col_sums = [sum([int(state[i][j]) for i in range(3) if state[i][j] != 'x']) for j in range(3]
    diag_sum1 = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
    diag_sum2 = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])

    h = 0
    for i in range(3):
        h += abs(row_sums[i] - goal_sums[0])
        h += abs(col_sums[i] - goal_sums[1])
    h += abs(diag_sum1 - diag_sum2 - goal_sums[2])

    return h


print(a_star())
