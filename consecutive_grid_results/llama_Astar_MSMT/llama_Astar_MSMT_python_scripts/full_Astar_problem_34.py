
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' replaced by '_' for better readability
   initial_state = [['38', '_', '77'], ['_', '_', '_'], ['_', '52', '_']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, number of rows and columns)
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == [['38', '49', '77'], ['44', '48', '52'], ['57', '60', '86']]:
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's in the grid with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == '_':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique integer from the given range that maintains the consecutive order in each row and column
                   for number in range(39, 87):
                       new_state[row_ind][col_ind] = str(number)
                       if check_state(new_state, row_ind, col_ind):
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                           new_cost = g + 1
                          
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, number)], new_state))
                              
   return None


def check_state(state, row_ind, col_ind):
   # Check if the new state maintains the consecutive order in each row and column
   for row in state:
       for i in range(len(row) - 1):
           if int(row[i]) >= int(row[i + 1]):
               return False
   for col_ind in range(len(state[0])):
       for row_ind in range(len(state) - 1):
           if int(state[row_ind][col_ind]) >= int(state[row_ind + 1][col_ind]):
               return False
   # Check if the new state maintains the consecutive order in the diagonal
   for i in range(len(state) - 1):
       if int(state[i][i]) >= int(state[i + 1][i + 1]):
           return False
   # If the state is valid, return True
   return True


def heuristic(state):
   # An admissible and consistent heuristic is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each invalid state must be corrected by at least one replacement
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is in the topmost row, the rightmost column, or the diagonal), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       h += int(state[i][i])
   h += sum(int(state[0][i]) for i in range(len(state[0])))
   h += sum(int(state[i][-1]) for i in range(len(state)))
   return h


print(a_star())
