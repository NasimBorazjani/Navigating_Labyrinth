
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('33', '37', 'x', '58'), ('44', '51', 'x', '63'), ('x', '52', '62', '64'), ('x', 'x', '65', 'x'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(map(str, range(33, 79)))
   # Define the numbers that are already in the grid
   initial_numbers = set([num for row in initial_state for num in row if num != 'x'])
   # Define the numbers that are available to replace the 'x's
   available_numbers = num_range - initial_numbers
   # Define the size of the grid
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state, available_numbers))


   while queue:
       _, g, actions, state, available_numbers = heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x's, return the actions taken
       if 'x' not in [num for row in state for num in row]:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for num in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(col) == list(col) or sorted(col, reverse=True) == list(col) for col in zip(*new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                           new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][-1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))
                           # The new set of available numbers is the current set of available numbers minus the number just added to the grid
                           new_available_numbers = available_numbers - set([num])
                           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # In the problem statement the grid is indexed starting from 1, thus must add 1 to the i and j indices
                               heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
   # It's consistent because replacing an 'x' in the state reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
   return sum(row.count('x') for row in state)


print(a_star())
