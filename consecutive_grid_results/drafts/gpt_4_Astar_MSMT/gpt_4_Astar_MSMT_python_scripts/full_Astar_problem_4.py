
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', '32', '37'), ('29', 'x', 'x'), ('x', '46', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(20, 53))


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
       # The goal state is where all the numbers in the grid are known
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       # Get the coordinate of the next 'x' in the grid
       x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       # Get the set of numbers present in the current state
       numbers_in_state = set([int(num) for num in np.array(state).flatten() if num != 'x'])
       # Get the set of numbers that can replace the 'x'
       numbers_to_replace_x = available_numbers - numbers_in_state
       for num in numbers_to_replace_x:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = str(num)
           new_state = tuple(tuple(row) for row in new_state)
           # Check if the new state is valid, ie the numbers in each row and column are in increasing or decreasing order
           if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(col) == list(col) or sorted(col, reverse=True) == list(col) for col in zip(*new_state)):
               # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
               new_cost = sum([int(num) for num in new_state[0] if num != 'x']) + sum([int(row[-1]) for row in new_state if row[-1] != 'x']) + sum([int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x'])


               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available numbers that can replace the remaining 'x's in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum available numbers are the lowest possible numbers that can replace the 'x's
   # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   h = 0
   # Get the set of numbers present in the current state
   numbers_in_state = set([int(num) for num in np.array(state).flatten() if num != 'x'])
   # Get the set of numbers that can replace the 'x'
   numbers_to_replace_x = available_numbers - numbers_in_state
   # Get the count of 'x's in the state
   x_count = list(np.array(state).flatten()).count('x')
   # Add the minimum available numbers that can replace the 'x's to the heuristic cost
   h += sum(sorted(list(numbers_to_replace_x))[:x_count])
   return h


print(a_star())
