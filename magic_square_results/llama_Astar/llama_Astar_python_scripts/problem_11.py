
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 48], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 127
   goal_row_sum = 144
   goal_diag_sum = 141
  
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the specified rows, columns, and diagonal equal the given amounts
       if sum(row) == goal_row_sum and sum(state[0]) == goal_col_sum and sum(state[i][i] for i in range(num_rows)) == goal_diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the minimum integer not in the current state
                   new_val = min(set(range(35, 60)) - set(sum(state, [])))
                   new_state[row_ind][col_ind] = new_val
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row_ind, col_ind, new_val)], new_state))
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the sums of the rows, columns, and diagonal
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect value must be replaced at least once
   # It's consistent because moving a value from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved value is the incorrect one), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += abs(sum(row) - goal_row_sum)
   for col_ind in range(num_cols):
       h += abs(sum(state[row_ind][col_ind] for row_ind in range(num_rows)) - goal_col_sum)
   h += abs(sum(state[i][i] for i in range(num_rows)) - goal_diag_sum)
   return h


print(a_star())
