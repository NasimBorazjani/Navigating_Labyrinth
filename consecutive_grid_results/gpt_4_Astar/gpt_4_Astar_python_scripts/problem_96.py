
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 58, 'x', 77), ('x', 49, 63, 70), ('x', 'x', 'x', 69), (22, 43, 'x', 68))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to replace the 'x's in the grid
   available_numbers = set(range(22, 83))


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
       # The goal state is where all the 'x's in the grid have been replaced with unique integers from the given range, and the numbers in each row and column are strictly increasing or decreasing
       if all(all(cell != 'x' for cell in row) for row in state) and all(all(int(row[i]) < int(row[i + 1]) or int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1)) for row in state) and all(all(int(state[i][j]) < int(state[i + 1][j]) or int(state[i][j]) > int(state[i + 1][j]) for i in range(len(state) - 1)) for j in range(len(state[0]))):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
       # Iterate through the cells in the grid to find the next 'x'
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The next 'x' is at coordinate (i, j)
                   # The available numbers are all numbers in the range - numbers present in the current state
                   available_numbers = set(range(22, 83)) - set(int(cell) for row in state for cell in row if cell != 'x')
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner of the grid
                       new_cost = sum(int(cell) for cell in new_state[0]) + sum(int(row[-1]) for row in new_state) + sum(int(new_state[k][k]) for k in range(num_rows))


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
                   return None
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number in the grid must be unique; ie It presumes we can replace each 'x' with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the number used to replace the 'x' in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the number used to replace the 'x') + h(n’)
   h = 0
   # The available numbers are all numbers in the range - numbers present in the current state
   available_numbers = sorted(set(range(22, 83)) - set(int(cell) for row in state for cell in row if cell != 'x'))
   # Count the number of 'x's in the state
   num_x = sum(cell == 'x' for row in state for cell in row)
   # The heuristic is the sum of the minimum available number for each remaining 'x' in the grid
   h = sum(available_numbers[:num_x])
   return h


print(a_star())
