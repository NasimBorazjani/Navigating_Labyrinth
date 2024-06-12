
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 36, 71, 79), ('x', 'x', 69, 'x'), ('x', 50, 63, 70), (21, 53, 'x', 62))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   available_numbers = set(range(20, 81))


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
       # The goal state is where all the 'x's have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # Get the coordinate of the next 'x' in the grid
       x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       # Get the set of numbers that are already in the grid
       numbers_in_grid = set([num for row in state for num in row if num != 'x'])
       # The set of available numbers is the difference between all numbers in the range and the numbers already in the grid
       available_numbers = set(range(20, 81)) - numbers_in_grid
       for number in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = number
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
           new_cost = sum([num for num in new_state[0] if num != 'x']) + sum([row[-1] for row in new_state if row[-1] != 'x']) + sum([new_state[i][i] for i in range(num_rows) if new_state[i][i] != 'x'])


           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of remaining 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only appear once in the grid; ie It presumes we can replace all of the remaining 'x's with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic estimate
   h = 0
   # Get the set of numbers that are already in the grid
   numbers_in_grid = set([num for row in state for num in row if num != 'x'])
   # The set of available numbers is the difference between all numbers in the range and the numbers already in the grid
   available_numbers = set(range(20, 81)) - numbers_in_grid
   # Get the minimum available number
   min_available_number = min(available_numbers)
   # Get the number of remaining 'x's in the grid
   num_remaining_xs = len([1 for row in state for num in row if num == 'x'])
   h = min_available_number * num_remaining_xs
   return h


print(a_star())
