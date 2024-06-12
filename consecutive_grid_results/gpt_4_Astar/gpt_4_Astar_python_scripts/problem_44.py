
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 58, 'x'), (42, 'x', 70), ('x', 'x', 'x'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers = set(range(31, 85))
   # Define the size of the grid
   num_rows = 3
   num_cols = 3


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
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers (all numbers in the range - numbers present in the current state)
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the set of numbers that are already in the grid
                   used_numbers = set(cell for row in state for cell in row if cell != 'x')
                   # Get the set of numbers that can be used to replace the 'x'
                   available_numbers = numbers - used_numbers
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner
                       new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[k][num_cols - 1]) for k in range(num_rows) if new_state[k][num_cols - 1] != 'x') + sum(int(new_state[k][k]) for k in range(num_rows) if new_state[k][k] != 'x')


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
                   return None
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only be used once, and presumes we can replace each 'x' with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost. Thus h(n) can never be greater than c(n, n’)(equal to the number used to replace the 'x') + h(n’)
   h = 0
   # Get the set of numbers that are already in the grid
   used_numbers = set(cell for row in state for cell in row if cell != 'x')
   # Get the set of numbers that can be used to replace the 'x'
   available_numbers = sorted(list(numbers - used_numbers))
   # Count the number of 'x's in the grid
   num_x = sum(cell == 'x' for row in state for cell in row)
   # Add the minimum available number for each remaining 'x' to the heuristic cost
   for i in range(num_x):
       h += available_numbers[i]
   return h


print(a_star())
