
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the row, column, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 'x', 'x'), ('x', 'x', 'x'), ('37', 'x', 'x'))
   goal_row_1_sum = 157
   goal_col_1_sum = 125
   goal_diag_sum = 138
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(35, 60))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if the sums of the specified row, column, and diagonal equal the goal sums
       if all(cell != 'x' for row in state for cell in row):
           row_1_sum = sum(int(cell) for cell in state[1])
           col_1_sum = sum(int(state[i][1]) for i in range(num_rows))
           diag_sum = sum(int(state[i][num_cols - i - 1]) for i in range(num_rows))
           if row_1_sum == goal_row_1_sum and col_1_sum == goal_col_1_sum and diag_sum == goal_diag_sum:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state)
                           # In the problem statement the grid is indexed starting from 0, thus must add 1 to the bucket_ind
                           heappush(queue, (new_cost + h, new_cost, actions + [(i, j, number)], new_state))
                   # After replacing the first 'x' in the grid, break the loop to avoid replacing all of the 'x's in the grid in one action
                   break
           else:
               continue
           break
   return None




def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the remaining 'x's in the grid
   # The heuristic relaxes the constraints that the sum of the specified row, column, and diagonal must equal the goal sums and that the sum of all of the numbers in the grid must be as low as possible; ie It presumes we can replace all of the remaining 'x's in the grid with 0s
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' in the grid with a number is the number itself, which is always greater than or equal to 0, the decrease in the number of 'x's in the grid
   return sum(cell == 'x' for row in state for cell in row)




print(a_star())
