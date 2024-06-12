
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('41', '48', 'x'), ('x', 'x', '63'), ('x', 'x', '67'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(str(i) for i in range(41, 74))


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
       # The goal state is where all the 'x's have been replaced with unique integers from the range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The next 'x' is at coordinate (i, j)
                   # The available numbers are all the numbers in the range that are not already in the grid
                   available_numbers = numbers - set(np.array(state).flatten())
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(col) == list(col) or sorted(col, reverse=True) == list(col) for col in zip(*new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(num) for num in new_state[0] if num != 'x') + sum(int(new_state[k][num_cols - 1]) for k in range(num_rows) if new_state[k][num_cols - 1] != 'x') + sum(int(new_state[k][k]) for k in range(num_rows) if new_state[k][k] != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # We only replace one 'x' at a time, thus must break the loop after finding the first 'x'
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only appear once in the grid; ie It presumes we can replace any 'x' with any number from the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner, which is always greater than or equal to 1, the decrease in the count of 'x's
   return np.count_nonzero(np.array(state) == 'x')


print(a_star())
