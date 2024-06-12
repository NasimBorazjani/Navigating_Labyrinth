
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [22, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sum = 82
   row_sum = 82
   diagonal_sum = 82
   total_sum = 3 * column_sum


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
       # The goal state is when the sum of all the numbers in the grid is as low as possible, and the sum of the specified rows, columns, and diagonal equals the given amounts
       if sum(sum(row) for row in state) == total_sum and sum(state[i][i] for i in range(num_rows)) == diagonal_sum and sum(state[i][0] for i in range(num_rows)) == column_sum and sum(state[0][i] for i in range(num_cols)) == row_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the next integer in the range that is not already in the grid
                   new_value = next(i for i in range(20, 40) if i not in sum(state, []))
                   new_state[row_ind][col_ind] = new_value
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(row_ind, col_ind, new_value)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the grid and the goal sum, and the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the unique integers must be in the given range and that the sum of all of the numbers in the grid is as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched integer must be replaced at least once
   # It's consistent because moving an integer from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved integer's value matches the goal sum but not in the old position), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in state:
       h += abs(sum(row) - column_sum)
   for i in range(num_rows):
       h += abs(sum(state[i][j] for j in range(num_cols)) - row_sum)
   h += abs(sum(state[i][i] for i in range(num_rows)) - diagonal_sum)
   return h


print(a_star())
