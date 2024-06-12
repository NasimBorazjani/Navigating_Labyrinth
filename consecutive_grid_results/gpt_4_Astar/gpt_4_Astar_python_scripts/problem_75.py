
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('37', '50', 'x', '70'), ('x', '46', 'x', '65'), ('41', '43', 'x', '49'), ('x', '30', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's in the grid
   available_numbers = set(range(22, 73))


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
       # The goal state is where all the 'x's in the grid have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to replace is the first 'x' in the flattened state
       x_ind = list(np.array(state).flatten()).index('x')
       # Convert the index of the 'x' in the flattened state to its row and column index in the 2d state
       x_row, x_col = divmod(x_ind, num_cols)
       # The available numbers are all the numbers in the range that are not already in the state
       available_numbers = set(range(22, 73)) - set(int(num) for num in np.array(state).flatten() if num != 'x')
       for num in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = str(num)
           # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
           if all(all(int(row[i]) < int(row[i + 1]) for i in range(len(row) - 1)) or all(int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1)) for row in new_state) and all(all(int(new_state[i][col]) < int(new_state[i + 1][col]) for i in range(len(new_state) - 1)) or all(int(new_state[i][col]) > int(new_state[i + 1][col]) for i in range(len(new_state) - 1)) for col in range(num_cols)):
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
               new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][-1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number in the grid must be unique; ie It presumes we can replace each 'x' with the minimum available number regardless of its position in the grid
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the number used to replace the 'x' in the heuristic
   h = 0
   # The available numbers are all the numbers in the range that are not already in the state
   available_numbers = sorted(set(range(22, 73)) - set(int(num) for num in np.array(state).flatten() if num != 'x'))
   # The number of 'x's in the state
   num_xs = list(np.array(state).flatten()).count('x')
   # The sum of the minimum available number for each remaining 'x' in the grid
   h = sum(available_numbers[:num_xs])
   return h


print(a_star())
