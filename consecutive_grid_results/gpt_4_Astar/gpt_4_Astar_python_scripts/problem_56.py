
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '63', 'x'), ('x', '53', '57', '73'), ('x', 'x', '56', 'x'), ('42', 'x', 'x', '68'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(range(40, 81))
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
       # The goal state is where all the 'x's have been replaced with unique integers from the given range, and the numbers in each row and column are strictly increasing or decreasing
       if all(all(cell != 'x' for cell in row) for row in state) and all(all(int(row[i]) < int(row[i + 1]) or int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1)) for row in state) and all(all(int(state[i][j]) < int(state[i + 1][j]) or int(state[i][j]) > int(state[i + 1][j]) for i in range(num_rows - 1)) for j in range(num_cols)):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers (all numbers in the range - numbers present in the current state) in the range
       # Generate the coordinates of the 'x's
       x_coordinates = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x']
       # If the state has at least 1 remaining unknown number, ie 'x'
       if x_coordinates:
           # Get the coordinate of the next 'x' to replace
           x_row, x_col = x_coordinates[0]
           # Generate the set of numbers present in the current state
           numbers_in_state = set([int(cell) for row in state for cell in row if cell != 'x'])
           # Generate the set of available numbers to replace the 'x's
           available_numbers = num_range - numbers_in_state
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = str(number)
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal from the top-left corner to the bottom-right corner of the grid
               new_cost = sum(int(cell) for cell in new_state[0]) + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number to replace each 'x' in the state
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing, and that each number can only appear once in the grid; ie It presumes we can replace each 'x' with the minimum available number in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number in the range, the number used to replace the 'x' in the heuristic
   h = 0
   # Generate the set of numbers present in the current state
   numbers_in_state = set([int(cell) for row in state for cell in row if cell != 'x'])
   # Generate the set of available numbers to replace the 'x's
   available_numbers = set(range(40, 81)) - numbers_in_state
   # If there are 'x's in the state
   if any('x' in row for row in state):
       # Add the minimum available number to the estimate for each 'x' in the state
       h += len([cell for row in state for cell in row if cell == 'x']) * min(available_numbers)
   return h


print(a_star())
