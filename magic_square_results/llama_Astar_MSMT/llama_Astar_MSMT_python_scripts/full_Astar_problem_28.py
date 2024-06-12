
import heapq


def initialize():
    # Define the initial state of the magic square, with 'x' represented as None
    initial_state = [[51, None, None], [None, None, None], [None, None, None]]
   
    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3
    goal_col_sums = [107, 124, 108]


    visited_costs = {}
    visited_costs[initial_state] = 0


    # The information we must encode for each state includes the current state of the magic square and the total cost so far
    # No actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]
  
    return initial_state, num_rows, num_cols, goal_col_sums, visited_costs, queue
  
def a_star():
   
    initial_state, num_rows, num_cols, goal_col_sums, visited_costs, queue = initialize()


    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)


        # Check if the current state is the goal state
        # The goal state is when the sum of all the numbers in the grid is as low as possible, while satisfying the given conditions
        if all(sum(row) == goal_col_sums[i] for i, row in enumerate(state)):
            return actions


        # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
        for row_ind in range(num_rows):
            for col_ind in range(num_cols):
                if state[row_ind][col_ind] is None:
                    # Generate the new state
                    new_state = [list(row[:]) for row in state]
                    # The unique integer to replace 'x' is the next integer in the range 26 to 65 that has not been used in the grid
                    new_value = next(x for x in range(26, 66) if x not in set(sum(new_state, [])))
                    new_state[row_ind][col_ind] = new_value
                    new_state = [tuple(row) for row in new_state]
                    # The cost so far is the number of unique integers used to replace 'x's, as the task is to minimize the number of unique integers used
                    new_cost = g + 1


                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(state, goal_col_sums), new_cost, actions + [(row_ind, col_ind, new_value)], new_state))
   return None


def heuristic(state, goal_col_sums):
    # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
    # This heuristic relaxes the constraint that the unique integers must be unique in the grid
    # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected by at least one unique integer
    # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved integer's sum matches the goal sum for one row, column, or diagonal but not in the other), which is equal to the cost of reaching the successor node
    h = 0
    for i, row in enumerate(state):
        h += abs(sum(row) - goal_col_sums[i])
    return h


print(a_star())
