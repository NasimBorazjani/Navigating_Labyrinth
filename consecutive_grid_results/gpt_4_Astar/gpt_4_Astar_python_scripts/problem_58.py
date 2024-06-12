
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '38', 'x'), ('x', '30', 'x', 'x'), ('20', 'x', '44', 'x'), ('x', '22', 'x', '57'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers = set(range(19, 60))
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
       # The goal state is where all 'x's have been replaced with unique integers from the given range
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers (all numbers in the range - numbers present in the current state)
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the set of numbers present in the current state
                   numbers_in_state = set(int(cell) for row in state for cell in row if cell != 'x')
                   # Get the set of available numbers to replace the 'x'
                   available_numbers = numbers - numbers_in_state
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(is_increasing_or_decreasing([int(cell) for cell in row if cell != 'x']) for row in new_state) and all(is_increasing_or_decreasing([int(new_state[row][col]) for row in range(num_rows) if new_state[row][col] != 'x']) for col in range(num_cols)):
                           # The cost so far is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[row][-1]) for row in range(num_rows) if new_state[row][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # Only replace the first 'x' found in the grid
                   break
           else:
               continue
           break
   return None


def is_increasing_or_decreasing(lst):
   # Check if a list of numbers is strictly increasing or decreasing
   return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the number of 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal from the top-left corner to the bottom-right corner must be minimized; ie It presumes we can replace any 'x' with any number from the given range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to 1, the decrease in the number of 'x's
   return sum(cell == 'x' for row in state for cell in row)


print(a_star())
