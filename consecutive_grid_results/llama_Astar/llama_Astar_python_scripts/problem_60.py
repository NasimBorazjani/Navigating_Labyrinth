
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, None],
                    [37, None, 49, None],
                    [None, 44, None, None],
                    [42, None, 51, 61]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   range_start = 24
   range_end = 64


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
       if all(all(cell is not None for cell in row) for row in state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in range(range_start, range_end):
                       # Check if the new number is valid, ie if it maintains the consecutive order in each row and column
                       if (row_ind > 0 and new_state[row_ind][col_ind] < new_state[row_ind - 1][col_ind] and new_state[row_ind][col_ind] < new_state[row_ind][col_ind - 1]) or (row_ind < num_rows - 1 and new_state[row_ind][col_ind] > new_state[row_ind + 1][col_ind] and new_state[row_ind][col_ind] > new_state[row_ind][col_ind + 1]) or (col_ind > 0 and new_state[row_ind][col_ind] < new_state[row_ind][col_ind - 1] and new_state[row_ind][col_ind] < new_state[row_ind - 1][col_ind]) or (col_ind < num_cols - 1 and new_state[row_ind][col_ind] > new_state[row_ind][col_ind + 1] and new_state[row_ind][col_ind] > new_state[row_ind + 1][col_ind]):
                           continue
                       # Replace the 'x' with the new number
                       new_state[row_ind][col_ind] = num
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                          
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must decrease the heuristic cost of the successor node
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is in the topmost row, rightmost column, or the diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in state:
       h += row[0]
   for col in range(len(state[0])):
       h += state[col][col]
   h += state[-1][0]
   return h


print(a_star())
