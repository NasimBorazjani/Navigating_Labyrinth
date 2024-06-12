
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, None],
                    [24, None, 27, 41],
                    [22, 37, None, None],
                    [29, None, None, 46]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   row_sums = [None, 139, 178, None]
   col_sums = [None, 187, 186, None]
   diagonal_sum = 160


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
       # The goal state is when the sums of the specified rows, columns, and diagonal are equal to the given amounts
       if all(sum(row) == row_sums[i] for i, row in enumerate(state)) and all(sum(col) == col_sums[i] for i, col in enumerate(zip(*state))) and sum(state[i][i] for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the smallest integer that has not been used in the grid
                   new_val = min(i for i in range(22, 69) if i not in set(sum(row, []) for row in new_state))
                   new_state[row_ind][col_ind] = new_val
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(row_ind, col_ind, new_val)], new_state))
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the difference between the current and goal sums
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect integer must be replaced at least once
   # It's consistent because moving an integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer's current position and the new position are both incorrect), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind, row in enumerate(state):
       h += abs(sum(row) - row_sums[row_ind])
   for col_ind, col in enumerate(zip(*state)):
       h += abs(sum(col) - col_sums[col_ind])
   h += abs(sum(state[i][i] for i in range(len(state))) - diagonal_sum)
   return h


print(a_star())
