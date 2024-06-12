
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, 36, 44], [None, 34, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


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


       # Check if the current state is the goal state
       # The goal state is when the grid is filled with unique integers from the given range, and the sum of the numbers in the topmost row, the rightmost column, and the diagonal is minimized
       if all(isinstance(cell, int) for row in state for cell in row):
           return actions


       # Generate all valid actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               # Check if the current cell is an 'x'
               if state[row_ind][col_ind] is None:
                   # Generate all possible integers that can be placed in the current cell
                   possible_integers = [i for i in range(19, 53) if i not in state[row_ind] and i not in [cell for row in state for cell in row]]
                   for integer in possible_integers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = integer
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, integer)], new_state))
                          
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the rightmost column, and the diagonal
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one cell to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the largest or smallest in its row or column), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   # Add the numbers in the topmost row
   h += sum(state[0])
   # Add the numbers in the rightmost column
   h += sum(state[i][-1] for i in range(len(state)))
   # Add the numbers in the diagonal
   h += sum(state[i][i] for i in range(len(state)))
   return h


print(a_star())
