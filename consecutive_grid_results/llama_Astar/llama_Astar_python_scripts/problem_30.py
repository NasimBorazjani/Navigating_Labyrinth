
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 57, None], [42, None, 72], [39, None, 73]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 39
   range_end = 87


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
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range, and the sum of the numbers in the topmost row, the rightmost column, and the diagonal is minimized
       if all(all(cell is not None for cell in row) for row in state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The new state must maintain the consecutive order in each row and column
                   for num in range(range_start, range_end + 1):
                       if num not in new_state[row_ind] and num not in new_state[col_ind] and (row_ind == col_ind or num not in [row[col_ind] for row in new_state]):
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           new_state = tuple(new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the cell to 'x' for the next possible number
                   new_state[row_ind][col_ind] = None
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the rightmost column, and the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one cell to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is in the topmost row, rightmost column, or diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in state:
       h += row[0]
   h += state[0][-1]
   h += state[0][0]
   return h


print(a_star())
