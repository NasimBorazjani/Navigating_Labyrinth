
import heapq


def initialize():
   # Define the initial state of the grid, with '_' as the 'x'
   initial_state = [['_', 29, 41, '_'],
                    ['_', '_', 32, 43],
                    [23, 25, 29, 44],
                    [12, '_', 20, '_']]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0
  
   # The information we must encode for each state includes the grid and the sum of the top row, rightmost column, and diagonal
   initial_state_info = (initial_state, 70, 76, 66)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()
  
   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, top_row_sum, right_col_sum, diagonal_sum = state_info


       # If the sum of the top row, rightmost column, and diagonal in the current state is 0, return the actions taken
       if top_row_sum == 0 and right_col_sum == 0 and diagonal_sum == 0:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   for num in range(9, 49):
                       # Check if the replacement maintains the consecutive order in each row and column
                       if (row > 0 and state[row][col] > state[row - 1][col] and state[row][col] < state[row - 1][col] + 38) or (row < num_rows - 1 and state[row][col] < state[row + 1][col] and state[row][col] > state[row + 1][col] - 38) or (col > 0 and state[row][col] > state[row][col - 1] and state[row][col] < state[row][col - 1] + 38) or (col < num_cols - 1 and state[row][col] < state[row][col + 1] and state[row][col] > state[row][col + 1] - 38):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # Update the sums of the top row, rightmost column, and diagonal
                           new_top_row_sum = sum(new_state[0])
                           new_right_col_sum = sum(new_state[i][-1] for i in range(num_rows))
                           new_diagonal_sum = new_state[0][0] + new_state[1][1] + new_state[2][2] + new_state[3][3]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_info, (new_state, new_top_row_sum, new_right_col_sum, new_diagonal_sum)), new_cost, actions + [(row, col, num)], (new_state, new_top_row_sum, new_right_col_sum, new_diagonal_sum)))
   return None


def heuristic(state_info, new_state_info):
   # An admissible and consistent heuristic for this problem is the sum of the top row, rightmost column, and diagonal
   # This heuristic relaxes the constraint that the numbers must be unique and only appears once in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must be less than or equal to the current cost of reaching the goal
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 38 (the difference between the maximum and minimum possible number), which is equal to the cost of reaching the successor node
   return abs(sum(state_info[:3]) - sum(new_state_info[1:]))


print(a_star())
