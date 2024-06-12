
import heapq


def initialize():
   # Define the initial state of the grid
   initial_state = [['x', '89', '95'], ['x', 'x', '96'], ['74', '93', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid and dimensions of the grid)
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the grid satisfies all the conditions given in the problem statement
       if is_goal_state(state):
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique integer from the given range
                   for num in range(45, 99):
                       new_state[row][col] = num
                       # Add the new state to the queue of not-yet-visited states
                       new_cost = g + 1
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, num)], new_state))
                   # Reset the 'x' in the current state
                   new_state[row][col] = 'x'


def is_goal_state(state):
   # Check if the state satisfies all the conditions given in the problem statement
   # The state satisfies the conditions if each row and column is strictly increasing or decreasing
   # And the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner is minimized
   # The conditions are checked row by row and column by column
   for row in state:
       if not is_increasing_or_decreasing(row):
           return False
   for col in range(num_cols):
       if not is_increasing_or_decreasing([state[row][col] for row in range(num_rows)]):
           return False
   # Check the diagonal
   if not is_increasing_or_decreasing([state[i][i] for i in range(num_rows)]):
       return False
   # Check the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal
   if sum(state[0]) + sum([state[i][num_cols - 1] for i in range(num_rows)]) + sum([state[i][i] for i in range(num_rows)]) != 190:
       return False
   return True


def is_increasing_or_decreasing(row):
   # Check if the row is strictly increasing or decreasing
   if all(row[i] < row[i + 1] for i in range(len(row) - 1)):
       return True
   if all(row[i] > row[i + 1] for i in range(len(row) - 1)):
       return True
   return False


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each absolute difference must be at least 0
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the same as the one it replaces), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in state:
       h += abs(row[0] - row[1])
   for col in range(num_cols):
       h += abs(state[0][col] - state[1][col])
   h += abs(state[0][0] - state[1][1])
   return h


print(a_star())
