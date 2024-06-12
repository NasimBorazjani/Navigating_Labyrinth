
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '55'), ('50', 'x', '56'), ('40', '43', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(range(33, 72))


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
       # The available numbers are all the numbers in the range minus the numbers already present in the grid
       available_numbers = numbers - set([int(num) for row in state for num in row if num != 'x'])
       for num in available_numbers:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                       new_cost = sum([int(num) for num in new_state[0]]) + sum([int(new_state[k][num_cols - 1]) for k in range(num_rows)]) + sum([int(new_state[k][k]) for k in range(num_rows)])


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                       # Once the 'x' has been replaced with a number, break the loop to avoid replacing the same 'x' multiple times
                       break
               else:
                   continue
               break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of remaining 'x's in the grid
   # This heuristic is admissible because it presumes we can replace all the remaining 'x's with the minimum available number, thus it never overestimates the cost to reach the goal
   # The heuristic is consistent because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   available_numbers = set(range(33, 72)) - set([int(num) for row in state for num in row if num != 'x'])
   min_available_number = min(available_numbers)
   num_remaining_xs = len([num for row in state for num in row if num == 'x'])
   return min_available_number * num_remaining_xs


print(a_star())
