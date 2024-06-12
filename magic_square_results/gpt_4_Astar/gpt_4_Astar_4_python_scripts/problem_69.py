
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('43', '65', 'x', 'x'), ('42', 'x', '59', 'x'), ('54', '45', 'x', 'x'), ('x', 'x', 'x', '35'))
   goal_sums_rows = [None, 219, 220, None]
   goal_sums_cols = [None, 205, 218, None]
   goal_sum_diag = 182
   num_rows = 4
   num_cols = 4
   # The range of unique integers that can be used to fill the grid
   numbers = set(str(i) for i in range(31, 68))
   # The numbers already present in the initial state of the grid
   initial_numbers = set(cell for row in initial_state for cell in row if cell != 'x')
   # The numbers available to fill the grid
   available_numbers = numbers - initial_numbers


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if the sums of the rows, columns, and diagonal of the state equal the goal sums
       if 'x' not in state:
           # Calculate the sums of the rows, columns, and diagonal of the state
           sums_rows = [sum(int(cell) for cell in row if cell != 'x') for row in state]
           sums_cols = [sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') for j in range(num_cols)]
           sum_diag = sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x')
           # If the sums of the rows, columns, and diagonal of the state equal the goal sums, return the actions taken
           if sums_rows == goal_sums_rows and sums_cols == goal_sums_cols and sum_diag == goal_sum_diag:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in state:
           # Find the coordinate of the next x in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Generate all possible actions from the current state
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = number
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, goal_sums_rows, goal_sums_cols, goal_sum_diag)
                   # In the problem statement the grid is indexed starting from 1, thus must add 1 to the x_row and x_col
                   heappush(queue, (new_cost + h, new_cost, actions + [(x_row, x_col, int(number))], new_state))
   return None




def heuristic(state, goal_sums_rows, goal_sums_cols, goal_sum_diag):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of the rows, columns, and diagonal of the current state and the goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the sums of the rows, columns, and diagonal of the current state and the goal sums
   h = 0
   sums_rows = [sum(int(cell) for cell in row if cell != 'x') for row in state]
   sums_cols = [sum(int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x') for j in range(len(state[0]))]
   sum_diag = sum(int(state[i][len(state[0]) - 1 - i]) for i in range(len(state)) if state[i][len(state[0]) - 1 - i] != 'x')
   for i in range(len(goal_sums_rows)):
       if goal_sums_rows[i] is not None:
           h += abs(sums_rows[i] - goal_sums_rows[i])
   for i in range(len(goal_sums_cols)):
       if goal_sums_cols[i] is not None:
           h += abs(sums_cols[i] - goal_sums_cols[i])
   h += abs(sum_diag - goal_sum_diag)
   return h


print(a_star())
