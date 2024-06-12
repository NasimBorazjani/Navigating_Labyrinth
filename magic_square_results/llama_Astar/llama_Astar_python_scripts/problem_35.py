
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [80, 48, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sum = 153
   row_sum = 186
   diagonal_sum = 188


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements made to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the specified rows, columns, and diagonal are equal to the given amounts
       if sum(state[i][j] for i in range(num_rows) for j in range(num_cols)) == column_sum + row_sum + diagonal_sum and sum(state[i][i] for i in range(num_rows)) == column_sum and sum(state[i][num_cols - i - 1] for i in range(num_rows)) == row_sum and state[0][2] + state[1][1] + state[2][0] == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that makes the sum of the specified rows, columns, and diagonal equal to the given amounts
                   integer_to_replace = 40 + sum(state[i][j] for i in range(num_rows) for j in range(num_cols)) - (column_sum + row_sum + diagonal_sum)
                   new_state[row][col] = integer_to_replace
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, column_sum, row_sum, diagonal_sum), new_cost, actions + [(row, col, integer_to_replace)], new_state))
   return None


def heuristic(state, column_sum, row_sum, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the given amounts
   # This heuristic relaxes the constraint that the unique integers must be unique, as it does not take into account the uniqueness of the integers
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect integer must be replaced at least once
   # It's consistent because moving an integer from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved integer's correct position is the same as the old one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in range(len(state)):
       for col in range(len(state[row])):
           if state[row][col] is None:
               # The unique integer to replace 'x' is the one that makes the sum of the specified rows, columns, and diagonal equal to the given amounts
               integer_to_replace = 40 + sum(state[i][j] for i in range(len(state)) for j in range(len(state[i]))) - (column_sum + row_sum + diagonal_sum)
               # Add the absolute difference between the current sum and the given amount to the estimate
               h += abs(sum(state[i][j] for i in range(len(state)) for j in range(len(state[i]))) - column_sum)
               h += abs(sum(state[i][i] for i in range(len(state))) - row_sum)
               h += abs(state[0][2] + state[1][1] + state[2][0] - diagonal_sum)
   return h


print(a_star())
