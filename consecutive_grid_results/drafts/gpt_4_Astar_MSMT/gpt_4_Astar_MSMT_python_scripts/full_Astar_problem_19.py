
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '85'), ('58', 'x', '84'), ('x', '74', '59'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(range(48, 91))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, numbers, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the range of numbers)
   initial_state, num_rows, num_cols, numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the range, maintaining the consecutive order in each row and column
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The numbers that have been used in the current state
                   used_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
                   # The numbers that are still available to replace the 'x's
                   available_numbers = numbers - used_numbers
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are in consecutive order
                       if all(is_consecutive([cell for cell in row if cell != 'x']) for row in new_state) and all(is_consecutive([new_state[row][col] for row in range(num_rows) if new_state[row][col] != 'x']) for col in range(num_cols)):
                           # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                           new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[row][num_cols - 1]) for row in range(num_rows) if new_state[row][num_cols - 1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # Once we have generated all possible states from replacing the current 'x', we can break the loop as we only replace one 'x' at a time
                   break
           else:
               continue
           break
   return None


def is_consecutive(lst):
   # Helper function to check if the numbers in a list are in consecutive order
   return all(int(lst[i]) <= int(lst[i + 1]) for i in range(len(lst) - 1)) or all(int(lst[i]) >= int(lst[i + 1]) for i in range(len(lst) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be in consecutive order and that each number in the grid must be unique; ie It presumes we can replace any 'x' with any number from the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because replacing an 'x' with a number reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node, ie one action. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return sum(cell == 'x' for row in state for cell in row)


print(a_star())
