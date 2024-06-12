
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 'x', 'x'), ('x', 51, 'x'), ('x', 61, 64))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(34, 68))


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


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to replace is the first 'x' in the flattened state
       x_ind = np.array(state).flatten().tolist().index('x')
       # Convert the index of the 'x' in the flattened state to its row and column indices in the 2d state
       x_row, x_col = x_ind // num_cols, x_ind % num_cols
       # The available numbers are all numbers in the range that are not already in the state
       available_numbers = set(range(34, 68)) - set(np.array(state).flatten().tolist())
       for number in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = number
           # Check if the new state is valid, ie if the numbers in each row and column are strictly increasing or decreasing
           if all(row[i] < row[i + 1] for row in new_state for i in range(len(row) - 1)) or all(row[i] > row[i + 1] for row in new_state for i in range(len(row) - 1)):
               if all(new_state[i][col] < new_state[i + 1][col] for col in range(num_cols) for i in range(num_rows - 1)) or all(new_state[i][col] > new_state[i + 1][col] for col in range(num_cols) for i in range(num_rows - 1)):
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                   new_cost = sum(new_state[0]) + sum(new_state[i][-1] for i in range(num_rows)) + sum(new_state[i][i] for i in range(num_rows))


                   # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of remaining 'x's in the state
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only be used once; ie It presumes we can replace all of the 'x's with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   return np.array(state).flatten().tolist().count('x') * min(set(range(34, 68)) - set(np.array(state).flatten().tolist()))


print(a_star())
