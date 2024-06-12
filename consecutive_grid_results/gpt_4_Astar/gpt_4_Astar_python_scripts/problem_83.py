
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('38', 'x', '50', 'x'), ('x', 'x', '64', '67'), ('54', 'x', '71', '79'), ('x', '59', '89', '90'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's
   available_numbers = set(range(36, 92))


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
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # For each available number, check if replacing the 'x' with the number results in a valid state, ie the numbers in the row and column of the new number are in strictly increasing or decreasing order
                   for number in available_numbers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid
                       if all(is_increasing_or_decreasing(row) for row in new_state) and all(is_increasing_or_decreasing(row) for row in zip(*new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the main diagonal
                           new_cost = sum(int(num) for num in new_state[0]) + sum(int(row[-1]) for row in new_state) + sum(int(new_state[k][k]) for k in range(num_rows))
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
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
   # Helper function to check if a list of numbers is in strictly increasing or decreasing order
   # Filter out the 'x's first
   lst = [int(num) for num in lst if num != 'x']
   return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of remaining 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be in strictly increasing or decreasing order and that each number in the grid must be unique; ie It presumes we can replace all the 'x's with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   return sum(1 for num in np.array(state).flatten() if num == 'x') * min(available_numbers)


print(a_star())
