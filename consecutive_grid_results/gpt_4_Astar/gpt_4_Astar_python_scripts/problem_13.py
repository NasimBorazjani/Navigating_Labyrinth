
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('29', '45', 'x'), ('x', 'x', 'x'), ('x', '43', '34'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(21, 60))


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
       # The goal state is where all the 'x's have been replaced with unique integers from the given range, maintaining the consecutive order in each row and column
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # The next 'x' to replace is the first 'x' in the grid when reading the grid from left to right, top to bottom
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The numbers that can replace the 'x' are the numbers in the range that are not already in the grid
                   for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie if the consecutive order in each row and column is maintained
                       if all(int(new_state[i][j]) < int(new_state[i][j + 1]) for i in range(num_rows) for j in range(num_cols - 1) if new_state[i][j] != 'x' and new_state[i][j + 1] != 'x') and all(int(new_state[i][j]) < int(new_state[i + 1][j]) for i in range(num_rows - 1) for j in range(num_cols) if new_state[i][j] != 'x' and new_state[i + 1][j] != 'x'):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows) if new_state[i][num_cols - 1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # Once we have generated all possible states from replacing the current 'x', we can break the loop as we only replace one 'x' at a time
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number that can replace each 'x' in the grid
   # The heuristic relaxes the constraints that the numbers replacing the 'x's must be unique and that the consecutive order in each row and column must be maintained; ie It presumes we can replace each 'x' with the same minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the number used to replace the 'x' in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the number replacing the 'x') + h(n’)
   h = 0
   for row in state:
       for cell in row:
           if cell == 'x':
               h += min(available_numbers - set(cell for row in state for cell in row if cell != 'x'))
   return h


print(a_star())
