
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 35, 'x', 'x'), (34, 36, 38, 'x'), (29, 'x', 43, 'x'), ('x', 'x', 49, 53))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's in the grid
   available_numbers = set(range(23, 74))


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
       # The goal state is where all 'x's have been replaced with unique integers, thus the goal state has no 'x's
       if 'x' not in np.array(state).flatten():
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in np.array(state).flatten():
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers that are already in the grid
           numbers_in_grid = set([num for row in state for num in row if num != 'x'])
           # The numbers that can replace the 'x' are the numbers in the range that are not already in the grid
           numbers_can_use = available_numbers - numbers_in_grid
           for num in numbers_can_use:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = num
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
               new_cost = sum([int(num) for num in new_state[0] if num != 'x']) + sum([int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x']) + sum([int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x'])


               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum remaining numbers that can be used to replace the 'x's in the grid
   # This heuristic is admissible because it always underestimates the cost to reach the goal state, as it presumes we can always replace the 'x's with the smallest remaining numbers, which is not always possible due to the constraints on the order of the numbers in the rows and columns
   # The heuristic is consistent because the estimated cost of the next node is equal or less than the cost of reaching the successor node plus the estimated cost from the successor node to the goal, as replacing an 'x' with a number increases the cost by at least the smallest remaining number, which is exactly the decrease in the heuristic cost
   h = 0
   # Get the set of numbers that are already in the grid
   numbers_in_grid = set([num for row in state for num in row if num != 'x'])
   # The numbers that can replace the 'x's are the numbers in the range that are not already in the grid
   numbers_can_use = sorted(list(available_numbers - numbers_in_grid))
   # The number of 'x's in the grid
   num_xs = len([num for row in state for num in row if num == 'x'])
   # The sum of the smallest remaining numbers that can replace the 'x's
   h = sum(numbers_can_use[:num_xs])
   return h


print(a_star())
