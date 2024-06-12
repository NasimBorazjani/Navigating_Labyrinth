
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('10', '15', '39'), ('x', '27', '29'), ('x', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(map(str, range(8, 41)))
   # The numbers already present in the initial state
   initial_numbers = set([num for row in initial_state for num in row if num != 'x'])
   # The numbers that can be used to replace the 'x's are the numbers in the range that are not already present in the initial state
   available_numbers = numbers - initial_numbers


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return num_rows, num_cols, available_numbers, visited_costs, queue


def a_star():
  
   num_rows, num_cols, available_numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the range, maintaining the consecutive order in each row and column
       if 'x' not in [num for row in state for num in row]:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The next 'x' to be replaced is the first 'x' in the grid when read row by row from left to right, top to bottom
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The 'x' at (i, j) is the next 'x' to be replaced
                   # Generate the new state by replacing the 'x' at (i, j) with each of the available numbers
                   for num in available_numbers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       # Check if the new state maintains the consecutive order in each row and column
                       if all(int(new_state[i][k]) < int(new_state[i][k + 1]) for k in range(num_cols - 1) for i in range(num_rows)) and all(int(new_state[k][j]) < int(new_state[k + 1][j]) for k in range(num_rows - 1) for j in range(num_cols)):
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                           new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][-1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each 'x' in the state
   # The heuristic relaxes the constraints that the numbers in each row and column must be in consecutive order and that each number can only be used once, and presumes we can replace each 'x' with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the number used to estimate the cost in the heuristic
   h = 0
   for row in state:
       for num in row:
           if num == 'x':
               h += min(available_numbers)
   return h


print(a_star())
