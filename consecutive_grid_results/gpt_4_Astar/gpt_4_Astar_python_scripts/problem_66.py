
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 37, 'x', 'x'), ('x', 35, 40, 'x'), (15, 'x', 'x', 44), (11, 20, 36, 'x'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(range(9, 55))
   # Define the size of the grid
   num_rows = 4
   num_cols = 4


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


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers (all numbers in the range - numbers present in the current state) in the range
       # Get the available numbers
       available_numbers = num_range - set(np.array(state).flatten())
       # Get the coordinate of the next 'x' in the grid
       x_coord = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       for number in available_numbers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_coord[0]][x_coord[1]] = number
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
           # Filter out the 'x's before calculating the sum
           new_cost = sum(int(i) for i in new_state[0] if i != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')


           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_coord[0], x_coord[1], number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number (all numbers in the range - numbers present in the current state) times the number of remaining 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that the numbers replacing the 'x's must be unique; ie It presumes we can replace all of the 'x's with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   available_numbers = set(range(9, 55)) - set(np.array(state).flatten())
   min_available_number = min(available_numbers)
   num_xs = np.count_nonzero(np.array(state) == 'x')
   return min_available_number * num_xs


print(a_star())
