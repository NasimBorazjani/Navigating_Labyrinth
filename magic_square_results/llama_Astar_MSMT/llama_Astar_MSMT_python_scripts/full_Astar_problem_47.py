
import heapq


def initialize():
   # Define the magic square, encoding given numbers as integers and unknown numbers as 'x'
   magic_square = [['x', 46, 'x', 'x'],
                   [44, 'x', 'x', 53],
                   [39, 'x', 'x', 'x'],
                   ['x', 'x', 'x', 38]]
  
   # Encoding other variables of the problem
   num_rows = 4
   num_cols = 4
   goal_row_sums = [None, 198, 175, None]
   goal_col_sums = [None, 201, 190, None]
   goal_diagonal_sum = 193
   range_start = 34
   range_end = 60


   visited_costs = {}
   visited_costs[magic_square] = 0


   # The information we must encode for each state includes the current magic square, the current row and column indices, and the current unique integer value
   initial_state = (magic_square, 0, 0, range_start)
   # The cost of the initial state is 0, as we have not replaced any 'x' with a unique integer
   queue = [(0, 0, [magic_square], initial_state)]
  
   return magic_square, num_rows, num_cols, goal_row_sums, goal_col_sums, goal_diagonal_sum, range_start, range_end, visited_costs, initial_state, queue
  
def a_star():
  
   magic_square, num_rows, num_cols, goal_row_sums, goal_col_sums, goal_diagonal_sum, range_start, range_end, visited_costs, initial_state, queue = initialize()
  
   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in the current state
       current_square, row_ind, col_ind, value = state


       # If the current magic square satisfies all the constraints, return the path of unique integers replaced with 'x's
       if check_constraints(current_square, goal_row_sums, goal_col_sums, goal_diagonal_sum):
           return path


       # Generate all possible actions from the current state, which includes replacing the 'x' at the current row and column index with the next unique integer value
       if value <= range_end:
           # Generate the new magic square
           new_square = [list(row[:]) for row in current_square]
           new_square[row_ind][col_ind] = value
           # Generate the new state
           new_state = (new_square, row_ind, col_ind, value + 1)
           # The cost of the new state is the sum of the unique integers replaced with 'x's in the path plus the value of the next unique integer
           new_cost = g + value


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(new_square, goal_row_sums, goal_col_sums, goal_diagonal_sum), new_cost, path + [(row_ind, col_ind, value)], new_state))


       # Move to the next 'x' in the magic square
       row_ind, col_ind = next_x(current_square, row_ind, col_ind)
   return None


def check_constraints(square, goal_row_sums, goal_col_sums, goal_diagonal_sum):
   # Check if the magic square satisfies all the constraints
   row_sums = [sum(row) for row in square]
   col_sums = [sum(col) for col in zip(*square)]
   diagonal_sum = sum(square[i][i] for i in range(len(square))) - square[1][1]
   return row_sums == goal_row_sums and col_sums == goal_col_sums and diagonal_sum == goal_diagonal_sum


def next_x(square, row_ind, col_ind):
   # Find the next 'x' in the magic square
   for i in range(row_ind, len(square)):
       for j in range(col_ind, len(square[i])):
           if square[i][j] == 'x':
               return i, j
   return len(square), 0


def heuristic(square, goal_row_sums, goal_col_sums, goal_diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique, that we cannot replace 'x's with the same unique integer, and that the sums of rows, columns, and the diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by replacing the 'x' with a unique integer from the given range
   # It is consistent because moving from one state to another only reduces the heuristic cost of the successor node by a max of 2 (if we have to correct both the row and column sums), which is equal to the cost of reaching the successor node
   row_sums = [sum(row) for row in square]
   col_sums = [sum(col) for col in zip(*square)]
   diagonal_sum = sum(square[i][i] for i in range(len(square))) - square[1][1]
   return abs(row_sums[0] - goal_row_sums[0]) + abs(row_sums[1] - goal_row_sums[1]) + abs(col_sums[0] - goal_col_sums[0]) + abs(col_sums[1] - goal_col_sums[1]) + abs(diagonal_sum - goal_diagonal_sum)


print(a_star())
