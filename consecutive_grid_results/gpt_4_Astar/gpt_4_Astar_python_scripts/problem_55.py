
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 38, 19, 'x'), (22, 'x', 'x', 'x'), ('x', 30, 'x', 42), ('x', 'x', 35, 45))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's in the grid
   available_numbers = set(range(10, 51))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, replacements, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers, maintaining the consecutive order in each row and column
       if all(cell != 'x' for row in state for cell in row):
           return replacements


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to replace is the first 'x' in the grid when read row by row from left to right, top to bottom
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The replacement must maintain the consecutive order in the row and column
                   # Thus the replacement must be greater than the largest number before it and smaller than the smallest number after it in the row and column
                   # Get the numbers before and after the 'x' in the row and column
                   row_before = [cell for cell in state[i][:j] if cell != 'x']
                   row_after = [cell for cell in state[i][j+1:] if cell != 'x']
                   col_before = [state[x][j] for x in range(i) if state[x][j] != 'x']
                   col_after = [state[x][j] for x in range(i+1, num_rows) if state[x][j] != 'x']
                   # Get the largest number before and smallest number after the 'x' in the row and column
                   row_before_max = max(row_before) if row_before else 10
                   row_after_min = min(row_after) if row_after else 50
                   col_before_max = max(col_before) if col_before else 10
                   col_after_min = min(col_after) if col_after else 50
                   # The replacement must be greater than the largest number before it and smaller than the smallest number after it in the row and column
                   replacements_pool = [num for num in available_numbers if row_before_max < num < row_after_min and col_before_max < num < col_after_min]
                   for replacement in replacements_pool:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = replacement
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                       new_cost = sum(new_state[0]) + sum(new_state[x][num_cols-1] for x in range(num_rows)) + sum(new_state[x][x] for x in range(num_rows))
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The replacement must be added to the list of replacements
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, replacements + [(i, j, replacement)], new_state))
                           # The replacement must be removed from the pool of available numbers for the next states
                           available_numbers.remove(replacement)
                           break
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of remaining 'x's in the grid
   # The heuristic relaxes the constraints that the replacements must maintain the consecutive order in each row and column and that each number can only appear once in the grid; ie It presumes we can replace all the 'x's with the smallest available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the smallest available number, the number used to replace the 'x's in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the number used to replace the 'x') + h(n’)
   return sum(cell == 'x' for row in state for cell in row) * min(range(10, 51))


print(a_star())
