
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '55'), ('50', 'x', '56'), ('40', '43', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 33
   range_end = 71


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the range of numbers)
   initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check of the current state is the goal state
       # The goal state is where all the numbers in the grid are known and unique
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       # Get the coordinates of the next 'x' in the grid
       x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       # Get the set of all unique numbers in the current state
       numbers_in_state = {int(cell) for row in state for cell in row if cell != 'x'}
       # Get the set of all numbers in the range
       all_numbers = set(range(range_start, range_end))
       # The set of available numbers is the difference between all_numbers and numbers_in_state
       available_numbers = all_numbers - numbers_in_state
       for number in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = str(number)
           new_state = tuple(tuple(row) for row in new_state)
           # Check if the new state is valid, ie if the numbers in each row and column are strictly increasing or decreasing
           if all(all(int(row[i]) < int(row[i + 1]) for i in range(len(row) - 1)) or all(int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1)) for row in new_state) and all(all(int(new_state[i][j]) < int(new_state[i + 1][j]) for i in range(len(new_state) - 1)) or all(int(new_state[i][j]) > int(new_state[i + 1][j]) for i in range(len(new_state) - 1)) for j in range(len(new_state[0]))):
               # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
               new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available numbers that can replace the remaining 'x's in the grid
   # This heuristic is admissible because it always underestimates the cost to reach the goal state, as it presumes we can replace the 'x's with the smallest available numbers, which is not always possible due to the constraints on the order of the numbers in each row and column
   # The heuristic is consistent because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   h = 0
   # Get the set of all unique numbers in the current state
   numbers_in_state = {int(cell) for row in state for cell in row if cell != 'x'}
   # Get the set of all numbers in the range
   all_numbers = set(range(range_start, range_end))
   # The set of available numbers is the difference between all_numbers and numbers_in_state
   available_numbers = all_numbers - numbers_in_state
   # The number of 'x's in the grid
   num_xs = sum(cell == 'x' for row in state for cell in row)
   # The sum of the smallest num_xs numbers in available_numbers
   h = sum(heapq.nsmallest(num_xs, available_numbers))
   return h


print(a_star())
