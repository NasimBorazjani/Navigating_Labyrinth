
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 89, 95), ('x', 'x', 96), (74, 93, 'x'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(range(45, 99))
   # Define the number of rows and columns in the grid
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range, and the numbers in each row and column are in strictly increasing or decreasing order
       if all(all(cell != 'x' for cell in row) for row in state) and all(is_increasing_or_decreasing(row) for row in state) and all(is_increasing_or_decreasing(col) for col in np.transpose(state)):
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any('x' in row for row in state):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers that are already in the grid
           numbers_in_state = set([cell for row in state for cell in row if cell != 'x'])
           # Get the set of numbers that can be used to replace the 'x's
           available_numbers = num_range - numbers_in_state
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = number
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
               new_cost = sum([cell for cell in new_state[0] if cell != 'x']) + sum([row[-1] for row in new_state if row[-1] != 'x']) + sum([new_state[i][i] for i in range(num_rows) if new_state[i][i] != 'x'])


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def is_increasing_or_decreasing(arr):
   # Helper function to check if the elements in an array are in strictly increasing or decreasing order
   return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be in strictly increasing or decreasing order, and that the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid should be minimized; ie It presumes we can replace any 'x' with any number from the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is equal to the cost of reaching the successor node, ie one replacement
   return sum(cell == 'x' for row in state for cell in row)


print(a_star())
