
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[46, 80, 90], [51, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


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


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == [[45, 46, 47], [48, 49, 50], [51, 52, 53]]:
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The value to replace the 'x' is the next unique integer in the range
                   value_to_replace = str(g + 1)
                   new_state[row][col] = value_to_replace
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state 
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, value_to_replace)], new_state))
                  
   return None


def heuristic(state):
   # An admissible and consistent heuristic is the sum of the values in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched value must be replaced at least once
   # It's consistent because moving a value from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved value's position is closer to the goal), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += int(row[0])
   for col in range(len(state)):
       h += int(state[col][-1])
   h += int(state[0][0]) + int(state[-1][-1])
   return h


print(a_star())
