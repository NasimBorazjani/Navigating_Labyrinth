
import heapq


def initialize():
   # Define the initial state of the magic square, with the given numbers represented as integers and the unknown numbers as 'x'
   initial_state = [['47', 'x', 'x'],
                    ['x', 'x', 'x'],
                    ['x', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_1 = 93
   goal_row_1 = 135
   goal_diag = 106


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   # The information we must encode for each state includes the current state of the magic square, the sum of the numbers in the square, and the sum of the numbers in the column 1
   initial_state_info = (initial_state, 0, 0)
   # The initial state must be added to the path
   queue = [(0, 0, [initial_state_info], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_1, goal_row_1, goal_diag, visited_costs, initial_state_info, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_1, goal_row_1, goal_diag, visited_costs, initial_state_info, queue = initialize()


   while queue:
       _, g, path, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, total_sum, col_1_sum = state_info


       # If the current state satisfies all the conditions of the problem, return the path
       if total_sum == goal_col_1 + goal_row_1 + goal_diag and col_1_sum == goal_col_1:
           return path


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(26, 66):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                       new_cost = g + 1
                       new_total_sum = total_sum + num
                       new_col_1_sum = col_1_sum + num if col_ind == 0 else col_1_sum


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The coordinate of the new state must be added to the path
                           heapq.heappush(queue, (new_cost + heuristic(state_info, goal_col_1, goal_row_1, goal_diag), new_cost, path + [(new_state, new_total_sum, new_col_1_sum)], (new_state, new_total_sum, new_col_1_sum)))
   return None


def heuristic(state_info, goal_col_1, goal_row_1, goal_diag):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the sum of the numbers in the square, the sum of the numbers in column 1, and the sum of the numbers in the diagonal from the top right to the bottom left corner of the grid must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one cell to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is in the goal state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   state, total_sum, col_1_sum = state_info
   # Calculate the absolute difference between the current state and the goal state
   h += abs(total_sum - goal_col_1 - goal_row_1 - goal_diag)
   h += abs(col_1_sum - goal_col_1)
   return h


print(a_star())
