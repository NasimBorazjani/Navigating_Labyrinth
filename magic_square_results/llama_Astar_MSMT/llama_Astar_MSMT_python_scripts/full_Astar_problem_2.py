
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, None, None], [30, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 82
   goal_row_sum = 87
   goal_diag_sum = 94


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the sum of all the numbers in the magic square
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, state_sum = state_info


       # If the current state of the magic square satisfies all the given conditions, return the actions taken
       if state[0][0] is not None and state[0][1] is not None and state[0][2] is not None and state[1][0] is not None and state[1][1] is not None and state[1][2] is not None and state[2][0] is not None and state[2][1] is not None and state[2][2] is not None and sum(state[0]) == goal_row_sum and sum(state[1]) == goal_row_sum and sum(state[2]) == goal_row_sum and state[0][0] + state[1][1] + state[2][2] == goal_diag_sum and state[0][2] + state[1][1] + state[2][0] == goal_diag_sum and sum(state[i][0] for i in range(num_rows)) == goal_col_sum and sum(state[i][1] for i in range(num_rows)) == goal_col_sum and sum(state[i][2] for i in range(num_rows)) == goal_col_sum and state_sum == 20 + 21 + 22 + 23 + 24 + 25 + 26 + 27 + 28 + 29 + 30 + 31 + 32 + 33 + 34 + 35 + 36 + 37 + 38 + 39:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in range(20, 40):
                       # Check if the new state would be valid, ie the number is unique in the row, column, and both diagonals
                       if num not in state[row] and num not in state[col] and num not in [state[i][i] for i in range(num_rows)] and num not in [state[i][num_rows - 1 - i] for i in range(num_rows)]:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of all the numbers in the magic square, as the task is to minimize the sum of all the numbers in the magic square
                           new_cost = g + num


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row, col, num)], (new_state, new_cost)))
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the largest difference), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += abs(sum(row) - goal_row_sum)
   for col in range(num_cols):
       h += abs(sum(state[i][col] for i in range(num_rows)) - goal_col_sum)
   h += abs(state[0][0] + state[1][1] + state[2][2] - goal_diag_sum)
   h += abs(state[0][2] + state[1][1] + state[2][0] - goal_diag_sum)
   return h


print(a_star())
