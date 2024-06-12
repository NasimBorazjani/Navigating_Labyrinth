
import heapq


def initialize():
   # Define the initial state of the grid, with 'x's replaced by None for easier manipulation
   initial_state = [[57, None, 86], [None, 75, None], [None, 76, 90]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   hidden_value = None
   valid_range = range(48, 101)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, hidden_value, valid_range, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, number of rows and columns, hidden value, valid range of numbers)
   initial_state, num_rows, num_cols, hidden_value, valid_range, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie all cells are filled and the grid satisfies the conditions of increasing or decreasing rows and columns
       if all(cell is not None for row in state for cell in row) and is_valid(state):
           return actions


       # Generate all valid actions from the current state, which includes replacing a hidden value with a unique valid number
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   for value in valid_range:
                       # Check if the new state would be valid, ie the replacement must satisfy the conditions of increasing or decreasing rows and columns
                       if is_valid_replacement(state, row_ind, col_ind, value):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = value
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, new_state), new_cost, actions + [(row_ind, col_ind, value)], new_state))
                              
   return None


def is_valid(state):
   # Check if the grid satisfies the conditions of increasing or decreasing rows and columns
   for row in state:
       if row[0] > row[1] > row[2]:
           if row[0] - row[1] != row[1] - row[2]:
               return False
   for col_ind in range(num_cols):
       col = [state[row_ind][col_ind] for row_ind in range(num_rows)]
       if col[0] > col[1] > col[2]:
           if col[0] - col[1] != col[1] - col[2]:
               return False
   diagonal = [state[i][i] for i in range(num_rows)]
   if diagonal[0] > diagonal[1] > diagonal[2]:
       if diagonal[0] - diagonal[1] != diagonal[1] - diagonal[2]:
           return False
   return True


def is_valid_replacement(state, row_ind, col_ind, value):
   # Check if the new state would be valid, ie the replacement must satisfy the conditions of increasing or decreasing rows and columns
   new_state = [list(row[:]) for row in state]
   new_state[row_ind][col_ind] = value
   return is_valid(new_state)


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the sum of the numbers in each row, column, and diagonal must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is part of the sum), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   h += sum(state[0])
   h += state[1][-1] + state[2][-1]
   h += state[2][0]
   return h


print(a_star())
