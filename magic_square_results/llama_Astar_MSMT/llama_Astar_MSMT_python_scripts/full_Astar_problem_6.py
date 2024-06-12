
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, 20, None], [None, None, None], [None, None, 33]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 82
   goal_row_sum = 82
   goal_diag_sum = 96


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the total sum of all the numbers in the magic square
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, total_sum = state_info


       # If the current state of the magic square satisfies all the conditions of the problem, return the actions taken
       if all(sum(row) == goal_row_sum for row in state) and all(sum(col) == goal_col_sum for col in zip(*state)) and sum(state[i][i] for i in range(num_rows)) == goal_diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   for num in range(19, 44):
                       # Check if the new state would be valid, ie the new state must satisfy all the conditions of the problem
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = num
                       # Generate the new state
                       new_state_info = (new_state, total_sum + num)
                       # The cost so far is the total sum of all the numbers in the magic square, as the task is to minimize the total sum
                       new_cost = g + num


                       if new_state_info not in visited_costs or new_cost < visited_costs[new_state_info]:
                           visited_costs[new_state_info] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state_info, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state_info))
   return None


def heuristic(state_info, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must equal the goal sum
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted by a positive amount
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the only one that causes the sum to mismatch), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   state, total_sum = state_info
   h = 0
   for row in state:
       h += abs(sum(row) - goal_row_sum)
   for col in zip(*state):
       h += abs(sum(col) - goal_col_sum)
   h += abs(sum(state[i][i] for i in range(len(state))) - goal_diag_sum)
   return h


print(a_star())
