
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 21, 'x', 'x'), (18, 27, 'x', 51), (24, 29, 'x', 'x'), (54, 33, 25, 12))
   # Define the range of unique integers that can be used to replace the 'x's
   unique_integers = set(range(10, 66))
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
       # The goal state is where all the 'x's have been replaced with unique integers, maintaining the consecutive order in each row and column
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the set of numbers already present in the grid
                   numbers_in_grid = set(cell for row in state for cell in row if cell != 'x')
                   # Get the set of numbers that can be used to replace the 'x'
                   available_numbers = unique_integers - numbers_in_grid
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie if the consecutive order in each row and column is maintained
                       if all(new_state[row][col] < new_state[row][col + 1] for row in range(num_rows) for col in range(num_cols - 1) if new_state[row][col] != 'x' and new_state[row][col + 1] != 'x') and all(new_state[row][col] < new_state[row + 1][col] for row in range(num_rows - 1) for col in range(num_cols) if new_state[row][col] != 'x' and new_state[row + 1][col] != 'x'):
                           # The cost so far is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                           new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[row][num_cols - 1]) for row in range(num_rows) if new_state[row][num_cols - 1] != 'x') + sum(int(new_state[row][row]) for row in range(num_rows) if new_state[row][row] != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available unique integer for each remaining 'x' in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be in consecutive order and that each number can only appear once in the grid; ie It presumes we can replace each 'x' with the smallest available unique integer regardless of its position in the grid
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the smallest available unique integer, the number used to replace the 'x' in the heuristic
   h = 0
   # Get the set of numbers already present in the grid
   numbers_in_grid = set(cell for row in state for cell in row if cell != 'x')
   # Get the set of numbers that can be used to replace the 'x's
   available_numbers = sorted(list(unique_integers - numbers_in_grid))
   # Count the number of 'x's in the grid
   num_x = sum(cell == 'x' for row in state for cell in row)
   # Add the smallest available unique integer for each 'x' to the estimate
   for i in range(num_x):
       h += available_numbers[i]
   return h


print(a_star())
