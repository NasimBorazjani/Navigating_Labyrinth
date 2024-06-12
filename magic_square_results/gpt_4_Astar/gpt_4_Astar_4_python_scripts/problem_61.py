
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the rows, columns, and diagonal
   initial_state = (('x', '31', 'x', 'x'), ('x', 'x', 'x', 'x'), ('x', 'x', '42', 'x'), ('x', '49', '30', '27'))
   num_rows = 4
   num_cols = 4
   row_sums = [None, 156, 156, None]
   col_sums = [None, 135, 149, None]
   diagonal_sum = 149
   # The range of unique integers is from 23 to 54
   available_numbers = set(range(23, 55))
   # Remove the numbers already present in the initial state from the set of available numbers
   for row in initial_state:
       for cell in row:
           if cell != 'x':
               available_numbers.remove(int(cell))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if the state is the goal state
       if all(cell != 'x' for row in state for cell in row):
           # The goal state is where the sum of the numbers in each row, column, and diagonal equals the given amounts
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') == diagonal_sum:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, row_sums, col_sums, diagonal_sum)
                           # In the problem statement the grid is indexed starting from 1, thus must add 1 to the row and column indices
                           heappush(queue, (new_cost + h, new_cost, actions + [(i+1, j+1, number)], new_state))
                   # After replacing an 'x' with a number, break the loop to avoid replacing multiple 'x's in one action
                   break
           else:
               continue
           break
   return None




def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current and goal sums of the rows, columns, and diagonal
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the sum of the absolute differences between the current and goal sums of the rows, columns, and diagonal
   h = 0
   for row, row_sum in zip(state, row_sums):
       if row_sum is not None:
           h += abs(sum(int(cell) for cell in row if cell != 'x') - row_sum)
   for j, col_sum in enumerate(col_sums):
       if col_sum is not None:
           h += abs(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') - col_sum)
   h += abs(sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') - diagonal_sum)
   return h




print(a_star())
