
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [None, None, 55]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sum = 138
   row_sum = 171
   diagonal_sum = 145


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements made to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the specified rows, columns, and diagonal are equal to the given amounts
       if sum(row) == row_sum and sum(state[0]) == column_sum and sum(state[i][i] for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the next integer in the range that is not already in the grid
                   new_value = next(x for x in range(31, 76) if x not in new_state[0] and x not in new_state[1] and x not in new_state[2])
                   new_state[row_ind][col_ind] = new_value
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, new_value)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the given amounts
   # This heuristic relaxes the constraint that the unique integers must be in the given range and that the sums of the specified rows, columns, and diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected by at least one
   # It's consistent because moving a unique integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer is in the sum, else it's 1), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += abs(sum(row) - 171)
   for col_ind in range(num_cols):
       h += abs(sum(state[row_ind][col_ind] for row_ind in range(num_rows)) - 138)
   h += abs(sum(state[i][i] for i in range(num_rows)) - 145)
   return h


print(a_star())
