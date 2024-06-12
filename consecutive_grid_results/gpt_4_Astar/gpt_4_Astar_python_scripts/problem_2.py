
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('10', '15', '39'), ('x', '27', '29'), ('x', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace the 'x's in the grid
   numbers = set(str(i) for i in range(8, 42))


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
       # The goal state is where all the 'x's have been replaced with unique integers from the given range, maintaining the consecutive order in each row and column
       if all(all(cell != 'x' for cell in row) for row in state):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # The next 'x' to replace is the first 'x' in the grid when read row by row from left to right, top to bottom
       # The available unique integers are all the numbers in the range that are not already in the grid
       available_numbers = numbers - set(cell for row in state for cell in row if cell != 'x')
       for number in available_numbers:
           # Find the coordinate of the next 'x' to replace
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = number
           # Check if the new state maintains the consecutive order in each row and column
           if all(all(int(new_state[i][j]) < int(new_state[i][j + 1]) for j in range(num_cols - 1)) or all(int(new_state[i][j]) > int(new_state[i][j + 1]) for j in range(num_cols - 1)) for i in range(num_rows)) and all(all(int(new_state[i][j]) < int(new_state[i + 1][j]) for i in range(num_rows - 1)) or all(int(new_state[i][j]) > int(new_state[i + 1][j]) for i in range(num_rows - 1)) for j in range(num_cols)):
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
               new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_row, x_col, int(number))], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available unique integers that can be used to replace the remaining 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only appear once in the grid; ie It presumes we can replace the 'x's with any of the available unique integers in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available unique integer, the decrease in the heuristic estimate
   h = 0
   available_numbers = sorted([int(cell) for cell in numbers - set(cell for row in state for cell in row if cell != 'x')])
   num_xs = sum(cell == 'x' for row in state for cell in row)
   for i in range(num_xs):
       h += available_numbers[i]
   return h


print(a_star())
