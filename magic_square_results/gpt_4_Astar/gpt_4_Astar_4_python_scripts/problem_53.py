
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('x', 'x', '22', '23'), ('x', 'x', '15', '25'), ('31', 'x', 'x', 'x'), ('12', '36', 'x', '13'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The sum of the numbers in the grid must be as low as possible, thus the numbers in the grid must be as low as possible
   # The numbers in the grid must be unique and in the range 9 to 40, thus the available numbers are all numbers in the range 9 to 40 that are not already in the grid
   available_numbers = set(range(9, 41)) - set(int(cell) for row in initial_state for cell in row if cell != 'x')
   # The sums of the rows, columns, and diagonal are given in the problem statement
   row_sums = [None, 94, 111, None]
   col_sums = [None, 116, 78, None]
   diagonal_sum = 70


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in state:
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = str(number)
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of the numbers in the grid
               new_cost = g + number


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, row_sums, col_sums, diagonal_sum)
                   # In the problem statement the grid is indexed starting from 0, thus must add 1 to the x_row and x_col
                   heappush(queue, (new_cost + h, new_cost, actions + [(x_row, x_col, number)], new_state))
       # If the state does not have any remaining 'x's, check if it is a goal state
       else:
           # Check if the sums of the rows, columns, and diagonal in the current state equal the given sums
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') == diagonal_sum:
               return actions
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the given sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and in the range 9 to 40, and that the sum of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the given sums
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
   h += abs(sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') - diagonal_sum)
   return h


print(a_star())
