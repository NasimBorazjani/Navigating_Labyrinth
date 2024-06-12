
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('30', 'x', 'x'), ('28', '33', '43'), ('x', 'x', '51'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers_range = set(map(str, range(15, 59)))


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


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the unique integers in the range
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the set of numbers that are already in the grid
                   numbers_in_grid = set(np.array(state).flatten())
                   # Get the set of numbers that can be used to replace the 'x'
                   available_numbers = numbers_range - numbers_in_grid
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(is_increasing_or_decreasing(row) for row in new_state) and all(is_increasing_or_decreasing(col) for col in np.array(new_state).T):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(num) for num in new_state[0]) + sum(int(num) for num in np.array(new_state).T[-1]) + sum(int(new_state[i][i]) for i in range(num_rows))
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, int(number))], new_state))
                   # Only need to replace one 'x' at a time
                   return None
   return None


def is_increasing_or_decreasing(lst):
   # Helper function to check if a list of numbers is strictly increasing or decreasing
   # Filter out the 'x's first
   lst = [int(num) for num in lst if num != 'x']
   return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum numbers that can be used to replace the 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only appear once in the grid; ie It presumes we can replace the 'x's with any of the numbers in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum number in the range, the number used to replace the 'x' in the heuristic
   # Thus h(n) can never be greater than c(n, n’)(equal to the number used to replace the 'x') + h(n’)
   h = 0
   # Get the set of numbers that are already in the grid
   numbers_in_grid = set(np.array(state).flatten())
   # Get the set of numbers that can be used to replace the 'x's
   available_numbers = numbers_range - numbers_in_grid
   # Get the number of 'x's in the grid
   num_xs = list(np.array(state).flatten()).count('x')
   # The heuristic is the sum of the minimum numbers that can be used to replace the 'x's
   h = sum(sorted(map(int, available_numbers))[:num_xs])
   return h


print(a_star())
