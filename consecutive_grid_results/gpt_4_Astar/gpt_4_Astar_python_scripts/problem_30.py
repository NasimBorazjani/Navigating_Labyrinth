
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 57, 'x'), (42, 'x', 72), (39, 'x', 73))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(39, 88))


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
       # Get the numbers present in the current state
       numbers_in_state = set([num for row in state for num in row if num != 'x'])
       # Get the numbers that can be used to replace the 'x's
       numbers_to_use = available_numbers - numbers_in_state
       for num in numbers_to_use:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = num
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
           new_cost = sum([int(num) for num in new_state[0] if num != 'x']) + sum([int(new_state[i][num_cols - 1]) for i in range(num_rows) if new_state[i][num_cols - 1] != 'x']) + sum([int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x'])


           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number to replace each 'x' in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum available number is always less than or equal to the number that will replace the 'x' in the optimal solution
   # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number
   h = 0
   for row in state:
       for num in row:
           if num == 'x':
               h += min(available_numbers - set([num for row in state for num in row if num != 'x']))
   return h


print(a_star())
