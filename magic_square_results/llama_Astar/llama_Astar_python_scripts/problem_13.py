
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [['41', None, None], ['34', None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sum = 129
   row_sum = 133
   diagonal_sum = 136
   min_value = 28
   max_value = 57


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the specified rows, columns, and diagonal equal the given amounts
       if sum(state[i][j] for i in range(num_rows) for j in range(num_cols)) == column_sum + row_sum + diagonal_sum and all(sum(state[i][j] for j in range(num_cols)) == column_sum for i in range(num_rows)) and sum(state[i][i] for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The new state must maintain the constraint on the unique integers in the grid
                   for value in range(min_value, max_value + 1):
                       if value not in new_state[row_ind] and value not in new_state[col_ind] and value not in new_state[row_ind + col_ind]:
                           new_state[row_ind][col_ind] = value
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(row_ind, col_ind, value)], new_state))
                   # Reset the new state to 'x' for the next possible value
                   new_state[row_ind][col_ind] = None
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers in the grid must be unique, as it only considers the sum of the absolute differences between the current state and the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved integer is the same in the new and old positions), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(num_rows):
       for col_ind in range(num_cols):
           if state[row_ind][col_ind] is not None:
               # Calculate the absolute difference between the current state and the goal state
               h += abs(state[row_ind][col_ind] - goal_state[row_ind][col_ind])
   return h


print(a_star())
