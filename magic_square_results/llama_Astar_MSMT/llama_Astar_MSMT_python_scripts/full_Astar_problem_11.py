
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 48], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 127
   goal_row_sum = 144
   goal_diag_sum = 141


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the total sum of all the numbers in the grid
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, total_sum = state_info


       # If the current state satisfies all the given conditions, return the actions taken
       if check_conditions(state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum) and total_sum == 127 + 144 + 141:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in range(35, 60):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to satisfy the given conditions
                       new_cost = g + 1
                       new_total_sum = total_sum + num


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum) + abs(new_total_sum - (127 + 144 + 141)), new_cost, actions + [(row, col, num)], (new_state, new_total_sum)))
   return None


def check_conditions(state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum):
   # Check if the current state satisfies all the given conditions
   # Check the sum of each column, row, and diagonal
   for col in range(num_cols):
       if sum(state[row][col] for row in range(num_rows)) != goal_col_sum:
           return False
   for row in range(num_rows):
       if sum(state[row][col] for col in range(num_cols)) != goal_row_sum:
           return False
   if sum(state[i][i] for i in range(num_rows)) != goal_diag_sum:
       return False
   return True


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each column, row, and diagonal and the goal sum
   # This heuristic relaxes the constraint that each number can be in the final grid only once
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the largest or smallest in its column, row, or diagonal), which is equal to the cost of reaching the successor node
   h = 0
   for col in range(num_cols):
       h += abs(sum(state[row][col] for row in range(num_rows)) - goal_col_sum)
   for row in range(num_rows):
       h += abs(sum(state[row][col] for col in range(num_cols)) - goal_row_sum)
   h += abs(sum(state[i][i] for i in range(num_rows)) - goal_diag_sum)
   return h


print(a_star())
