
import heapq


def initialize():
   # Define the initial state of the grid, with the given numbers represented as integers and the unknown numbers represented as 'x'
   initial_state = [['35', 'x', '46'], ['x', 'x', 'x'], ['x', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 107
   goal_row_sum = 103
   goal_diag_sum = 124


   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # The information we must encode for each state includes the current state of the grid and the sum of the numbers in the grid
   initial_state_info = (initial_state, 0)
   # The initial state must be added to the path
   queue = [(0, 0, [initial_state_info], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, initial_state_info, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, initial_state_info, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state_grid, state_sum = state


       # If the sum of the numbers in the grid is equal to the goal sum, return the path
       if state_sum == goal_col_sum + goal_row_sum + goal_diag_sum:
           return path


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state_grid[row][col] == 'x':
                   for num in range(29, 49):
                       # Generate the new state
                       new_grid = [list(row[:]) for row in state_grid]
                       new_grid[row][col] = num
                       new_grid = tuple(tuple(row) for row in new_grid)
                       # The cost so far is the sum of the numbers in the grid
                       new_cost = g + num
                       # The sum of the numbers in the new state is the sum of the numbers in the current state plus the new number
                       new_sum = state_sum + num


                       if new_grid not in visited_costs or new_cost < visited_costs[new_grid]:
                           visited_costs[new_grid] = new_cost
                           # The new state must be added to the path
                           heapq.heappush(queue, (new_cost + heuristic(new_grid, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, path + [(new_grid, new_sum)], (new_grid, new_sum)))
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the numbers in the grid and the goal sum
   # This heuristic relaxes the constraint that the numbers in the grid must be unique and the sum of the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect number must be replaced with the correct number once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is incorrect), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   col_sum = 0
   row_sum = 0
   diag_sum = 0
   for row in range(len(state)):
       for col in range(len(state[row])):
           col_sum += state[row][col]
           row_sum += state[col][row]
           if row == col:
               diag_sum += state[row][col]
   h = abs(col_sum - goal_col_sum) + abs(row_sum - goal_row_sum) + abs(diag_sum - goal_diag_sum)
   return h


print(a_star())
