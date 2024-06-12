
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [None, None, 19]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sums = [71, 82, 70]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of all the numbers in the grid is as low as possible, and the sums of the specified rows, columns, and diagonal equal the given amounts
       if all(sum(row) == column_sums[i] for i, row in enumerate(state)) and sum(sum(row) for row in state) == 222:
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that is not in the grid
                   unique_integer = next(i for i in range(12, 47) if i not in sum(state, []))
                   new_state[row_ind][col_ind] = unique_integer
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of unique integers used, as our objective is to minimize the number of unique integers used
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, column_sums), new_cost, actions + [(row_ind, col_ind, unique_integer)], new_state))
                      
   return None


def heuristic(state, column_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the given amounts
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the difference between the current sums and the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each overestimation must be balanced by an underestimation
   # It's consistent because moving a unique integer from one position to another results in a change in the heuristic cost of the successor node by a max of 2 (if the moved unique integer's current position and new position are both in the same row, column, or diagonal), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       h += abs(sum(state[row_ind]) - column_sums[row_ind])
   h += abs(sum(state[i][i] for i in range(len(state))) - column_sums[-1])
   return h


print(a_star())
