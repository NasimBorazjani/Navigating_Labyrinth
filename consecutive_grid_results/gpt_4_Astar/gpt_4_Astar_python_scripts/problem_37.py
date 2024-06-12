
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('57', 'x', '86'), ('x', '75', 'x'), ('x', '76', '90'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(range(48, 102))


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
       # The goal state is where there are no 'x's in the grid
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the set of numbers that are already in the grid
                   used_numbers = set([int(num) for num in np.array(state).flatten() if num != 'x'])
                   # The available numbers are the numbers in the range that are not already in the grid
                   available_numbers = numbers - used_numbers
                   for num in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(is_increasing_or_decreasing([int(num) for num in row if num != 'x']) for row in new_state) and all(is_increasing_or_decreasing([int(num) for num in column if num != 'x']) for column in zip(*new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                           new_cost = sum([int(num) for num in new_state[0] if num != 'x']) + sum([int(num) for num in [row[-1] for row in new_state] if num != 'x']) + sum([int(num) for num in [new_state[k][k] for k in range(num_rows)] if num != 'x'])
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                   # Once we have generated all possible states from replacing the current 'x', we can break the loop as we only replace one 'x' at a time
                   break
           else:
               continue
           break
   return None


def is_increasing_or_decreasing(lst):
   # Helper function to check if a list of numbers is strictly increasing or decreasing
   return all(x < y for x, y in zip(lst, lst[1:])) or all(x > y for x, y in zip(lst, lst[1:]))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
   # It's consistent because replacing an 'x' in the grid reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
   return np.array(state).flatten().tolist().count('x')


print(a_star())
