
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 53, 'x', 79), (46, 51, 'x', 78), (45, 'x', 73, 77), (42, 47, 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's in the grid
   available_numbers = set(range(40, 81))


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
       # The goal state is where all the 'x's in the grid have been replaced with unique integers from the given range, maintaining the consecutive order in each row and column
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to replace is the first 'x' in the flattened state
       x_ind = list(np.array(state).flatten()).index('x')
       # Convert the index of the 'x' in the flattened state to its row and column indices in the 2d state
       x_row, x_col = divmod(x_ind, num_cols)
       # The available numbers are all the numbers in the range that are not already in the state
       available_numbers = set(range(40, 81)) - set(np.array(state).flatten())
       for number in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = number
           # Check if the new state maintains the consecutive order in each row and column
           if all(all(np.diff(row) > 0) or all(np.diff(row) < 0) for row in new_state) and all(all(np.diff(col) > 0) or all(np.diff(col) < 0) for col in np.transpose(new_state)):
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
               new_cost = sum(int(i) for i in new_state[0] if i != 'x') + sum(int(i[-1]) for i in new_state if i[-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the state
   # This heuristic is admissible because it always underestimates the cost to reach the goal state, as it presumes we can always replace the 'x's with the minimum available number, which is not always possible due to the constraint on the consecutive order in each row and column
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   h = 0
   available_numbers = set(range(40, 81)) - set(np.array(state).flatten())
   for _ in range(list(np.array(state).flatten()).count('x')):
       h += min(available_numbers)
       available_numbers.remove(min(available_numbers))
   return h


print(a_star())
