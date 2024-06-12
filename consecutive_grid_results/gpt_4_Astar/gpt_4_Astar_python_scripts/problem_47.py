
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('27', '37', 'x', 'x'), ('30', 'x', 'x', 'x'), ('32', '44', '53', '61'), ('33', '54', 'x', '64'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's
   available_numbers = set(range(27, 68))


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


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to replace is the first 'x' in the flattened state
       x_ind = list(np.array(state).flatten()).index('x')
       # Convert the index of the 'x' in the flattened state to the row and column index in the 2d state
       x_row, x_col = divmod(x_ind, num_cols)
       # The available numbers are all numbers in the range - numbers present in the current state
       available_numbers = set(range(27, 68)) - set(int(num) for num in np.array(state).flatten() if num != 'x')
       for num in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = str(num)
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
           new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][-1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))


           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the state
   # This heuristic is admissible because it always opts for the action that fills the 'x's with the smallest available number, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is removed from the grid, or equal or less by at most the smallest available number (equal to the cost of reaching the successor node, ie one action) as the maximum amount of number that can be added to the grid is the smallest available number, which is exactly the number used to fill the 'x' in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the smallest available number) + h(n’)
   h = 0
   # The available numbers are all numbers in the range - numbers present in the current state
   available_numbers = sorted(set(range(27, 68)) - set(int(num) for num in np.array(state).flatten() if num != 'x'))
   # The number of 'x's in the state
   num_xs = list(np.array(state).flatten()).count('x')
   # The sum of the minimum available number for each remaining 'x' in the state
   h = sum(available_numbers[:num_xs])
   return h


print(a_star())
