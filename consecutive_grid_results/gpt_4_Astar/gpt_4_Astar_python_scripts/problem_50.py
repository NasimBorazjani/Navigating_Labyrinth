
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', 'x', '60'), ('47', 'x', '62', '65'), ('x', '58', '67', '68'), ('54', 'x', '74', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's
   available_numbers = set(range(36, 77))


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
       # The goal state is where all the 'x's have been replaced with unique integers, maintaining the consecutive order in each row and column
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The actions are valid if the new state maintains the consecutive order in each row and column
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the numbers present in the current state
                   numbers_in_state = set([int(num) for num in np.array(state).flatten() if num != 'x'])
                   # The numbers that can replace the 'x' are the numbers in the range that are not present in the current state
                   numbers_can_use = available_numbers - numbers_in_state
                   for num in numbers_can_use:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state maintains the consecutive order in each row and column
                       if all(is_consecutive(row) for row in new_state) and all(is_consecutive(col) for col in zip(*new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                           new_cost = sum([int(num) for num in new_state[0] if num != 'x']) + sum([int(row[-1]) for row in new_state if row[-1] != 'x']) + sum([int(new_state[k][k]) for k in range(num_rows) if new_state[k][k] != 'x'])
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                   break
           else:
               continue
           break
   return None


def is_consecutive(lst):
   # A helper function to check if the numbers in a list are consecutive
   # The list is consecutive if the difference between the maximum and minimum number is equal to the length of the list - 1, and the number of unique elements in the list is equal to the length of the list
   lst = [int(num) for num in lst if num != 'x']
   if len(lst) > 1:
       return max(lst) - min(lst) == len(lst) - 1 and len(set(lst)) == len(lst)
   return True


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the state
   # The heuristic relaxes the constraints that the numbers replacing the 'x's must be unique and maintain the consecutive order in each row and column, and presumes we can replace all the 'x's with any number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum decrease in the count of 'x's is 1, which is exactly the decrease in the count of 'x's if an 'x' is replaced with a number. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return np.array(state).flatten().tolist().count('x')


print(a_star())
