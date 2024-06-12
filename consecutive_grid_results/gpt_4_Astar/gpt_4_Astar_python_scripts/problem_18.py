
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('16', '17', 'x'), ('x', 'x', 'x'), ('x', '44', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(16, 55))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # Get the coordinate of the next 'x' in the grid
       x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       # Get the set of numbers that are already in the grid
       numbers_in_grid = set([int(state[i][j]) for i in range(num_rows) for j in range(num_cols) if state[i][j] != 'x'])
       # Get the set of numbers that can replace the 'x'
       numbers_to_replace_x = available_numbers - numbers_in_grid
       for number in numbers_to_replace_x:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = str(number)
           new_state = tuple(tuple(row) for row in new_state)
           # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
           if all(all(int(new_state[i][j]) < int(new_state[i][j + 1]) for j in range(num_cols - 1)) or all(int(new_state[i][j]) > int(new_state[i][j + 1]) for j in range(num_cols - 1)) for i in range(num_rows)) and all(all(int(new_state[i][j]) < int(new_state[i + 1][j]) for i in range(num_rows - 1)) or all(int(new_state[i][j]) > int(new_state[i + 1][j]) for i in range(num_rows - 1)) for j in range(num_cols)):
               # The cost so far is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
               new_cost = sum(int(new_state[0][j]) for j in range(num_cols) if new_state[0][j] != 'x') + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows) if new_state[i][num_cols - 1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available numbers that can replace the remaining 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced with at least one of the available numbers
   # It's consistent because replacing an 'x' with a number increases the heuristic cost of the successor node by at least the minimum available number, which is equal to the cost of reaching the successor node
   h = 0
   # Get the set of numbers that are already in the grid
   numbers_in_grid = set([int(state[i][j]) for i in range(num_rows) for j in range(num_cols) if state[i][j] != 'x'])
   # Get the set of numbers that can replace the 'x's
   numbers_to_replace_x = available_numbers - numbers_in_grid
   # Get the count of 'x's in the grid
   count_x = len([1 for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'])
   # Add the minimum available number to the estimate for each 'x' in the grid
   for _ in range(count_x):
       min_number = min(numbers_to_replace_x)
       h += min_number
       numbers_to_replace_x.remove(min_number)
   return h


print(a_star())
