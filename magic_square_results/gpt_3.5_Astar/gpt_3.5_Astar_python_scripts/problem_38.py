
import heapq


def a_star():
   # Define the initial grid, the goal sums for rows, columns, and diagonal, and the range of unique integers to fill the grid
   initial_grid = [['x', '56', 'x', '40'],
                   ['x', 'x', '44', '60'],
                   ['x', '52', 'x', '45'],
                   ['x', 'x', '62', '47']]
   goal_row_sums = [None, 207, 218, None]
   goal_col_sums = [None, 227, 215, None]
   goal_diagonal_sum = 195
   unique_integers = list(range(40, 67))


   visited_costs = {}
   visited_costs[str(initial_grid)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_grid))


   while queue:
       _, g, actions, grid = heappop(queue)


       # If the grid satisfies all the constraints, return the actions taken
       if check_constraints(grid, goal_row_sums, goal_col_sums, goal_diagonal_sum):
           return actions


       # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers in the range
       for i in range(4):
           for j in range(4):
               if grid[i][j] == 'x':
                   for num in unique_integers:
                       new_grid = [row[:] for row in grid]
                       new_grid[i][j] = str(num)
                       new_cost = g + num
                       # Encode the new grid as a string to store in the visited_costs dictionary
                       new_grid_str = str(new_grid)


                       if new_grid_str not in visited_costs or new_cost < visited_costs[new_grid_str]:
                           visited_costs[new_grid_str] = new_cost
                           heappush(queue, (new_cost + heuristic(new_grid, goal_row_sums, goal_col_sums, goal_diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))
   return None


def check_constraints(grid, goal_row_sums, goal_col_sums, goal_diagonal_sum):
   # Check if the sums of rows, columns, and diagonal in the grid match the specified goals
   for i in range(4):
       row_sum = sum(int(num) for num in grid[i] if num != 'x')
       col_sum = sum(int(grid[j][i]) for j in range(4) if grid[j][i] != 'x')
       if goal_row_sums[i] is not None and row_sum != goal_row_sums[i]:
           return False
       if goal_col_sums[i] is not None and col_sum != goal_col_sums[i]
           return False
   diagonal_sum = sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x')
   if diagonal_sum != goal_diagonal_sum:
       return False
   return True


def heuristic(grid, goal_row_sums, goal_col_sums, goal_diagonal_sum):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be minimized, as it only considers the sum of the differences
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the goal
   # It is consistent because the estimated cost of the next node is higher if the sum of a row, column, or diagonal is further from the goal sum, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum decrease in the sum is 1
   h = 0
   for i in range(4):
       row_sum = sum(int(num) for num in grid[i] if num != 'x')
       col_sum = sum(int(grid[j][i]) for j in range(4) if grid[j][i] != 'x')
       if goal_row_sums[i] is not None:
           h += abs(row_sum - goal_row_sums[i])
       if goal_col_sums[i] is not None:
           h += abs(col_sum - goal_col_sums[i])
   diagonal_sum = sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x')
   h += abs(diagonal_sum - goal_diagonal_sum)
   return h


print(a_star())
