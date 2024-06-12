
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('22', 'x', '48'), ('27', 'x', 'x'), ('x', '42', '52'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   available_numbers = set(range(20, 53))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, available_numbers, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the available numbers)
   initial_state, num_rows, num_cols, available_numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # Get the coordinate of the next 'x' in the grid
       x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       # Get the numbers already present in the grid
       numbers_in_grid = set([int(state[i][j]) for i in range(num_rows) for j in range(num_cols) if state[i][j] != 'x'])
       # The numbers that can replace the 'x' are the numbers in the range that are not already in the grid
       numbers_can_replace_x = available_numbers - numbers_in_grid
       for number in numbers_can_replace_x:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = str(number)
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
           # Filter out the 'x's before calculating the sum
           new_cost = sum([int(new_state[0][j]) for j in range(num_cols) if new_state[0][j] != 'x']) + sum([int(new_state[i][num_cols - 1]) for i in range(num_rows) if new_state[i][num_cols - 1] != 'x']) + sum([int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x'])


           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only be used once, ie it presumes we can replace each 'x' with the smallest available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the smallest available number, the number used to estimate the cost in the heuristic
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 'x':
               h += min(available_numbers)
   return h


print(a_star())
