
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', '68', '71', 'x'), ('x', 'x', '62', 'x'), ('43', 'x', '55', 'x'), ('44', '45', '52', '58'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers = set(range(31, 77))
   # Remove the numbers already present in the grid from the set of available numbers
   for row in initial_state:
       for number in row:
           if number != 'x':
               numbers.remove(int(number))
   # Define the initial state as a tuple of the grid and the set of available numbers
   initial_state = (initial_state, tuple(numbers))
  
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


       # Unpack the state into the grid and the set of available numbers
       grid, numbers = state


       # If the grid has no 'x's, ie all of the numbers have been filled in, return the actions taken to reach this state
       if all(number != 'x' for row in grid for number in row):
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for number in numbers:
           # Find the next 'x' in the grid
           for i in range(len(grid)):
               for j in range(len(grid[i])):
                   if grid[i][j] == 'x':
                       # Generate the new state
                       new_grid = [list(row[:]) for row in grid]
                       new_grid[i][j] = str(number)
                       new_grid = tuple(tuple(row) for row in new_grid)
                       # Remove the number used to replace the 'x' from the set of available numbers
                       new_numbers = list(numbers[:])
                       new_numbers.remove(number)
                       new_numbers = tuple(new_numbers)
                       new_state = (new_grid, new_numbers)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                       new_cost = sum(int(number) for number in new_grid[0] if number != 'x') + sum(int(new_grid[i][-1]) for i in range(len(new_grid)) if new_grid[i][-1] != 'x') + sum(int(new_grid[i][i]) for i in range(len(new_grid)) if new_grid[i][i] != 'x')


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The action taken to reach the new state is replacing the 'x' at coordinate (i, j) with the number
                           heapq.heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(i, j, number)], new_state))
                       # Once an 'x' has been replaced, break the loop to avoid replacing multiple 'x's in one action
                       break
               else:
                   continue
               break
   return None


def heuristic(grid):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing, and that each number can only appear once in the grid; ie It presumes we can replace all of the 'x's with any number
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid, which is always greater than or equal to 1, the decrease in the count of 'x's
   return sum(1 for row in grid for number in row if number == 'x')


print(a_star())
