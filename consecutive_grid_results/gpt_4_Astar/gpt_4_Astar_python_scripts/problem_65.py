
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('10', '26', '30', '46'), ('x', '33', '43', 'x'), ('21', '40', 'x', 'x'), ('x', 'x', 'x', '52'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's in the grid
   available_numbers = set(range(9, 55))


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
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to replace is the one that appears first when reading the grid from left to right, top to bottom
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The available numbers are all the numbers in the range that are not already in the grid
                   available_numbers = set(range(9, 55)) - set(int(x) for x in np.array(state).flatten() if x != 'x')
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are in consecutive order
                       if all(is_consecutive([int(x) for x in row if x != 'x']) for row in new_state) and all(is_consecutive([int(x) for x in col if x != 'x']) for col in zip(*new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(x) for x in new_state[0] if x != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


                           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # Once we have generated all possible states from replacing the current 'x', we can break the loop as we only replace one 'x' at a time
                   break
           else:
               continue
           break
   return None


def is_consecutive(lst):
   # Helper function to check if the numbers in a list are in consecutive order
   return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
   # It's consistent because replacing an 'x' in the grid reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
   return sum(row.count('x') for row in state)


print(a_star())
