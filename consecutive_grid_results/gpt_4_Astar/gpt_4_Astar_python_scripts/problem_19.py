
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 'x', '85'), ('58', 'x', '84'), ('x', '74', '59'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace the 'x's
   available_numbers = set(range(48, 92))


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
       # The goal state is where all 'x's have been replaced with unique integers from the given range
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # For each available number, check if replacing the 'x' with this number results in a valid state, ie the numbers in each row and column are strictly increasing or decreasing
                   for number in available_numbers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid
                       if all(is_increasing_or_decreasing(row) for row in new_state) and all(is_increasing_or_decreasing(col) for col in np.transpose(new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(cell) for cell in new_state[0]) + sum(int(row[-1]) for row in new_state) + sum(int(new_state[k][k]) for k in range(num_rows))
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # Once we have tried all available numbers for the current 'x', break the loop to avoid replacing the other 'x's in the same iteration
                   break
           else:
               continue
           break
   return None


def is_increasing_or_decreasing(arr):
   # Helper function to check if the elements in an array are strictly increasing or decreasing
   # Filter out the 'x's first
   arr = [int(cell) for cell in arr if cell != 'x']
   return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
   # It's consistent because replacing an 'x' reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
   return sum(cell == 'x' for row in state for cell in row)


print(a_star())
