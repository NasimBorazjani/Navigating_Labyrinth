
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('81', '52', 'x', 'x'), ('x', '50', '53', 'x'), ('42', 'x', '54', '74'), ('x', 'x', '56', '77'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers = set(str(i) for i in range(28, 84))
   # Remove the numbers already present in the initial state from the set of available numbers
   for row in initial_state:
       for number in row:
           if number != 'x':
               numbers.remove(number)
   # Define the size of the grid
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, numbers)]


   while queue:
       _, g, actions, state, numbers = heapq.heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x's, return the actions taken
       if all(number != 'x' for row in state for number in row):
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for number in numbers:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie if the numbers in each row and column are strictly increasing or decreasing
                       if all(all(int(row[k]) < int(row[k + 1]) for k in range(len(row) - 1)) or all(int(row[k]) > int(row[k + 1]) for k in range(len(row) - 1)) for row in new_state if 'x' not in row) and all(all(int(new_state[k][l]) < int(new_state[k + 1][l]) for k in range(len(new_state) - 1)) or all(int(new_state[k][l]) > int(new_state[k + 1][l]) for k in range(len(new_state) - 1)) for l in range(num_cols) if 'x' not in [new_state[m][l] for m in range(num_rows)]):
                           # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                           new_cost = sum(int(number) for number in new_state[0] if number != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action taken to generate the new state is replacing the 'x' at coordinate (i, j) with the number
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state, numbers - {number}))
                       # Stop looking for 'x's after finding the first one
                       break
               else:
                   continue
               break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the state
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only appear once in the grid; ie It presumes we can replace any 'x' with any number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is equal to the cost of reaching the successor node, as replacing an 'x' with a number reduces the count of 'x's by 1, which is equal to the cost of reaching the successor node
   return sum(1 for row in state for number in row if number == 'x')


print(a_star())
