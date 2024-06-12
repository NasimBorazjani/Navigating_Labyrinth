
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 'x', 'x', '67'), ('62', 'x', '32', '77'), ('66', 'x', '34', 'x'), ('x', 'x', '73', '35'))
   row_sums = [None, 220, 184, None]
   col_sums = [None, 239, 192, None]
   diagonal_sum = 199
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to fill the grid
   available_numbers = set(range(30, 87))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if it is the goal state
       if 'x' not in [cell for row in state for cell in row]:
           # The state is the goal state if the sum of the numbers in each row, column, and diagonal equals the given amounts
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and \
              all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and \
              sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') == diagonal_sum:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in [cell for row in state for cell in row]:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate all possible actions from the current state
                       for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j] = str(number)
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                           new_cost = g + number


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, number)], new_state))
                       # Only replace the first 'x' found in the grid
                       return None
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one state to an adjacent state is the number added to the grid, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums
   h = 0
   num_rows = len(state)
   num_cols = len(state[0])
   for i in range(num_rows):
       if row_sums[i] is not None:
           h += abs(sum(int(cell) for cell in state[i] if cell != 'x') - row_sums[i])
   for j in range(num_cols):
       if col_sums[j] is not None:
           h += abs(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') - col_sums[j])
   h += abs(sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') - diagonal_sum)
   return h


print(a_star())
