
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the rows, columns, and diagonal
   initial_state = (('42', '53', '43', '72'), ('x', '82', '54', 'x'), ('x', '62', '44', 'x'), ('x', 'x', 'x', 'x'))
   num_rows = 4
   num_cols = 4
   row_sums = [None, 253, 221, None]
   col_sums = [None, 277, 204, None]
   diagonal_sum = 252
   # The range of unique integers is from 37 to 83
   available_numbers = set(range(37, 84))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', and the sums of the rows, columns, and diagonal equal the given amounts, return the actions taken
       if 'x' not in state and all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == diagonal_sum:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in state:
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers present in the current state
           numbers_in_state = set(int(cell) for row in state for cell in row if cell != 'x')
           # Get the set of available numbers
           available_numbers = set(range(37, 84)) - numbers_in_state
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = str(number)
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = g + number


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, row_sums, col_sums, diagonal_sum)
                   # In the problem statement the grid is indexed starting from 0, thus must add 1 to the x_row and x_col
                   heappush(queue, (new_cost + h, new_cost, actions + [(x_row, x_col, number)], new_state))
   return None




def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the given sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sums of the rows, columns, and diagonal must equal the given amounts; ie It presumes we can add any number to the grid to reach the given sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current sums and the given sums
   h = 0
   num_rows = len(state)
   num_cols = len(state[0])
   for row, row_sum in zip(state, row_sums):
       if row_sum is not None:
           h += abs(sum(int(cell) for cell in row if cell != 'x') - row_sum)
   for j, col_sum in enumerate(col_sums):
       if col_sum is not None:
           h += abs(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') - col_sum)
   h += abs(sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') - diagonal_sum)
   return h


print(a_star())
