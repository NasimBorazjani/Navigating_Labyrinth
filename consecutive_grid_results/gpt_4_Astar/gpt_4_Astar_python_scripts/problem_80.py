
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 33, 34, 47), ('x', 'x', 'x', 50), ('x', 'x', 'x', 52), ('x', 'x', 'x', 53))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's
   available_numbers = set(range(10, 61))


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
       # The goal state is where all the 'x's have been replaced with unique integers, maintaining the consecutive order in each row and column
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to be replaced is the one that appears first when reading the grid from left to right, top to bottom
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The numbers that have already been used in the grid
                   used_numbers = set([num for row in state for num in row if num != 'x'])
                   # The numbers that can be used to replace the current 'x'
                   numbers_to_use = available_numbers - used_numbers
                   for num in numbers_to_use:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       # Check if the new state maintains the consecutive order in each row and column
                       if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(col) == list(col) or sorted(col, reverse=True) == list(col) for col in zip(*new_state)):
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum([int(num) for num in new_state[0] if num != 'x']) + sum([int(row[-1]) for row in new_state if row[-1] != 'x']) + sum([int(new_state[k][k]) for k in range(num_rows) if new_state[k][k] != 'x'])


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                   # Once we have generated all possible states from the current 'x', break the loop to avoid generating states from other 'x's in the same iteration
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers replacing the 'x's must be unique and maintain the consecutive order in each row and column, and presumes we can replace all the 'x's with the same number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because replacing an 'x' in the grid reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node, ie one action. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return sum([1 for row in state for num in row if num == 'x'])


print(a_star())
