
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[64, 78, None], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sums = [234, None, None]
   row_sums = [201, None, None]
   diagonal_sum = 213


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
       if all(sum(row) == row_sums[i] for i, row in enumerate(state)) and all(sum(col) == column_sums[i] for i, col in enumerate(zip(*state))) and sum(state[i][i] for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that makes the sum of the specified rows, columns, and diagonal equal to the given amounts
                   # The integer is the difference between the given sum and the current sum
                   new_value = row_sums[row_ind] - sum(new_state[row_ind]) + column_sums[col_ind] - sum(new_state[i][col_ind] for i in range(num_rows)) + diagonal_sum - sum(new_state[i][i] for i in range(num_rows))
                   new_state[row_ind][col_ind] = new_value
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, row_sums, column_sums, diagonal_sum), new_cost, actions + [(row_ind, col_ind, new_value)], new_state))
   return None


def heuristic(state, row_sums, column_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums and the given sums
   # This heuristic relaxes the constraint that the unique integer to replace 'x' must be the one that makes the sum of the specified rows, columns, and diagonal equal to the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected at least once
   # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved unique integer's current position and the new position are both in the same row, column, or diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is None:
               # The unique integer to replace 'x' is the one that makes the sum of the specified rows, columns, and diagonal equal to the given amounts
               # The integer is the difference between the given sum and the current sum
               new_value = row_sums[row_ind] - sum(state[row_ind]) + column_sums[col_ind] - sum(state[i][col_ind] for i in range(len(state))) + diagonal_sum - sum(state[i][i] for i in range(len(state)))
               h += abs(new_value)
   return h


print(a_star())
