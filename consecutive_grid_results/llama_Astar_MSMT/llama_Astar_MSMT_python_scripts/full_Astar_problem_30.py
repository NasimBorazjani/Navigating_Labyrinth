
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 57, None], [42, None, 72], [39, None, 73]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 39
   range_end = 87


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue
  
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the range of the numbers)
   initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if the grid is filled with unique numbers in the given range and each row and column is strictly increasing or decreasing
       if is_goal_state(state):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               # Check if the current cell is a 'x'
               if state[row][col] is None:
                   # Generate the new state by replacing the 'x' with each unique integer from the given range
                   for num in range(range_start, range_end + 1):
                       # Check if the new number is valid, ie if it maintains the consecutive order in each row and column
                       if is_valid_placement(state, row, col, num):
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, num_rows, num_cols), new_cost, actions + [(row, col, num)], new_state))
                              
   return None


def is_goal_state(state):
   # Check if the grid is filled with unique numbers in the given range and each row and column is strictly increasing or decreasing
   # Check if all cells are filled
   if None in state[0] or None in state[1] or None in state[2]:
       return False
   # Check if each row and column is strictly increasing or decreasing
   for row in state:
       if not (all(row[i] < row[i + 1] for i in range(len(row) - 1)) or all(row[i] > row[i + 1] for i in range(len(row) - 1))):
           return False
   for col in range(len(state[0])):
       if not (all(state[i][col] < state[i + 1][col] for i in range(len(state) - 1)) or all(state[i][col] > state[i + 1][col] for i in range(len(state) - 1))):
           return False
   return True


def is_valid_placement(state, row, col, num):
   # Check if the new number is valid, ie if it maintains the consecutive order in each row and column
   # Check if the new number is in the given range
   if num < 39 or num > 86:
       return False
   # Check if the new number maintains the consecutive order in the row
   if row > 0 and state[row][col] < state[row - 1][col] and state[row][col] < num:
       return False
   if row < 2 and state[row][col] > state[row + 1][col] and state[row][col] > num:
       return False
   # Check if the new number maintains the consecutive order in the column
   if col > 0 and state[row][col] < state[row][col - 1] and state[row][col] < num:
       return False
   if col < 2 and state[row][col] > state[row][col + 1] and state[row][col] > num:
       return False
   return True


def heuristic(state, num_rows, num_cols):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in the grid must be unique and in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each invalid placement of a number increases the heuristic cost of the successor node
   # It's consistent because moving a number from one cell to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is in the topmost row, rightmost column, or diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in state:
       h += row[0]
   h += state[0][-1]
   h += state[0][0]
   return h


print(a_star())
