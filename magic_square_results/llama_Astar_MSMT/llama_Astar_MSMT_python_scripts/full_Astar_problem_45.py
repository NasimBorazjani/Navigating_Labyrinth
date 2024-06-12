
import heapq


def initialize():
   # Define the initial grid with 'x' and given numbers
   initial_grid = [['x', 50, 'x', 'x'],
                   [58, 'x', 'x', 'x'],
                   ['x', 49, 'x', 59],
                   [39, 41, 'x', 'x']]


   # Encoding other variables of the problem
   num_rows = 4
   num_cols = 4
   goal_col_sums = [None, 177, 196, None]
   goal_row_sums = [None, 183, 190, None]
   goal_diag_sum = 188


   visited_costs = {}
   visited_costs[tuple(row[:]) for row in initial_grid] = 0


   # The initial state is the initial grid
   queue = [(0, 0, [], initial_grid)]
  
   return initial_grid, num_rows, num_cols, goal_col_sums, goal_row_sums, goal_diag_sum, visited_costs, queue
  

def a_star():
  
   initial_grid, num_rows, num_cols, goal_col_sums, goal_row_sums, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, grid = heapq.heappop(queue)


       # Check if the current grid fulfills all the conditions: sums of columns, rows, and diagonal
       if all(sum(col) == goal_col_sums[i] or goal_col_sums[i] is None for i, col in enumerate(zip(*grid))) and all(sum(row) == goal_row_sums[i] or goal_row_sums[i] is None for i, row in enumerate(grid)) and sum(grid[i][i] for i in range(num_rows)) == goal_diag_sum:
           return actions


       # Generate all possible actions from the current grid, which involves replacing any of the 'x's with a number from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if grid[row_ind][col_ind] == 'x':
                   # Iterate through all possible numbers to replace the 'x'
                   for num in range(35, 62):
                       # Generate the new grid
                       new_grid = [list(row[:]) for row in grid]
                       new_grid[row_ind][col_ind] = num
                       # The cost so far is the number of replacements made
                       new_cost = g + 1


                       if tuple(tuple(row) for row in new_grid) not in visited_costs or new_cost < visited_costs[tuple(row[:]) for row in new_grid]:
                           visited_costs[tuple(tuple(row) for row in new_grid)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(grid, num_rows, num_cols, goal_col_sums, goal_row_sums, goal_diag_sum), new_cost, actions + [(row_ind, col_ind, num)], new_grid))
   return None


def heuristic(grid, num_rows, num_cols, goal_col_sums, goal_row_sums, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that the number of replacements made so far is taken into account when estimating the cost to reach the goal
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the absolute difference between the current and goal sum, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(num_rows):
       # Check if the current row sum is not None
       if goal_row_sums[i] is not None:
           h += abs(sum(grid[i]) - goal_row_sums[i])
       # Check if the current column sum is not None
       if goal_col_sums[i] is not None:
           h += abs(sum(grid[j][i] for j in range(num_rows)) - goal_col_sums[i])
   # Check if the current diagonal sum is not None
   if goal_diag_sum is not None:
       h += abs(sum(grid[i][i] for i in range(num_rows)) - goal_diag_sum)
   return h


print(a_star())
