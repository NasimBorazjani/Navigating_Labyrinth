
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, None, 40, None], [None, 31, None, 43], [37, None, None, 32], [34, 29, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   row_sums = [None, 125, 164, None]
   col_sums = [None, 135, 160, None]
   goal_diagonal_sum = 146
   goal_total_sum = 121


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current configuration of the magic square and the total sum of the numbers in the grid
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, row_sums, col_sums, goal_diagonal_sum, goal_total_sum, visited_costs, initial_state_info, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, row_sums, col_sums, goal_diagonal_sum, goal_total_sum, visited_costs, initial_state_info, queue = initialize()
  
   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, total_sum = state_info


       # If the total sum of the numbers in the grid is equal to the goal total sum, return the actions taken
       if total_sum == goal_total_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # Check if the new state would be valid, ie the new total sum of the numbers in the grid would not exceed the goal total sum
                   for num in range(24, 51):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_total_sum = total_sum + num
                       if new_total_sum <= goal_total_sum:
                           # Check if the new state meets the constraints on the sums of the rows, columns, and diagonal
                           if check_constraints(new_state, row_sums, col_sums, goal_diagonal_sum):
                               new_state_info = (new_state, new_total_sum)
                               new_cost = g + 1


                               if new_state_info not in visited_costs or new_cost < visited_costs[new_state_info]:
                                   visited_costs[new_state_info] = new_cost
                                   heapq.heappush(queue, (new_cost + heuristic(state_info, goal_total_sum), g + 1, actions + [(row, col, num)], new_state_info))
   return None


def check_constraints(state, row_sums, col_sums, goal_diagonal_sum):
   # Check if the new state meets the constraints on the sums of the rows, columns, and diagonal
   for row in range(len(state)):
       row_sum = sum(state[row])
       if row_sums[row] is not None and row_sum != row_sums[row]:
           return False
   for col in range(len(state[0])):
       col_sum = sum(state[row][col] for row in range(len(state)))
       if col_sums[col] is not None and col_sum != col_sums[col]:
           return False
   diagonal_sum = sum(state[i][i] for i in range(len(state)))
   if diagonal_sum != goal_diagonal_sum:
       return False
   return True


def heuristic(state_info, goal_total_sum):
   # An admissible and consistent heuristic for this problem is the difference between the current total sum of the numbers in the grid and the goal total sum
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving a number from one position to another in the grid can only increase the heuristic cost of the successor node by a max of 1 (if the moved number is the largest number in the grid), which is equal to the cost of reaching the successor node
   _, total_sum = state_info
   return goal_total_sum - total_sum


print(a_star())
