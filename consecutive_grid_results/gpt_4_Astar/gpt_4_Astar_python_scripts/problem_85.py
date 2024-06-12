
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('71', 'x', '57', 'x'), ('67', '68', 'x', '73'), ('51', 'x', '72', 'x'), ('50', 'x', '75', 'x'))
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
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the set of numbers that are already in the grid
                   used_numbers = set(int(num) for num in np.array(state).flatten() if num != 'x')
                   # Get the set of numbers that can be used to replace the 'x'
                   available_numbers = num_range - used_numbers
                   for num in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(is_increasing_or_decreasing([int(num) for num in row if num != 'x']) for row in new_state) and all(is_increasing_or_decreasing([int(new_state[x][y]) for x in range(num_rows) if new_state[x][y] != 'x']) for y in range(num_cols)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(num) for num in new_state[0] if num != 'x') + sum(int(new_state[x][num_cols - 1]) for x in range(num_rows) if new_state[x][num_cols - 1] != 'x') + sum(int(new_state[x][x]) for x in range(num_rows) if new_state[x][x] != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                   # Only replace one 'x' at a time
                   break
           else:
               continue
           break
   return None


def is_increasing_or_decreasing(lst):
   # Check if a list of numbers is strictly increasing or decreasing
   return all(x < y for x, y in zip(lst, lst[1:])) or all(x > y for x, y in zip(lst, lst[1:]))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
   # It's consistent because replacing an 'x' in the grid reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
   return sum(row.count('x') for row in state)


print(a_star())
