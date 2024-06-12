
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 'x', 'x', 'x'), ('x', '37', 'x', '41'), ('48', 'x', 'x', 'x'), ('49', 'x', '46', '38'))
   row_sums = [None, 180, 176, None]
   col_sums = [None, 151, 189, None]
   diag_sum = 184
   num_rows = 4
   num_cols = 4
   available_numbers = set(range(35, 62)) - set(int(cell) for row in initial_state for cell in row if cell != 'x')


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if the state is the goal state
       if 'x' not in state:
           # Check if the sums of the rows, columns, and diagonal of the state equal the goal sums
           if all(sum(int(cell) for cell in row) == row_sums[i] or row_sums[i] is None for i, row in enumerate(state)) and all(sum(int(state[j][i]) for j in range(num_rows)) == col_sums[i] or col_sums[i] is None for i in range(num_cols)) and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows)) == diag_sum:
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
                           # The new number must be removed from the set of available numbers
                           new_available_numbers = available_numbers - {number}
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diag_sum, new_available_numbers), new_cost, actions + [(i, j, number)], new_state))
                   # After generating all possible actions from the current state, break the loop to avoid generating actions from the same state multiple times
                   break
           else:
               continue
           break
   return None


def heuristic(state, row_sums, col_sums, diag_sum, available_numbers):
   # An admissible and consistent heuristic for this problem is the sum of the minimum remaining numbers that need to be added to the grid to reach the goal sums of the rows, columns, and diagonal
   # The heuristic relaxes the constraints that each number in the grid must be unique and that the sum of the numbers in the grid must be minimized, and presumes we can add the smallest available number to the grid multiple times
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to the smallest available number, the decrease in the heuristic cost
   h = 0
   min_available_number = min(available_numbers)
   for i, row in enumerate(state):
       if row_sums[i] is not None:
           row_sum = sum(int(cell) for cell in row if cell != 'x')
           if row_sum < row_sums[i]:
               h += (row_sums[i] - row_sum) // min_available_number
   for i in range(len(state[0])):
       if col_sums[i] is not None:
           col_sum = sum(int(state[j][i]) for j in range(len(state)) if state[j][i] != 'x')
           if col_sum < col_sums[i]:
               h += (col_sums[i] - col_sum) // min_available_number
   diag_sum_current = sum(int(state[i][len(state) - i - 1]) for i in range(len(state)) if state[i][len(state) - i - 1] != 'x')
   if diag_sum_current < diag_sum:
       h += (diag_sum - diag_sum_current) // min_available_number
   return h


print(a_star())
