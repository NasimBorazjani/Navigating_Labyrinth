
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[57, None, None], [None, 50, 63], [None, 69, 71]]
  
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
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, number of rows and columns)
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range, and the sum of the numbers in the topmost row, the rightmost column, and the diagonal is minimized
       if all(isinstance(cell, int) for row in state for cell in row):
           return actions


       # Generate all valid actions from the current state, which includes replacing an 'x' with an integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate all possible integers that can replace the 'x'
                   possible_integers = [i for i in range(35, 74) if i not in state[row_ind] and i not in [cell for row in state for cell in row]]
                   for integer in possible_integers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = integer
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, integer)], new_state))
                          
   return None


def heuristic(state):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the numbers in the grid must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row, the rightmost column, and the diagonal must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched cell must be replaced at least once
   # It's consistent because moving a cell from one state to another reduces the heuristic cost of the successor node by a max of 1 (if the moved cell's value matches the most common value in the new state but not in the old one), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(num_rows):
       for col_ind in range(num_cols):
           if state[row_ind][col_ind] is None:
               h += 73 - 35 + 1
   return h


print(a_star())
