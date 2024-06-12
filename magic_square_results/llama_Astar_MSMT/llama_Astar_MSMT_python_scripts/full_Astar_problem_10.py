
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [None, None, 57]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 154
   goal_row_sum = 151
   goal_diag_sum = 133


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the sum of all numbers in the square
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, state_sum = state_info


       # If the current state satisfies all the conditions of the problem, return the actions taken
       if state_sum == goal_col_sum + goal_row_sum + goal_diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in range(35, 60):
                       # Check if the new state would be valid, ie the new state must satisfy the conditions of the problem
                       if state_sum + num <= goal_col_sum + goal_row_sum + goal_diag_sum:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to satisfy the conditions of the problem
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row, col, num)], (new_state, state_sum + num)))
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must equal the goal sum
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is part of the mismatched sum), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += abs(sum(row) - goal_col_sum)
   for col in range(num_cols):
       h += abs(sum(state[row][col] for row in range(num_rows)) - goal_row_sum)
   h += abs(sum(state[i][i] for i in range(num_rows)) - goal_diag_sum)
   return h


print(a_star())
