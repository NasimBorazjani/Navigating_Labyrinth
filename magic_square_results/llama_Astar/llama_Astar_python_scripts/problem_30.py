
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 59], [None, None, None], [38, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 172
   goal_row_sum = 212
   goal_diag_sum = 165
   min_val = 34
   max_val = 78


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the specified rows, columns, and diagonal equal the given amounts
       if sum(row) == goal_row_sum and sum(state[i][i] for i in range(num_rows)) == goal_diag_sum and sum(state[i][num_rows - i - 1] for i in range(num_rows)) == goal_col_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for new_val in range(min_val, max_val + 1):
                       # Check if the new value is valid, ie it does not violate the constraints of the sums of the rows, columns, and diagonal
                       if (sum(new_state[row_ind]) + new_val == goal_row_sum and
                           sum(new_state[i][i] for i in range(num_rows)) + new_val == goal_diag_sum and
                           sum(new_state[i][num_rows - i - 1] for i in range(num_rows)) + new_val == goal_col_sum):
                           # If the new state is valid, replace the 'x' with the new value
                           new_state[row_ind][col_ind] = new_val
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_row_sum, goal_diag_sum, goal_col_sum), new_cost, actions + [(row_ind, col_ind, new_val)], new_state))
   return None


def heuristic(state, goal_row_sum, goal_diag_sum, goal_col_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the values of the integers can only be in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted at least once
   # It's consistent because moving a value from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved value's sum matches the goal sum for the row, column, or diagonal but not in the old position), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       h += abs(sum(state[row_ind]) - goal_row_sum)
       h += abs(sum(state[i][i] for i in range(len(state))) - goal_diag_sum)
       h += abs(sum(state[i][len(state) - i - 1] for i in range(len(state))) - goal_col_sum)
   return h


print(a_star())
