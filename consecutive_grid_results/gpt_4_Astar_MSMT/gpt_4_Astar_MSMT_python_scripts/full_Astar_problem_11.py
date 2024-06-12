
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '55'), ('50', 'x', '56'), ('40', '43', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(33, 71))


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
       # The goal state is where each row and column of the grid is consecutive and there are no 'x's in the grid
       if all(all(cell != 'x' for cell in row) for row in state) and all(is_consecutive(row) for row in state) and all(is_consecutive([state[i][j] for i in range(num_rows)]) for j in range(num_cols)):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available numbers
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                       new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows) if new_state[i][num_cols - 1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                           # Update the set of available numbers
                           available_numbers.remove(number)
   return None


def is_consecutive(row):
   # Helper function to check if the numbers in a row or column are consecutive
   # Convert the elements of the row to integers and sort the row
   row = sorted([int(cell) for cell in row if cell != 'x'])
   # Check if the difference between each pair of consecutive numbers in the row is 1
   return all(row[i + 1] - row[i] == 1 for i in range(len(row) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraint that the numbers in each row and column must be consecutive and presumes we can replace the 'x's with any of the available numbers
   # It is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
   # It's consistent because replacing an 'x' reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       for cell in row:
           if cell == 'x':
               h += 1
   return h


print(a_star())
