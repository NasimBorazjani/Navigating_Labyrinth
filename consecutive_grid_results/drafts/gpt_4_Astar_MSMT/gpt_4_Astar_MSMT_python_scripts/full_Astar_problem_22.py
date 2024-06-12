
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('16', 'x', 'x'), ('28', '34', 'x'), ('x', '46', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 13
   range_end = 56
   # The set of all unique numbers that can be used to replace the 'x's in the grid
   available_numbers = set(range(range_start, range_end))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return num_rows, num_cols, available_numbers, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the set of available numbers)
   num_rows, num_cols, available_numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's in the grid have been replaced with unique integers from the given range, while maintaining the consecutive order in each row and column
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # Generate the coordinates of the 'x's in the grid
       x_coordinates = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x']
       # The next 'x' to be replaced is the one with the smallest row index, and among those, the one with the smallest column index
       next_x_coordinate = min(x_coordinates)
       # The set of numbers already present in the grid
       present_numbers = set(np.array(state).flatten()) - set(['x'])
       # The set of numbers that can be used to replace the next 'x'
       available_numbers = set(range(range_start, range_end)) - present_numbers
       for number in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[next_x_coordinate[0]][next_x_coordinate[1]] = str(number)
           new_state = tuple(tuple(row) for row in new_state)
           # Check if the new state is valid, ie if the consecutive order in each row and column is maintained
           if all(all(int(new_state[i][j]) < int(new_state[i][j + 1]) for j in range(num_cols - 1)) or all(int(new_state[i][j]) > int(new_state[i][j + 1]) for j in range(num_cols - 1)) for i in range(num_rows)) and all(all(int(new_state[i][j]) < int(new_state[i + 1][j]) for i in range(num_rows - 1)) or all(int(new_state[i][j]) > int(new_state[i + 1][j]) for i in range(num_rows - 1)) for j in range(num_cols)):
               # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
               new_cost = sum(int(num) for num in new_state[0] if num != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(next_x_coordinate[0], next_x_coordinate[1], number)], new_state))
                  
   return None


def heuristic(state):
   # An admissible and consistent heuristic is the sum of the smallest available numbers that can be used to replace the remaining 'x's in the grid
   # The heuristic relaxes the constraint that the replacements must maintain the consecutive order in each row and column and presumes we can replace the 'x's with any of the available numbers
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the smallest available number, the decrease in the heuristic cost, if the 'x' is replaced with the smallest available number, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no 'x's to be replaced in the goal state.
   h = 0
   # The set of numbers already present in the grid
   present_numbers = set(np.array(state).flatten()) - set(['x'])
   # The set of numbers that can be used to replace the 'x's
   available_numbers = set(range(range_start, range_end)) - present_numbers
   # The number of 'x's in the grid
   num_xs = list(np.array(state).flatten()).count('x')
   # Add the smallest available numbers to the estimate
   h += sum(sorted(list(available_numbers))[:num_xs])
   return h


print(a_star())
