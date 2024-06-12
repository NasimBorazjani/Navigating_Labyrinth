
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('57', 'x', 'x'), ('x', '50', '63'), ('x', '69', '71'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(range(35, 74))
   # The numbers already present in the initial state
   initial_numbers = set(int(num) for row in initial_state for num in row if num != 'x')
   # The numbers that can be used to replace the 'x's are the numbers in the range that are not already present in the initial state
   available_numbers = numbers - initial_numbers


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, available_numbers)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where there are no 'x's in the grid
       if all(num != 'x' for row in state for num in row):
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for num in available_numbers:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                       new_cost = g + sum(int(num) for num in new_state[0] if num != 'x') + sum(int(new_state[k][num_cols - 1 - k]) for k in range(num_rows) if new_state[k][num_cols - 1 - k] != 'x') + sum(int(new_state[k][k]) for k in range(num_rows) if new_state[k][k] != 'x')
                       # The new set of available numbers is the current set of available numbers without the number that was just added to the grid
                       new_available_numbers = available_numbers - {num}


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))
                       # Once an 'x' has been replaced, break the loop to avoid replacing the other 'x's in the same iteration
                       break
               else:
                   continue
               break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers replacing the 'x's must be unique and in the given range, and that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
   # It's consistent because replacing an 'x' reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
   h = sum(1 for row in state for num in row if num == 'x')
   return h


print(a_star())
