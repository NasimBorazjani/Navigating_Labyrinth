
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the specified row, column, and diagonal, and the range of unique integers that can be used to replace 'x's
   initial_state = (('64', '78', 'x'), ('x', 'x', 'x'), ('x', 'x', 'x'))
   goal_sum_row_1 = 201
   goal_sum_col_1 = 234
   goal_sum_diag = 213
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(50, 85)) - set(int(cell) for row in initial_state for cell in row if cell != 'x')


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x's, check if the sums of the specified row, column, and diagonal equal the goal sums
       if all(cell != 'x' for row in state for cell in row):
           if sum(int(cell) for cell in state[1]) == goal_sum_row_1 and sum(int(state[i][1]) for i in range(num_rows)) == goal_sum_col_1 and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows)) == goal_sum_diag:
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
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The action is replacing the 'x' at coordinate (i, j) with the number
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum_row_1, goal_sum_col_1, goal_sum_diag), new_cost, actions + [(i, j, number)], new_state))
                   # After generating all possible actions from the current state, break the loop to avoid generating invalid actions
                   break
           else:
               continue
           break
   return None


def heuristic(state, goal_sum_row_1, goal_sum_col_1, goal_sum_diag):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified row, column, and diagonal and the goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sums of the specified row, column, and diagonal must equal the goal sums; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums
   h = 0
   h += abs(sum(int(cell) for cell in state[1]) - goal_sum_row_1)
   h += abs(sum(int(state[i][1]) for i in range(len(state))) - goal_sum_col_1)
   h += abs(sum(int(state[i][len(state) - 1 - i]) for i in range(len(state))) - goal_sum_diag)
   return h


print(a_star())
