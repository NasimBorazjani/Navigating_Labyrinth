
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('12', 'x', 'x'), ('18', 'x', '52'), ('22', 'x', '31'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of numbers that can be used to replace the 'x's
   numbers = set(str(i) for i in range(12, 61))


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
       # The goal state is where all the 'x's have been replaced with unique integers from the given range, and the numbers in each row and column are in strictly increasing or decreasing order
       if all(all(cell != 'x' for cell in row) for row in state) and all(all(int(row[i]) < int(row[i + 1]) or int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1)) for row in state) and all(all(int(state[i][j]) < int(state[i + 1][j]) or int(state[i][j]) > int(state[i + 1][j]) for i in range(len(state) - 1)) for j in range(len(state[0]))):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # The next 'x' to replace is the first 'x' in the grid when reading from left to right, top to bottom
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The available numbers are all the numbers in the range that are not already in the grid
                   available_numbers = numbers - set(cell for row in state for cell in row if cell != 'x')
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid
                       new_cost = sum(int(cell) for cell in new_state[0] if cell != 'x') + sum(int(new_state[k][num_cols - 1]) for k in range(num_rows) if new_state[k][num_cols - 1] != 'x') + sum(int(new_state[l][l]) for l in range(num_rows) if new_state[l][l] != 'x')


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, int(number))], new_state))
                   # Once we have generated all possible states from replacing the current 'x', break the loop to avoid generating states from replacing other 'x's in the same iteration
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers replacing the 'x's must be unique and in the given range, and that the numbers in each row and column must be in strictly increasing or decreasing order; ie It presumes we can replace all the 'x's with any number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner of the grid, which is always greater than or equal to 1, the decrease in the count of 'x's
   return sum(cell == 'x' for row in state for cell in row)


print(a_star())
