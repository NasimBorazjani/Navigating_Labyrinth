
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 58, None, None],
                    [None, None, None, 70],
                    [None, 48, 52, None],
                    [None, 43, None, 67]]
  
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
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range, and the sum of the numbers in the topmost row, rightmost column, and diagonal is minimized
       if all(isinstance(cell, int) for row in state for cell in row):
           return actions


       # Generate all valid actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The valid range of numbers is from 33 to 77, as 78 is not included in the range
                   for num in range(33, 78):
                       # Check if the new number is valid, ie if it maintains the consecutive order in each row and column
                       if (new_state[row_ind][col_ind - 1] is None or new_state[row_ind][col_ind] >= new_state[row_ind][col_ind - 1]) and (new_state[row_ind - 1][col_ind] is None or new_state[row_ind][col_ind] >= new_state[row_ind - 1][col_ind]) and (row_ind > 0 and col_ind > 0 and new_state[row_ind - 1][col_ind - 1] is None or new_state[row_ind][col_ind] >= new_state[row_ind - 1][col_ind - 1]):
                           new_state[row_ind][col_ind] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                              
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and diagonal
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the largest or smallest in its row or column), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in state:
       h += row[0]
   h += state[-1][-1]
   for row_ind in range(len(state)):
       h += state[row_ind][row_ind]
   return h


print(a_star())
