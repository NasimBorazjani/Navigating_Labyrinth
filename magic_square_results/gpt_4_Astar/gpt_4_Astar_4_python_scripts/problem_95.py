
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 'x', 'x', 'x'), ('x', '52', '20', 'x'), ('41', '13', 'x', 'x'), ('54', 'x', '16', '11'))
   row_sums = [None, 105, 115, None]
   col_sums = [None, 148, 109, None]
   diagonal_sum = 134
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to fill the grid
   available_numbers = set(range(11, 63)) - set(int(cell) for row in initial_state for cell in row if cell != 'x')


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if it is the goal state
       if 'x' not in state:
           # Check if the sums of the rows, columns, and diagonal of the state equal the goal sums
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') == diagonal_sum:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in state:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
                       for number in available_numbers:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j] = str(number)
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                           new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action taken to get to the new state must be added to the actions list
                               heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, number)], new_state))
                       break
               else:
                   continue
               break
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sums of the rows, columns, and diagonal must equal the goal sums; ie It presumes we can add any number to the grid to make the sums of the rows, columns, and diagonal equal the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current sums and the goal sums
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
