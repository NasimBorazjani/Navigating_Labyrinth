
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 'x', 'x', 'x'), ('24', 'x', '27', '41'), ('22', '37', 'x', 'x'), ('29', 'x', 'x', '46'))
   goal_sums_rows = [None, 139, 178, None]
   goal_sums_cols = [None, 187, 186, None]
   goal_sum_diag = 160
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to fill the grid
   available_numbers = set(range(22, 69))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if the sums of the rows, columns, and diagonal of the grid in the current state equal the goal sums
       if 'x' not in [cell for row in state for cell in row]:
           # Convert any element of the grid equal to 'x' to a 0, to avoid the error "ValueError: invalid literal for int() with base 10: 'x'"
           sums_rows = [sum(int(cell) if cell != 'x' else 0 for cell in row) for row in state]
           sums_cols = [sum(int(row[j]) if row[j] != 'x' else 0 for row in state) for j in range(num_cols)]
           sum_diag = sum(int(state[i][num_cols - 1 - i]) if state[i][num_cols - 1 - i] != 'x' else 0 for i in range(num_rows))
           # If the sums of the rows, columns, and diagonal of the grid in the current state equal the goal sums, return the actions taken
           if all(sums_rows[i] == goal_sums_rows[i] or goal_sums_rows[i] is None for i in range(num_rows)) and all(sums_cols[i] == goal_sums_cols[i] or goal_sums_cols[i] is None for i in range(num_cols)) and sum_diag == goal_sum_diag:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in [cell for row in state for cell in row]:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
                       for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j] = str(number)
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                           new_cost = g + number


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_sums_rows, goal_sums_cols, goal_sum_diag)
                               # In the problem statement the grid is indexed starting from 0, thus must add 1 to the bucket_ind
                               heappush(queue, (new_cost + h, new_cost, actions + [(i, j, number)], new_state))
                       # After replacing the first 'x' found in the grid, break the loop to avoid replacing all 'x's in the grid in one action
                       break
               else:
                   continue
               break
   return None




def heuristic(state, goal_sums_rows, goal_sums_cols, goal_sum_diag):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sums of the rows, columns, and diagonal must equal the goal sums; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current sums and the goal sums
   num_rows = 4
   num_cols = 4
   # Convert any element of the grid equal to 'x' to a 0, to avoid the error "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
   sums_rows = [sum(int(cell) if cell != 'x' else 0 for cell in row) for row in state]
   sums_cols = [sum(int(row[j]) if row[j] != 'x' else 0 for row in state) for j in range(num_cols)]
   sum_diag = sum(int(state[i][num_cols - 1 - i]) if state[i][num_cols - 1 - i] != 'x' else 0 for i in range(num_rows))
   h = sum(abs(sums_rows[i] - goal_sums_rows[i]) if goal_sums_rows[i] is not None else 0 for i in range(num_rows)) + sum(abs(sums_cols[i] - goal_sums_cols[i]) if goal_sums_cols[i] is not None else 0 for i in range(num_cols)) + abs(sum_diag - goal_sum_diag)
   return h


print(a_star())
