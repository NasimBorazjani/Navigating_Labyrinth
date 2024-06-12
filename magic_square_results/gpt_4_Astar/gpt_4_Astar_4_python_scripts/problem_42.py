
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 42, 'x', 'x'), ('x', 38, 'x', 'x'), ('x', 36, 46, 'x'), (49, 25, 24, 'x'))
   row_sums = [None, 133, 150, None]
   col_sums = [None, 141, 134, None]
   diagonal_sum = 155
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to fill the grid
   numbers = set(range(24, 51))
   # The numbers already present in the initial state
   initial_numbers = set(int(cell) for row in initial_state for cell in row if cell != 'x')
   # The numbers available to fill the grid
   available_numbers = numbers - initial_numbers


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if the state is the goal state
       if 'x' not in state:
           # Convert the state to a list to avoid "TypeError: 'tuple' object does not support item assignment"
           state = [list(row) for row in state]
           # Check if the sums of the rows, columns, and diagonal of the state equal the goal sums
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sums[i] or row_sums[i] is None for i, row in enumerate(state)) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sums[j] or col_sums[j] is None for j in range(num_cols)) and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == diagonal_sum:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       else:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Replace the 'x' with each of the available numbers to generate the new states
                       for number in available_numbers:
                           new_state = [list(row) for row in state]
                           new_state[i][j] = number
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                           new_cost = g + number


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action taken to generate the new state must be added to the actions list
                               # The action is a tuple of the row index, column index, and the number replaced with 'x' at that position
                               # The row and column indices are indexed from 0
                               heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, number)], new_state))
                       # After generating all of the new states by replacing the current 'x' with each of the available numbers, break the loop to avoid generating states by replacing multiple 'x's in the grid at once
                       break
               else:
                   continue
               break
   return None




def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums
   h = 0
   num_rows = len(state)
   num_cols = len(state[0])
   # Convert the state to a list to avoid "TypeError: 'tuple' object does not support item assignment"
   state = [list(row) for row in state]
   # Calculate the heuristic
   for i, row in enumerate(state):
       if row_sums[i] is not None:
           h += abs(sum(int(cell) for cell in row if cell != 'x') - row_sums[i])
   for j in range(num_cols):
       if col_sums[j] is not None:
           h += abs(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') - col_sums[j])
   h += abs(sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') - diagonal_sum)
   return h




print(a_star())