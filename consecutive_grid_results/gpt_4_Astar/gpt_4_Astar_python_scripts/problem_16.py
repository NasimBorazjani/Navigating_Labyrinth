
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('37', 'x', 'x'), ('x', 'x', 'x'), ('44', 'x', '61'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace the 'x's in the grid
   available_numbers = set(range(28, 67))


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


       # Check of the current state is the goal state
       # The goal state is where all the 'x's in the grid have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # For each available number, generate a new state
                   for number in available_numbers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(is_increasing_or_decreasing([int(new_state[k][l]) for k in range(num_rows) if new_state[k][l] != 'x']) for l in range(num_cols)) and all(is_increasing_or_decreasing([int(new_state[k][l]) for k in range(num_cols) if new_state[k][l] != 'x']) for l in range(num_rows)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                           new_cost = sum(int(new_state[0][l]) for l in range(num_cols) if new_state[0][l] != 'x') + sum(int(new_state[k][num_cols - 1]) for k in range(num_rows) if new_state[k][num_cols - 1] != 'x') + sum(int(new_state[k][k]) for k in range(num_rows) if new_state[k][k] != 'x')


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action is valid, generate the new state
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                               # Update the set of available numbers
                               available_numbers.remove(number)
                               break
                   break
           else:
               continue
           break
   return None


def is_increasing_or_decreasing(lst):
   # Helper function to check if a list of numbers is strictly increasing or decreasing
   return all(x < y for x, y in zip(lst, lst[1:])) or all(x > y for x, y in zip(lst, lst[1:]))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid should be minimized; ie It presumes we can replace any 'x' with any available number
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid, which is always greater than or equal to 1, the decrease in the count of 'x's
   return np.array(state).flatten().tolist().count('x')


print(a_star())
