
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 77, None], [49, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 180
   goal_row_sum = 156
   goal_diag_sum = 127
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
       # The goal state is when the sum of the numbers in the specified rows, columns, and diagonal equals the given amounts
       if sum(row) == goal_row_sum and sum(state[i][i] for i in range(num_rows)) == goal_diag_sum and sum(state[i][num_rows - i - 1] for i in range(num_rows)) == goal_col_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for new_val in range(min_val, max_val + 1):
                       # Check if the new state would be valid, ie the new_val is not already in the state
                       if new_val not in sum(new_state, []):
                           new_state[row_ind][col_ind] = new_val
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the grid with unique integers
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_row_sum, goal_diag_sum, goal_col_sum), new_cost, actions + [(row_ind, col_ind, new_val)], new_state))
                   # Reset the cell to 'x' for the next possible value
                   new_state[row_ind][col_ind] = None
   return None


def heuristic(state, goal_row_sum, goal_diag_sum, goal_col_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the specified rows, columns, and diagonal and the goal amounts
   # This heuristic relaxes the constraint that the sum of all of the numbers in the grid is as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted at least once
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node by a max of the difference between the old and new sums, which is equal to the cost of reaching the successor node
   h = 0
   # Check the sum of the specified rows
   for row in state:
       h += abs(sum(row) - goal_row_sum)
   # Check the sum of the numbers in the diagonal from the top right to the bottom left corner of the grid
   for i in range(len(state)):
       h += abs(state[i][i] - goal_diag_sum)
   # Check the sum of the numbers in the diagonal from the top left to the bottom right corner of the grid
   for i in range(len(state)):
       h += abs(state[i][len(state) - i - 1] - goal_col_sum)
   return h


print(a_star())
