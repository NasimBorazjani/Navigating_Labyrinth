
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('22', 'x', '48'), ('27', 'x', 'x'), ('x', '42', '52'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(map(str, range(20, 54)))
   # Define the numbers that are already in the grid
   initial_numbers = set([num for row in initial_state for num in row if num != 'x'])
   # Define the numbers that are available to replace the 'x's
   available_numbers = num_range - initial_numbers
   # Define the size of the grid
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state, available_numbers)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, replacements, state, available_numbers = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range
       if 'x' not in [num for row in state for num in row]:
           return replacements


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in [num for row in state for num in row]:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Replace the 'x' with each of the available numbers
                       for num in available_numbers:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                           if all(is_increasing_or_decreasing([int(new_state[k][j]) for k in range(num_rows) if new_state[k][j] != 'x']) for j in range(num_cols)) and all(is_increasing_or_decreasing([int(new_state[i][k]) for k in range(num_cols) if new_state[i][k] != 'x']) for i in range(num_rows)):
                               # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                               new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))
                               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                   visited_costs[new_state] = new_cost
                                   # The replacement made to get to the new state must be added to the replacements
                                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, replacements + [(i, j, int(num))], new_state, available_numbers - set([num])))
                       break
               else:
                   continue
               break
   return None


def is_increasing_or_decreasing(lst):
   # Check if a list of numbers is strictly increasing or decreasing
   return all(x < y for x, y in zip(lst, lst[1:])) or all(x > y for x, y in zip(lst, lst[1:]))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available numbers that can be used to replace the remaining 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only be used once, and presumes we can replace the 'x's with the smallest available numbers
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the smallest available number, the number used to replace the 'x' in the heuristic
   return sum(int(num) for num in sorted([num for row in state for num in row if num != 'x'])[:sum(1 for row in state for num in row if num == 'x')])


print(a_star())
