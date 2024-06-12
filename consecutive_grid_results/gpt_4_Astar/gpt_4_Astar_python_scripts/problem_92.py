
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 28, 11, 'x'), ('x', 27, 'x', 'x'), (15, 'x', 'x', 46), ('x', 'x', 'x', 50))
   # Define the range of unique integers that can be used to replace the 'x's
   unique_integers = set(range(6, 62))
   # Define the size of the grid
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, unique_integers)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all 'x's have been replaced with unique integers, maintaining the consecutive order in each row and column
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie if the consecutive order in each row and column is maintained
                       if all(new_state[row][col] < new_state[row][col + 1] for row in range(num_rows) for col in range(num_cols - 1) if isinstance(new_state[row][col], int) and isinstance(new_state[row][col + 1], int)) and all(new_state[row][col] < new_state[row + 1][col] for row in range(num_rows - 1) for col in range(num_cols) if isinstance(new_state[row][col], int) and isinstance(new_state[row + 1][col], int)):
                           # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                           new_cost = sum(int(new_state[0][col]) for col in range(num_cols) if isinstance(new_state[0][col], int)) + sum(int(new_state[row][num_cols - 1]) for row in range(num_rows) if isinstance(new_state[row][num_cols - 1], int)) + sum(int(new_state[row][row]) for row in range(num_rows) if isinstance(new_state[row][row], int))


                           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action is valid, generate the new action
                               action = (i, j, number)
                               # Update the set of available numbers
                               available_numbers_new = available_numbers - {number}
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [action], new_state, available_numbers_new))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available unique integer for each 'x' in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be in consecutive order and that each number in the grid must be unique; ie It presumes we can replace each 'x' with the minimum available unique integer without considering the other 'x's
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available unique integer, the decrease in the heuristic cost
   return sum(min(unique_integers - set(np.array(state).flatten())) for _ in range(np.count_nonzero(np.array(state) == 'x')))


print(a_star())
