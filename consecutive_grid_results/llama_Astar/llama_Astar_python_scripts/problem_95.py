
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by 'None' for easier handling
   initial_state = [[71, None, 57, None], [67, 68, None, 73], [51, None, 72, None], [50, None, 75, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4


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
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range
       if all(isinstance(cell, int) for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The new state must maintain the consecutive order in each row and column
                   for new_val in range(39, 94):
                       if all(new_val > new_state[row_ind][col_ind - 1] if col_ind > 0 else True,
                              new_val < new_state[row_ind][col_ind + 1] if col_ind < num_cols - 1 else True,
                              new_val > new_state[row_ind - 1][col_ind] if row_ind > 0 else True,
                              new_val < new_state[row_ind + 1][col_ind] if row_ind < num_rows - 1 else True):
                           new_state[row_ind][col_ind] = new_val
                           new_state = [tuple(row) for row in new_state]
                           new_state = tuple(new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, new_val)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must not result in a sum greater than the current sum
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is in the topmost row, rightmost column, or diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in state:
       h += row[0]
   h += state[-1][-1]
   h += state[0][0]
   for i in range(len(state)):
       h += state[i][i]
   return h


print(a_star())
