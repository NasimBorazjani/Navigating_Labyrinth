
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[68, None, None, 76], [74, None, None, None], [None, None, 82, None], [66, None, 35, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   row_sums = [None, 229, 249, None]
   col_sums = [None, 189, 204, None]
   diagonal_sum = 219


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the rows, columns, and diagonal are as given, and the sum of all the numbers in the grid is as low as possible
       if all(sum(row) == row_sums[i] for i, row in enumerate(state)) and all(sum(col) == col_sums[i] for i, col in enumerate(zip(*state))) and sum(state[i][i] for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that is not in the current state
                   for num in range(33, 85):
                       if num not in new_state[row_ind] and num not in zip(*new_state)[col_ind]:
                           new_state[row_ind][col_ind] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                              
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the sums of rows, columns, and diagonal
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect integer must be replaced at least once
   # It's consistent because moving an integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer is in the row or column that is not at the goal sum), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind, row in enumerate(state):
       h += abs(sum(row) - row_sums[row_ind])
   for col_ind, col in enumerate(zip(*state)):
       h += abs(sum(col) - col_sums[col_ind])
   h += abs(sum(state[i][i] for i in range(len(state))) - diagonal_sum)
   return h


print(a_star())
