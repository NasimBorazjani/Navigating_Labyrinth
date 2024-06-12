
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[21, None, None], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 72
   goal_row_sum = 95
   goal_diag_sum = 71


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the total sum of all the numbers in the magic square
   initial_state_info = (initial_state, 0)
   # The priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the sum of the cost so far and the estimate remaining cost to reach the goal
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # If the current state of the magic square satisfies all the conditions of the problem, return the actions taken
       if check_goal(state_info[0], num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state_info[0][row][col] is None:
                   for num in range(20, 40):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state_info[0]]
                       new_state[row][col] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the magic square
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row, col, num)], (new_state, state_info[1] + num)))
   return None


def check_goal(state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum):
   # Check if the current state of the magic square satisfies all the conditions of the problem
   # The conditions are that the sum of each column, row, and diagonal equals the given amounts
   col_sums = [sum(state[row][col] for row in range(num_rows)) for col in range(num_cols)]
   row_sums = [sum(state[row][col] for col in range(num_cols)) for row in range(num_rows)]
   diag_sum = sum(state[i][i] for i in range(num_rows)) - state[1][1]
   return all(col_sum == goal_col_sum for col_sum in col_sums) and all(row_sum == goal_row_sum for row_sum in row_sums) and diag_sum == goal_diag_sum


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of columns, rows, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that the sum of each column, row, and diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the difference between the goal sum and the current sum, which is equal to the cost of reaching the successor node
   h = 0
   num_rows = len(state)
   num_cols = len(state[0])
   col_sums = [sum(state[row][col] for row in range(num_rows)) for col in range(num_cols)]
   row_sums = [sum(state[row][col] for col in range(num_cols)) for row in range(num_rows)]
   diag_sum = sum(state[i][i] for i in range(num_rows)) - state[1][1]
   h += abs(col_sums[0] - goal_col_sum) + abs(row_sums[0] - goal_row_sum) + abs(diag_sum - goal_diag_sum)
   return h


print(a_star())
