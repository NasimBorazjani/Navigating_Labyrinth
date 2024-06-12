
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 59, 'x'), (47, 'x', 62), ('x', 50, 63))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's in the grid
   available_numbers = set(range(41, 79))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, available_numbers, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the range of numbers that can be used to replace the 'x's)
   initial_state, num_rows, num_cols, available_numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all 'x's have been replaced with unique integers from the range, and the numbers in each row and column are in consecutive order
       if all(all(cell != 'x' for cell in row) for row in state):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # For each available number, generate a new state by replacing the 'x' with the number
                   for number in available_numbers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       # Check if the new state is valid, ie the numbers in each row and column are in consecutive order
                       if all(new_state[row][col] < new_state[row][col + 1] for row in range(num_rows) for col in range(num_cols - 1)) and all(new_state[row][col] < new_state[row + 1][col] for row in range(num_rows - 1) for col in range(num_cols)):
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                           new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[row][-1]) for row in range(num_rows) if new_state[row][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action taken to reach the new state is replacing the 'x' at coordinate (i, j) with the number
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                               # The number used to replace the 'x' is no longer available
                               available_numbers.remove(number)
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of remaining 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be in consecutive order and that each number can only be used once; ie It presumes we can replace all of the 'x's with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic estimate
   return sum(1 for row in state for cell in row if cell == 'x') * min(available_numbers)


print(a_star())
