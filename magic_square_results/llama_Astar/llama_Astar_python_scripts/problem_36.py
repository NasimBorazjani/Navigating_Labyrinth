
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [69, 71, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sum = 198
   row_sum = 152
   diagonal_sum = 195
   total_sum = column_sum + row_sum + diagonal_sum


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the specified rows, columns, and diagonal equals the given amounts
       if sum(row for row in state) == total_sum and sum(state[i][i] for i in range(num_rows)) == diagonal_sum and sum(state[i][num_rows - i - 1] for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that makes the sum of the specified rows, columns, and diagonal equal to the given amounts
                   # The integer is the only one that satisfies the equation: total_sum - current_sum + new_integer = 0
                   new_integer = (total_sum - sum(new_state) + column_sum - sum(new_state[row_ind])) // 2
                   new_state[row_ind][col_ind] = new_integer
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, new_integer)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only cares about the sum of the absolute differences between the current state and the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved integer's absolute difference with the goal state is 1), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(num_rows):
       for col_ind in range(num_cols):
           if state[row_ind][col_ind] is not None:
               h += abs(state[row_ind][col_ind] - (total_sum - sum(state) + column_sum - sum(state[row_ind])))
   return h


print(a_star())
