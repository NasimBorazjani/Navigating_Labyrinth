
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('85', '73', '59', 'x'), ('x', 'x', '66', '70'), ('x', '59', 'x', 'x'), ('40', '41', '79', '82'))
   # Define the range of numbers that can be used to replace the 'x's
   num_range = set(map(str, range(31, 87)))
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
       # The goal state is where all 'x's have been replaced with unique integers from the given range, and the numbers in each row and column are in strictly increasing or decreasing order
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers (all numbers in the range - numbers present in the current state)
       # Get the available numbers
       available_nums = num_range - set(np.array(state).flatten())
       # Get the coordinate of the next 'x' in the grid
       x_coord = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       for num in available_nums:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_coord[0]][x_coord[1]] = num
           new_state = tuple(tuple(row) for row in new_state)
           # Check if the new state is valid, ie the numbers in each row and column are in strictly increasing or decreasing order
           if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(col) == list(col) or sorted(col, reverse=True) == list(col) for col in zip(*new_state)):
               # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner of the grid
               new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][-1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(x_coord[0], x_coord[1], int(num))], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be in strictly increasing or decreasing order, and that each number can only be used once; ie It presumes we can replace each 'x' with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic estimate
   return sum(int(min(num_range - set(np.array(state).flatten()))) for _ in range(np.array(state).flatten().tolist().count('x')))


print(a_star())
