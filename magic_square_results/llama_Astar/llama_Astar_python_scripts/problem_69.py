
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by 'None' for easier manipulation
   initial_state = [[43, 65, None, None], [42, None, 59, None], [54, 45, None, None], [None, None, None, 35]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   row_sums = [None, 219, 220, None]
   col_sums = [None, 205, 218, None]
   diagonal_sum = 182


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the rows, columns, and diagonal are as given in the problem statement
       if all(sum(row) == row_sums[i] for i, row in enumerate(state)) and all(sum(col) == col_sums[j] for j, col in enumerate(zip(*state))) and sum(state[i][i] for i in range(num_rows)) - state[1][1] == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The new state must maintain the constraint on the row and column sums
                   for i in range(num_rows):
                       if row_sums[i] is not None:
                           new_state[i][col_ind] = row_sums[i] - sum(new_state[i]) + new_state[row_ind][col_ind]
                   for j in range(num_cols):
                       if col_sums[j] is not None:
                           new_state[row_ind][j] = col_sums[j] - sum(new_state[i][j] for i in range(num_rows)) + new_state[row_ind][col_ind]
                   # The new state must maintain the constraint on the diagonal sum
                   new_state[row_ind][col_ind] = diagonal_sum - sum(new_state[i][i] for i in range(num_rows)) + new_state[row_ind][col_ind]
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the grid with the unique integers
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the difference between the current and goal sums
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted by a positive amount
   # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved integer's current position is part of the sum that is violated, and the new position is not), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       # Check if the row sum is not None
       if row_sums[i] is not None:
           h += abs(sum(state[i]) - row_sums[i])
   for j in range(len(state[0])):
       # Check if the column sum is not None
       if col_sums[j] is not None:
           h += abs(sum(state[i][j] for i in range(len(state))) - col_sums[j])
   h += abs(sum(state[i][i] for i in range(len(state))) - diagonal_sum)
   return h


print(a_star())
