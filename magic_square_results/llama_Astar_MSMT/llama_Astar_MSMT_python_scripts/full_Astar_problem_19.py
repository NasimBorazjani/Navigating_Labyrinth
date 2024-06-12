
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[64, 78, None], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sums = [234, 201, 213]
   goal_total_sum = 362


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the current total sum of the numbers in the grid
   initial_state_info = (initial_state, 0)
   # No actions performed to reach the initial state
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sums, goal_total_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sums, goal_total_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state of the magic square satisfies all the given conditions, return the actions taken
       if state[0] == goal_col_sums and sum(sum(row) for row in state[0]) == goal_total_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[0][row_ind][col_ind] is None:
                   for num in range(50, 85):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state[0]]
                       new_state[row_ind][col_ind] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the magic square
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sums, goal_total_sum), new_cost, actions + [(row_ind, col_ind, num)], (new_state, new_cost)))
   return None


def heuristic(state, goal_col_sums, goal_total_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current column sums and the goal column sums, and the absolute difference between the current total sum and the goal total sum
   # This heuristic relaxes the constraint that each number can be in the final grid only once
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's value matches the goal column sum but not in the current column sum), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           # Calculate the current column sum
           col_sum = sum(state[i][col_ind] for i in range(len(state)))
           # Add the absolute difference between the current column sum and the goal column sum to the estimate
           h += abs(col_sum - goal_col_sums[col_ind])
   # Add the absolute difference between the current total sum and the goal total sum to the estimate
   h += abs(sum(sum(row) for row in state) - goal_total_sum)
   return h


print(a_star())
