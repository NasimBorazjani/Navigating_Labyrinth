
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('16', '17', 'x'), ('x', 'x', 'x'), ('x', '44', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(16, 54))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, available_numbers, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, number of rows and columns, and the set of available numbers)
   initial_state, num_rows, num_cols, available_numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check of the current state is the goal state
       # The goal state is where each row and column is in consecutive order and there are no 'x's in the grid
       if all(all(cell != 'x' for cell in row) for row in state) and all(all(int(row[i]) < int(row[i + 1]) for i in range(len(row) - 1)) or all(int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1)) for row in state) and all(all(int(state[i][j]) < int(state[i + 1][j]) for i in range(len(state) - 1)) or all(int(state[i][j]) > int(state[i + 1][j]) for i in range(len(state) - 1)) for j in range(len(state[0]))):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers - set([int(cell) for row in state for cell in row if cell != 'x']):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner
                       new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[k][num_cols - 1]) for k in range(num_rows) if new_state[k][num_cols - 1] != 'x') + sum(int(new_state[l][l]) for l in range(min(num_rows, num_cols)) if new_state[l][l] != 'x')


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each 'x' in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced with at least the minimum available number
   # It's consistent because the estimated cost of the next node is higher if an 'x' is replaced with a number greater than the minimum available number, or equal if the 'x' is replaced with the minimum available number, which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       for cell in row:
           if cell == 'x':
               h += min(available_numbers - set([int(cell) for row in state for cell in row if cell != 'x']))
   return h


print(a_star())
