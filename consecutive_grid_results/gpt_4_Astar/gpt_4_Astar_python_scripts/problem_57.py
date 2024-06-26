
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('11', '14', 'x', 'x'), ('12', 'x', 'x', '38'), ('x', 'x', 'x', '36'), ('25', 'x', 'x', '34'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(str(i) for i in range(7, 48))
   # Define the size of the grid
   num_rows = 4
   num_cols = 4


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


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers (all numbers in the range - numbers present in the current state) in the range
       # Get the coordinate of the next 'x' in the grid
       x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       # Get the set of numbers that are already in the grid
       numbers_in_grid = set(np.array(state).flatten())
       # Get the set of numbers that can be used to replace the 'x's
       available_numbers = num_range - numbers_in_grid
       for number in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = number
           new_state = tuple(tuple(row) for row in new_state)
           # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
           if all(is_increasing_or_decreasing(row) for row in new_state) and all(is_increasing_or_decreasing(col) for col in np.array(new_state).T):
               # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
               new_cost = sum(int(num) for num in new_state[0]) + sum(int(num) for num in np.array(new_state).T[-1]) + sum(int(new_state[i][i]) for i in range(num_rows))
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, int(number))], new_state))
   return None


def is_increasing_or_decreasing(lst):
   # Helper function to check if a list of numbers is strictly increasing or decreasing
   # Filter out the 'x's first
   lst = [int(num) for num in lst if num != 'x']
   return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the number of 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing, and that each number can only appear once in the grid; ie It presumes we can replace any 'x' with any number from the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner, which is always greater than or equal to 1, the decrease in the number of 'x's
   return np.array(state).flatten().tolist().count('x')


print(a_star())
