
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('41', 'x', '21'), ('x', 'x', 'x'), ('12', 'x', '42'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   available_numbers = set(range(11, 49))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return num_rows, num_cols, available_numbers, visited_costs, queue


def a_star():
  
   num_rows, num_cols, available_numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the set of numbers that are already in the grid
                   numbers_in_grid = set([int(num) for num in np.array(state).flatten() if num != 'x'])
                   # The numbers that can replace the 'x' are the numbers in the range that are not already in the grid
                   numbers_to_replace_x = available_numbers - numbers_in_grid
                   for num in numbers_to_replace_x:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner
                       new_cost = sum([int(num) for num in new_state[0]]) + sum([int(new_state[k][num_cols - 1]) for k in range(num_rows)]) + sum([int(new_state[k][k]) for k in range(num_rows)])


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only be used once, and presumes we can replace all the 'x's with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of replacing an 'x' with a number is always greater than or equal to the minimum available number, which is exactly the decrease in the heuristic cost, if the 'x' is replaced with the minimum available number, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no 'x's in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 'x':
               h += min(available_numbers)
   return h


print(a_star())
