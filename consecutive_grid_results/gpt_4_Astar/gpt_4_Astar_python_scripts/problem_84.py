
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('91', '57', 'x', '45'), ('41', '49', 'x', 'x'), ('x', 'x', '49', 'x'), ('x', '46', '47', '73'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(range(39, 95))
   # Define the size of the grid
   num_rows = 4
   num_cols = 4


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
       # The goal state is where all 'x's have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers (all numbers in the range - numbers present in the current state) in the range
       # Get the coordinates of the next 'x' in the grid
       x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       # Get the set of numbers that are already in the grid
       numbers_in_grid = set([int(num) for num in np.array(state).flatten() if num != 'x'])
       # Get the set of numbers that can be used to replace the 'x's
       available_numbers = num_range - numbers_in_grid
       for num in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = str(num)
           new_state = tuple(tuple(row) for row in new_state)
           # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
           if all(all(int(new_state[i][j]) < int(new_state[i][j + 1]) for j in range(num_cols - 1)) or all(int(new_state[i][j]) > int(new_state[i][j + 1]) for j in range(num_cols - 1)) for i in range(num_rows)) and all(all(int(new_state[i][j]) < int(new_state[i + 1][j]) for i in range(num_rows - 1)) or all(int(new_state[i][j]) > int(new_state[i + 1][j]) for i in range(num_rows - 1)) for j in range(num_cols)):
               # The cost so far is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
               new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available numbers that can be used to replace the remaining 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum available numbers are always less than or equal to the actual numbers that will replace the 'x's
   # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number
   h = 0
   # Get the set of numbers that are already in the grid
   numbers_in_grid = set([int(num) for num in np.array(state).flatten() if num != 'x'])
   # Get the set of numbers that can be used to replace the 'x's
   available_numbers = sorted(list(num_range - numbers_in_grid))
   # Get the number of 'x's in the grid
   num_xs = list(np.array(state).flatten()).count('x')
   # Add the minimum available numbers to the estimate
   for i in range(num_xs):
       h += available_numbers[i]
   return h


print(a_star())
