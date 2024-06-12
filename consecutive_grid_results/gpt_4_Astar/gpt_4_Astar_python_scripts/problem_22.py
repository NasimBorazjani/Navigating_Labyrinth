
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('16', 'x', 'x'), ('28', '34', 'x'), ('x', '46', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(str(i) for i in range(13, 57))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # The available numbers are all the numbers in the range that are not already in the grid
       available_numbers = numbers - set(np.array(state).flatten())
       for number in available_numbers:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie if the numbers in each row and column are strictly increasing or decreasing
                       if all(is_increasing_or_decreasing(row) for row in new_state) and all(is_increasing_or_decreasing(col) for col in zip(*new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(num) for num in new_state[0]) + sum(int(num) for num in zip(*new_state)[-1]) + sum(int(new_state[k][k]) for k in range(num_rows))


                           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
   return None


def is_increasing_or_decreasing(lst):
   # Helper function to check if a list of numbers is strictly increasing or decreasing
   # Filter out the 'x's first
   lst = [int(num) for num in lst if num != 'x']
   return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number in the grid must be unique; ie It presumes we can replace any 'x' with any number from the range
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner, which is always greater than or equal to 1, the decrease in the count of 'x's
   return np.array(state).flatten().tolist().count('x')


print(a_star())
