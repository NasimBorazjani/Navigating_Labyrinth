
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('45', '55', '59', 'x'), ('x', '67', 'x', 'x'), ('60', 'x', '79', '80'), ('x', 'x', 'x', '83'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers_range = set(str(i) for i in range(44, 85))
   # Define the numbers that are already in the grid
   numbers_in_grid = set([num for row in initial_state for num in row if num != 'x'])
   # Define the numbers that are available to replace the 'x's
   available_numbers = numbers_range - numbers_in_grid
   # Define the number of rows and columns in the grid
   num_rows = 4
   num_cols = 4
   # Define the indices of the 'x's in the grid
   x_indices = [(i, j) for i in range(num_rows) for j in range(num_cols) if initial_state[i][j] == 'x']
   # Define the number of 'x's in the grid
   num_x = len(x_indices)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state, available_numbers)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, replacements, state, available_numbers = heapq.heappop(queue)


       # If the current state has no 'x's, ie all of the 'x's have been replaced, return the replacements
       if 'x' not in [num for row in state for num in row]:
           return replacements


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       # The next 'x' to be replaced is the one with the smallest index
       next_x_ind = min([ind for ind in x_indices if state[ind[0]][ind[1]] == 'x'])
       for num in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[next_x_ind[0]][next_x_ind[1]] = num
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner of the grid
           # Filter out the 'x's before calculating the sum
           new_cost = sum(int(num) for num in new_state[0] if num != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               # Update the set of available numbers after each number is added to the grid to ensure all of the numbers in the final grid are uique 
               available_numbers_new = available_numbers - set([num])
               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, replacements + [(*next_x_ind, int(num))], new_state, available_numbers_new))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only appear once in the grid; ie It presumes we can replace each 'x' with the smallest available number
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the smallest available number, the number used to replace the 'x' in the heuristic
   return sum(int(min(available_numbers)) for num in [num for row in state for num in row] if num == 'x')


print(a_star())
