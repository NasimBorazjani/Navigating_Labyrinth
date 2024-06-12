
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 62], [None, None, None], [None, None, 56]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [212, 193, 217]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the numbers in the specified rows, columns, and diagonal equals the given amounts
       if all(sum(row) == goal_col_sum[i] for i, row in enumerate(state)):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the minimum integer not in the current state
                   new_value = min(range(50, 85), key=lambda x: (x not in new_state[row_ind] and x not in state[row_ind + 1] and x not in state[row_ind - 1]))
                   new_state[row_ind][col_ind] = new_value
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, goal_col_sum), new_cost, actions + [(row_ind, col_ind, new_value)], new_state))
   return None


def heuristic(state, goal_col_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the specified rows, columns, and diagonal and the goal amounts
   # This heuristic relaxes the constraint that the unique integers must be in the given range and that the sum of all of the numbers in the grid is as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected at least once
   # It's consistent because moving a unique integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved integer's value matches the goal amount for the current row, column, or diagonal but not in the old one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       h += abs(sum(state[i]) - goal_col_sum[i])
   return h


print(a_star())
