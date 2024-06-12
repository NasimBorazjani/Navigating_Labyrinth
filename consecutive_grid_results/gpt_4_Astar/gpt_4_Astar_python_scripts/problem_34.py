
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('38', 'x', '77'), ('x', 'x', 'x'), ('x', '52', 'x'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(str(i) for i in range(38, 87))
   # Define the numbers that are already in the grid
   initial_numbers = set([num for row in initial_state for num in row if num != 'x'])
   # Define the numbers that are available to replace the 'x's
   available_numbers = num_range - initial_numbers
   # Define the number of rows and columns in the grid
   num_rows = 3
   num_cols = 3


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


       # If the state has no remaining unknown numbers, ie 'x', return the replacements made to reach this state
       if 'x' not in [num for row in state for num in row]:
           return replacements


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for num in available_numbers:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                       new_cost = sum(int(num) for num in new_state[0] if num != 'x') + sum(int(new_state[k][num_cols - 1]) for k in range(num_rows) if new_state[k][num_cols - 1] != 'x') + sum(int(new_state[k][k]) for k in range(num_rows) if new_state[k][k] != 'x')


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The new number must be removed from the set of available numbers
                           new_available_numbers = available_numbers - set([num])
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, replacements + [(i, j, int(num))], new_state, new_available_numbers))
                       # Break the loop after the first 'x' is replaced
                       break
               else:
                   continue
               break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the state
   # This heuristic relaxes the constraints that the numbers in the grid must be unique and that the numbers in each row and column must be strictly increasing or decreasing; ie It presumes we can replace all of the 'x's with any number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid, which is always greater than or equal to 1, the decrease in the count of 'x's
   return sum(1 for row in state for num in row if num == 'x')


print(a_star())
