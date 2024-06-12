
import heapq


def initialize():
    # Define the initial state of the magic square, with 'x' represented as None
    initial_state = [[None, None, None, 39], [28, None, None, None], [None, 11, 33, None], [18, 20, 38, 35]]
    # Define the goal state of the magic square, with the sum of each row, column, and diagonal
    goal_state = (None, 77, 110, None, None, 114, 84, None, 98)

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    sum_rows = [None, 114, 84, None]
    sum_cols = [None, 77, 110, None]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(row[:] for row in initial_state)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    return initial_state, goal_state, num_rows, num_cols, sum_rows, sum_cols, visited_costs, queue


def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal board and dimensions of the puzzle board)
    initial_state, goal_state, num_rows, num_cols, sum_rows, sum_cols, visited_costs, queue = initialize()

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state by checking if the sums of rows, columns and diagonal match the goal state
        if (None if row is None else sum(row) for row in state) == goal_state:
            return actions

        # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer within the given range
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] is None:
                    # Generate the new state
                    new_state = [row[:] for row in state]
                    for number in range(9, 41):
                        if number not in new_state:
                            new_state[row][col] = number
                            # Update the sums of rows and columns
                            new_state[row] = [number if val is None else val for val in new_state[row]]
                            new_state = tuple(tuple(row) for row in new_state)
                            # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                            new_cost = g + 1

                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, number)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current sums and the goal sums
    # This heuristic relaxes the constraint that each number can be in the final grid only once
    # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be replaced at least once
    # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number's sum matches the sum in the new position but not in the old one), which is equal to the cost of reaching the successor node
    # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
    h = 0
    for row in range(len(state)):
        if state[row] is not None:
            h += abs(sum(state[row]) - goal[row])
    return h


print(a_star())
