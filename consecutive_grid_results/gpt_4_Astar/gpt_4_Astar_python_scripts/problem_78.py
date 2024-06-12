
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 'x', 58, 'x'), (44, 54, 59, 'x'), (43, 'x', 63, 75), ('x', 'x', 'x', 84))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's in the grid
   available_numbers = set(range(36, 87))


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
       # The goal state is where all the 'x's in the grid have been replaced with unique integers, maintaining the consecutive order in each row and column
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers that are already in the grid
           numbers_in_grid = set(cell for row in state for cell in row if cell != 'x')
           # The set of numbers that can replace the 'x' are the numbers in the range that are not already in the grid
           numbers_to_replace_x = available_numbers - numbers_in_grid
           for number in numbers_to_replace_x:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = number
               # Check if the new state maintains the consecutive order in each row and column
               if all(new_state[i][j] < new_state[i][j + 1] for i in range(num_rows) for j in range(num_cols - 1) if new_state[i][j] != 'x' and new_state[i][j + 1] != 'x') and all(new_state[i][j] < new_state[i + 1][j] for i in range(num_rows - 1) for j in range(num_cols) if new_state[i][j] != 'x' and new_state[i + 1][j] != 'x'):
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                   new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows) if new_state[i][num_cols - 1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state)
                       # In the problem statement the grid is indexed starting from 0, thus must add 1 to the x_row and x_col
                       heappush(queue, (new_cost + h, new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers replacing the 'x's must be unique and maintain the consecutive order in each row and column; ie It presumes we can replace all the 'x's with any number
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner, which is always greater than or equal to 1, the decrease in the count of 'x's
   return sum(cell == 'x' for row in state for cell in row)


print(a_star())
