
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', 'x'), ('x', 61, 62), ('x', 'x', 63))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(40, 89))


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
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Check if the new state would be valid, ie the new number must maintain the consecutive order in its row and column
                       row = [int(x) for x in state[i] if x != 'x']
                       col = [int(state[x][j]) for x in range(num_rows) if state[x][j] != 'x']
                       if (all(x < number for x in row) or all(x > number for x in row)) and (all(x < number for x in col) or all(x > number for x in col)):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j] = number
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner
                           new_cost = sum([int(x) for x in new_state[0]]) + sum([int(new_state[x][num_cols - 1]) for x in range(num_rows)]) + sum([int(new_state[x][x]) for x in range(num_rows)])
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                               # Update the set of available numbers
                               available_numbers.remove(number)
                               break
                   break
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number times the number of remaining 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be in consecutive order and that each number in the grid must be unique; ie It presumes we can replace all of the 'x's with the minimum available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic estimate
   return len([x for x in np.array(state).flatten() if x == 'x']) * min(available_numbers)


print(a_star())
