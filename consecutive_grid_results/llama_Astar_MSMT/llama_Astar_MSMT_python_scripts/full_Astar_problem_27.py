
import heapq


def initialize():
   # Define the initial state of the grid, with the numbers as strings
   initial_state = [['52', 'x', 'x'], ['50', 'x', 'x'], ['x', 'x', '69']]
   # Define the range of the numbers
   num_range = range(46, 89)
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_range, num_rows, num_cols, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, the range of the numbers, and dimensions of the grid)
   initial_state, num_range, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where each row, column, and diagonal is strictly increasing or decreasing
       # And the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner is minimized
       if is_goal_state(state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with any of the unique integers from the range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Check if the new state would be valid, ie the replaced number maintains the consecutive order in each row and column
                   for num in num_range:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = str(num)
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def is_goal_state(state):
   # Check if the state is the goal state
   # The state is the goal state if each row, column, and diagonal is strictly increasing or decreasing
   for row in state:
       if not is_increasing_or_decreasing(row):
           return False
   for col in range(num_cols):
       if not is_increasing_or_decreasing([state[row][col] for row in range(num_rows)]):
           return False
   diagonal = [state[i][i] for i in range(num_rows)]
   if not is_increasing_or_decreasing(diagonal):
       return False
   diagonal = [state[i][num_cols - i - 1] for i in range(num_rows)]
   if not is_increasing_or_decreasing(diagonal):
       return False
   return True


def is_increasing_or_decreasing(lst):
   # Check if the list is strictly increasing or decreasing
   if lst[0] < lst[1]:
       for i in range(1, len(lst)):
           if lst[i] <= lst[i - 1]:
               return False
   else:
       for i in range(1, len(lst)):
           if lst[i] >= lst[i - 1]:
               return False
   return True


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must not result in an increase of the heuristic cost of the successor node
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the one in the topmost row, rightmost column, or diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = sum(int(state[0][i]) for i in range(num_cols)) + sum(int(state[i][num_cols - 1]) for i in range(num_rows)) + sum(state[i][i] for i in range(num_rows))
   return h


print(a_star())
