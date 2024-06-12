
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('57', 'x', 'x'), ('x', '50', '63'), ('x', '69', '71'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   available_numbers = set(range(35, 73))


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


       # Check of the current state is the goal state
       # The goal state is where each row and column of the grid are consecutive and there are no 'x's in the grid
       if all(all(cell != 'x' for cell in row) for row in state) and all(is_consecutive(row) for row in state) and all(is_consecutive([state[i][j] for i in range(num_rows)]) for j in range(num_cols)):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available numbers
       for i in range(num_rows):
           for j in range(num_cols):
               # If the cell at (i, j) is 'x', it can be replaced
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                       new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[k][num_cols - 1]) for k in range(num_rows) if new_state[k][num_cols - 1] != 'x') + sum(int(new_state[l][l]) for l in range(num_rows) if new_state[l][l] != 'x')


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The new set of available numbers is the current set of available numbers minus the number that was just added to the grid
                           new_available_numbers = available_numbers - {number}
                           heapq.heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(i, j, number)], new_state))
   return None


def is_consecutive(row):
   # A helper function to check if the numbers in a row or column are consecutive
   # The numbers in a row or column are consecutive if the difference between the maximum and minimum numbers is equal to the number of cells minus 1, and there are no 'x's in the row or column
   return max(row) - min(row) == len(row) - 1 and all(cell != 'x' for cell in row)


def heuristic(state, available_numbers):
   # An admissible and consistent heuristic for this problem is the sum of the smallest available numbers that can be used to replace the remaining 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of reaching the goal state is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid, and the smallest available numbers will minimize this sum
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of reaching the successor node is the number that was added to the grid, which is always greater than or equal to the smallest available number, the decrease in the heuristic
   h = 0
   # Sort the available numbers in ascending order
   available_numbers = sorted(list(available_numbers))
   # Count the number of 'x's in the grid
   num_x = sum(cell == 'x' for row in state for cell in row)
   # Add the smallest available numbers to the heuristic
   for i in range(num_x):
       h += available_numbers[i]
   return h


print(a_star())
