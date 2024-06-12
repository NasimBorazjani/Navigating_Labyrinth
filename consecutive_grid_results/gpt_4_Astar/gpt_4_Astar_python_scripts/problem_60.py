
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '46', 'x'), ('x', '57', '59', '70'), ('56', 'x', '69', '73'), ('57', '75', 'x', '80'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers = set(range(36, 82))
   # Remove the numbers already present in the grid from the set of available numbers
   for row in initial_state:
       for number in row:
           if number != 'x':
               numbers.remove(int(number))
   # Define the size of the grid
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state, numbers))


   while queue:
       _, g, actions, state, numbers = heappop(queue)


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
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(is_increasing_or_decreasing(row) for row in new_state) and all(is_increasing_or_decreasing([new_state[i][j] for i in range(num_rows)]) for j in range(num_cols)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(number) for number in new_state[0] if number != 'x') + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows) if new_state[i][num_cols - 1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')
                           # Update the set of available numbers
                           new_numbers = numbers.copy()
                           new_numbers.remove(number)


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # In the problem statement the grid is indexed starting from 1, thus must add 1 to the i and j
                               heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state, new_numbers))
                       # Stop the search for the next 'x' as we have found one
                       break
               else:
                   continue
               break
   return None


def is_increasing_or_decreasing(numbers):
   # Check if the numbers in a list are strictly increasing or decreasing
   # Filter out the 'x's first
   numbers = [int(number) for number in numbers if number != 'x']
   return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)) or all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the state
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only appear once in the grid; ie It presumes we can replace any 'x' with any number in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is equal to the cost of reaching the successor node, ie one action, which is exactly the decrease in the count of 'x's
   return sum(1 for row in state for number in row if number == 'x')


print(a_star())
