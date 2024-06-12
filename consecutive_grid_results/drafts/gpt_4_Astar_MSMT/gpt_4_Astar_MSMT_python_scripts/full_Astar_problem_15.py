
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '23'), ('31', 'x', 'x'), ('x', '42', '51'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's in the grid
   numbers = set(range(18, 56))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, numbers, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the range of numbers that can be used to replace the 'x's)
   initial_state, num_rows, num_cols, numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check of the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the range, and the numbers in each row and column are in consecutive order
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The next 'x' is at coordinate (i, j)
                   # Generate the new state by replacing the 'x' at (i, j) with any of the available unique integers in the range
                   for number in numbers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are in consecutive order
                       if all(int(new_state[i][j]) < int(new_state[i][j + 1]) for i in range(num_rows) for j in range(num_cols - 1) if new_state[i][j] != 'x' and new_state[i][j + 1] != 'x') and all(int(new_state[i][j]) < int(new_state[i + 1][j]) for i in range(num_rows - 1) for j in range(num_cols) if new_state[i][j] != 'x' and new_state[i + 1][j] != 'x'):
                           # The cost so far is the sum of the numbers in the topmost row, rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                           new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


                           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum remaining numbers that can be used to replace the 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum remaining numbers are always less than or equal to the actual numbers that will replace the 'x's in the grid
   # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' in the grid is the number that replaces the 'x', which is always greater than or equal to the minimum remaining number
   h = 0
   remaining_numbers = sorted(set(range(18, 56)) - set(int(cell) for row in state for cell in row if cell != 'x'))
   for i in range(num_rows):
       for j in range(num_cols):
           if state[i][j] == 'x':
               h += remaining_numbers.pop(0)
   return h


print(a_star())
