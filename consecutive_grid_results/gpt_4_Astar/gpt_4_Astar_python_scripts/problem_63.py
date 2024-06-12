
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 73, 74, 'x'), (46, 'x', 63, 72), ('x', 47, 'x', 'x'), (41, 45, 'x', 54))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's
   available_numbers = set(range(35, 81))


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
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to replace is the first 'x' in the grid when reading the grid from left to right, top to bottom
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # For each available number, check if replacing the 'x' with this number results in a valid state, ie the consecutive order in the row and column of the 'x' is maintained
                   for number in available_numbers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       # Check if the consecutive order in the row and column of the 'x' is maintained
                       if all(new_state[i][k] < new_state[i][k + 1] for k in range(num_cols - 1) if new_state[i][k] != 'x' and new_state[i][k + 1] != 'x') and all(new_state[k][j] < new_state[k + 1][j] for k in range(num_rows - 1) if new_state[k][j] != 'x' and new_state[k + 1][j] != 'x'):
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                           new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[k][num_cols - 1]) for k in range(num_rows) if new_state[k][num_cols - 1] != 'x') + sum(int(new_state[k][k]) for k in range(num_rows) if new_state[k][k] != 'x')


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action is valid, generate the new state
                               # The action is represented as a tuple of the row index of the 'x', the column index of the 'x', and the value of the number that replaces the 'x'
                               # The new set of available numbers is the old set minus the number that was just added to the grid
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                               available_numbers.remove(number)
                               break
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of remaining 'x's in the grid
   # This heuristic is admissible because it presumes we can replace all the remaining 'x's with the minimum available number, thus it never overestimates the cost to reach the goal
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   return sum(cell == 'x' for row in state for cell in row) * min(available_numbers)


print(a_star())
