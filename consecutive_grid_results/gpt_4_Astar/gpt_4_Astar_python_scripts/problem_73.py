
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('39', '40', '44', '62'), ('29', '33', '38', '61'), ('x', 'x', '35', '59'), ('x', 'x', 'x', 'x'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers_range = set(map(str, range(17, 68)))
   # Define the numbers that are already in the grid
   numbers_in_grid = set([num for row in initial_state for num in row if num != 'x'])
   # Define the numbers that are available to replace the 'x's
   available_numbers = numbers_range - numbers_in_grid
   # Define the size of the grid
   grid_size = 4


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
       if 'x' not in [num for row in state for num in row]:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for num in available_numbers:
           # Find the next 'x' in the grid
           for i in range(grid_size):
               for j in range(grid_size):
                   if state[i][j] == 'x':
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the main diagonal, as our objective is to minimize this sum
                       new_cost = g + int(num)
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, int(num))], new_state, available_numbers - set([num])))
                       break
               else:
                   continue
               break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced with at least the minimum available number
   # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' is the number that replaces it, which is always greater than or equal to the minimum available number, the decrease in the heuristic
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 'x':
               h += min(available_numbers)
   return h


print(a_star())
