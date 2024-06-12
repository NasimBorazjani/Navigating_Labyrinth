
import heapq


def a_star():
   # Define the initial state of the magic square problem, with the grid and the sums of the rows, columns, and diagonal
   initial_grid = [['51', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
   row_sum = [124, 'x', 'x']
   col_sum = [107, 'x', 'x']
   diagonal_sum = 108
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[str(initial_grid)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_grid))


   while queue:
       _, g, actions, grid = heappop(queue)


       # If the grid satisfies all the constraints, return the actions taken
       if check_constraints(grid, row_sum, col_sum, diagonal_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the given range
       for i in range(26, 66):
           for row in range(num_rows):
               for col in range(num_cols):
                   if grid[row][col] == 'x':
                       new_grid = [list(row[:]) for row in grid]
                       new_grid[row][col] = str(i)
                       new_grid_str = str(new_grid)
                       new_cost = g + i
                      
                       if new_grid_str not in visited_costs or new_cost < visited_costs[new_grid_str]:
                           visited_costs[new_grid_str] = new_cost
                           heappush(queue, (new_cost + heuristic(new_grid, row_sum, col_sum, diagonal_sum), new_cost, actions + [(row, col, i)], new_grid))
   return None


def heuristic(grid, row_sum, col_sum, diagonal_sum):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
   # This heuristic relaxes the constraint that each number must be unique and presumes we can replace 'x' with any number in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences can only decrease as we replace 'x' with numbers
   # It is consistent because the estimated cost of the next node is higher if 'x' is replaced with a number that increases the sum of the row, column, or diagonal, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum amount that can be added to the sum is 1
   h = 0
   for i in range(len(grid)):
       # Calculate the sum of each row and compare it to the target sum
       row_total = sum(int(num) for num in grid[i] if num != 'x')
       h += abs(row_total - row_sum[i])
       # Calculate the sum of each column and compare it to the target sum
       col_total = sum(int(grid[j][i]) for j in range(len(grid)) if grid[j][i] != 'x')
       h += abs(col_total - col_sum[i])
   # Calculate the sum of the diagonal from the top right to the bottom left and compare it to the target sum
   diagonal_total = sum(int(grid[i][len(grid)-1-i]) for i in range(len(grid)) if grid[i][len(grid)-1-i] != 'x')
   h += abs(diagonal_total - diagonal_sum)
   return h


def check_constraints(grid, row_sum, col_sum, diagonal_sum):
   # Check if the grid satisfies all the constraints
   for i in range(len(grid)):
       # Check if the sum of each row matches the target sum
       row_total = sum(int(num) for num in grid[i] if num != 'x')
       if row_total != row_sum[i]:
           return False
       # Check if the sum of each column matches the target sum
       col_total = sum(int(grid[j][i]) for j in range(len(grid)) if grid[j][i] != 'x')
       if col_total != col_sum[i]
           return False
   # Check if the sum of the diagonal from the top right to the bottom left matches the target sum
   diagonal_total = sum(int(grid[i][len(grid)-1-i]) for i in range(len(grid)) if grid[i][len(grid)-1-i] != 'x')
   if diagonal_total != diagonal_sum:
       return False
   return True


print(a_star())
