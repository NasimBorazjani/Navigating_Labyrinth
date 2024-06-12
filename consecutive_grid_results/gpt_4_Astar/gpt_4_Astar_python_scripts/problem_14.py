
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('41', 'x', '21'), ('x', 'x', 'x'), ('12', 'x', '42'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers = set(str(i) for i in range(11, 50))
   # Define the numbers that are already in the grid
   initial_numbers = set([num for row in initial_state for num in row if num != 'x'])
   # Define the numbers that are available to replace the 'x's
   available_numbers = numbers - initial_numbers
   # Define the number of rows and columns in the grid
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, available_numbers)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where there are no 'x's in the grid
       if 'x' not in [num for row in state for num in row]:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for num in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(is_increasing_or_decreasing(row) for row in new_state) and all(is_increasing_or_decreasing([new_state[i][j] for i in range(num_rows)]) for j in range(num_cols)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                           new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state, available_numbers - {num}))
                   break
           else:
               continue
           break
   return None


def is_increasing_or_decreasing(arr):
   # Check if the elements in the array are strictly increasing or decreasing
   # Ignore 'x's in the array
   arr = [int(num) for num in arr if num != 'x']
   return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each 'x' in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only be used once; ie It presumes we can replace each 'x' with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the number used to replace the 'x' in the heuristic
   return sum(int(min(available_numbers)) for num in [num for row in state for num in row] if num == 'x')


print(a_star())
