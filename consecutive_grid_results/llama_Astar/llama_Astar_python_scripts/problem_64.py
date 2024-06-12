
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 73, 74, None], [46, None, 63, 72], [None, 47, None, None], [41, 45, None, 54]]
  
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
       # The goal state is when all 'x's are replaced with unique integers from the given range, and the consecutive order in each row and column is maintained
       if all(row[0] < row[1] < row[2] < row[3] for row in state) and all(state[0][i] < state[1][i] < state[2][i] < state[3][i] for i in range(num_cols)) and all(state[i][i] < state[i + 1][i + 1] for i in range(num_rows - 1)) and all(state[i][num_cols - i - 1] < state[i + 1][num_cols - i - 2] for i in range(num_rows - 1)):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [row[:] for row in state]
                   # The new state must maintain the consecutive order in each row and column
                   for i in range(num_rows):
                       if new_state[i][col_ind] is not None:
                           new_state[row_ind][col_ind] = new_state[i][col_ind] + 1
                   for i in range(num_cols):
                       if new_state[row_ind][i] is not None:
                           new_state[row_ind][col_ind] = new_state[row_ind][i] + 1
                   if row_ind == col_ind:
                       new_state[row_ind][col_ind] = new_state[row_ind - 1][col_ind - 1] + 1
                   elif row_ind == num_rows - col_ind - 1:
                       new_state[row_ind][col_ind] = new_state[row_ind + 1][col_ind + 1] + 1
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, new_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def heuristic(state, new_state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the sum of the numbers in each row and column must be minimized, and the sum of the numbers in the diagonal must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must decrease the heuristic cost of the successor node
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved number is the largest in its row or column), which is equal to the cost of reaching the successor node
   h = sum(new_state[0]) + sum(row[-1] for row in new_state) + sum(new_state[i][i] for i in range(len(new_state)))
   return h


print(a_star())
