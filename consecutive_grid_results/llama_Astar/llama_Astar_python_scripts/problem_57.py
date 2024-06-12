
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[11, 14, None, None], [12, None, None, 38], [None, None, None, 36], [25, None, None, 34]]
  
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


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique integer from the given range
                   for num in range(7, 47):
                       new_state[row][col] = num
                       # Check if the new state is valid, ie if the numbers in each row and column are strictly increasing or decreasing
                       if is_valid(new_state):
                           new_cost = g + 1
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, num)], new_state))
                   # Reset the 'x' in the current state
                   new_state[row][col] = None


   return None


def is_valid(state):
   # Check if the numbers in each row and column are strictly increasing or decreasing
   for row in state:
       if row[0] < row[1] < row[2] < row[3]:
           continue
       elif row[0] > row[1] > row[2] > row[3]:
           continue
       else:
           return False
   for col in range(len(state)):
       if state[0][col] < state[1][col] < state[2][col] < state[3][col]:
           continue
       elif state[0][col] > state[1][col] > state[2][col] > state[3][col]:
           continue
       else:
           return False
   # Check if the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner are minimized
   if state[0][0] + state[0][1] + state[0][2] + state[0][3] + state[3][0] + state[3][1] + state[3][2] + state[3][3] + state[0][0] + state[1][1] + state[2][2] + state[3][3] != 120:
       return False
   return True


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the one that causes the sum to decrease), which is equal to the cost of reaching the successor node
   return state[0][0] + state[0][1] + state[0][2] + state[0][3] + state[3][0] + state[3][1] + state[3][2] + state[3][3] + state[0][0] + state[1][1] + state[2][2] + state[3][3]


print(a_star())
