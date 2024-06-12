
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 59, 'x'), (47, 'x', 62), ('x', 50, 63))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(range(41, 79))


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


       # Check if the current state is the goal state
       # The goal state is where each row and column of the grid are consecutive and there are no 'x's in the grid
       if all(all(cell != 'x' for cell in row) for row in state) and all(all(int(row[i]) < int(row[i + 1]) for i in range(len(row) - 1)) or all(int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1)) for row in state) and all(all(int(state[i][col]) < int(state[i + 1][col]) for i in range(len(state) - 1)) or all(int(state[i][col]) > int(state[i + 1][col]) for i in range(len(state) - 1)) for col in range(len(state[0]))):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range
       # Find the next 'x' in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Get the set of numbers that are not in the current state
                   available_numbers = numbers - set([int(cell) for row in state for cell in row if cell != 'x'])
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                       new_cost = sum(int(cell) for cell in new_state[0]) + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, number)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each 'x' in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced with at least the minimum available number
   # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   h = 0
   available_numbers = sorted(list(numbers - set([int(cell) for row in state for cell in row if cell != 'x'])))
   for row in state:
       for cell in row:
           if cell == 'x':
               h += available_numbers.pop(0)
   return h


print(a_star())
