
import heapq


def initialize():
   # Define the initial state of the grid, with the given numbers represented as integers and the unknown numbers represented as 'x'
   initial_state = [['52', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 130
   goal_row_sum = 144
   goal_diag_sum = 123


   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # The information we must encode for each state includes the current state of the grid and the total sum of all the numbers in the grid
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, initial_state_info, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, initial_state_info, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, total_sum = state_info


       # If the current state satisfies all the given conditions, return the actions taken
       if sum(map(sum, state)) == total_sum and sum(state[0]) == goal_col_sum and sum(state[1]) == goal_row_sum and state[0][0] + state[1][1] + state[2][2] == goal_diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in range(35, 60):
                       # Check if the new state would be valid, ie the new number does not already exist in the grid
                       if str(num) not in map(str, state):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to satisfy the given conditions
                           new_cost = g + 1
                           new_total_sum = total_sum + num


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_info, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row, col, num)], (new_state, new_total_sum)))
   return None


def heuristic(state_info, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the specified rows, columns, and diagonal and the given amounts
   # This heuristic relaxes the constraint that the sum of all the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a positive amount
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is the only one that causes the sum to be incorrect), which is equal to the cost of reaching the successor node
   state, total_sum = state_info
   h = abs(sum(state[0]) - goal_col_sum) + abs(sum(state[1]) - goal_row_sum) + abs(state[0][0] + state[1][1] + state[2][2] - goal_diag_sum)
   return h


print(a_star())
