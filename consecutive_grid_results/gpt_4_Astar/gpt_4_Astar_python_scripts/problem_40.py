
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', 'x'), ('65', 'x', 'x'), ('79', '73', '50'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   min_num = 34
   max_num = 87
   # The set of all unique numbers that can be used to replace the 'x's in the grid
   available_nums = set(range(min_num, max_num + 1)) - set(int(num) for row in initial_state for num in row if num != 'x')


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
       if all(num != 'x' for row in state for num in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to replace is the first 'x' in the grid when reading the grid from left to right, top to bottom
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The next 'x' to replace is at coordinate (i, j)
                   # Generate all possible new states by replacing the 'x' at (i, j) with any of the available unique integers
                   for num in available_nums:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie if the consecutive order in each row and column is maintained
                       if all(is_consecutive([int(num) for num in row if num != 'x']) for row in new_state) and all(is_consecutive([int(new_state[x][y]) for x in range(num_rows) if new_state[x][y] != 'x']) for y in range(num_cols)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(num) for num in new_state[0] if num != 'x') + sum(int(new_state[x][num_cols - 1]) for x in range(num_rows) if new_state[x][num_cols - 1] != 'x') + sum(int(new_state[x][x]) for x in range(num_rows) if new_state[x][x] != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                   # After generating all possible new states by replacing the 'x' at (i, j), break the loop as we only replace one 'x' at a time
                   break
           else:
               continue
           break
   return None


def is_consecutive(nums):
   # Check if the numbers in a list are consecutive, ie either strictly increasing or strictly decreasing
   return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)) or all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the number of 'x's in the grid
   # The heuristic relaxes the constraints that the numbers replacing the 'x's must be unique and maintain the consecutive order in each row and column, and presumes we can replace all the 'x's with any number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner, which is always greater than or equal to 1, the decrease in the number of 'x's
   return sum(1 for row in state for num in row if num == 'x')


print(a_star())
