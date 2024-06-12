
import heapq


def a_star():
   # Define the initial state of the magic square problem, with the grid and the sums of the rows, columns, and diagonal
   initial_grid = [[41, 'x', 'x'], [34, 'x', 'x'], ['x', 'x', 'x']]
   row_sum = [133, 'x', 'x']
   col_sum = [129, 'x', 'x']
   diagonal_sum = 136
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[str(initial_grid)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_grid))


   while queue:
       _, g, actions, grid = heappop(queue)


       # If the grid satisfies the conditions, return the actions taken
       if check_sums(grid, row_sum, col_sum, diagonal_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the given range
       for i in range(num_rows):
           for j in range(num_cols):
               if grid[i][j] == 'x':
                   for num in range(28, 58):
                       new_grid = [row[:] for row in grid]
                       new_grid[i][j] = num
                       new_cost = g + num
                       if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                           visited_costs[str(new_grid)] = new_cost
                           heappush(queue, (new_cost + heuristic(new_grid, row_sum, col_sum, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))
   return None


def check_sums(grid, row_sum, col_sum, diagonal_sum):
   # Check if the sums of rows, columns, and diagonal match the specified values
   for i in range(len(grid)):
       if row_sum[i] != 'x' and sum(grid[i]) != row_sum[i]:
           return False
       col_total = sum(row[i] for row in grid)
       if col_sum[i] != 'x' and col_total != col_sum[i]:
           return False
   diagonal_total = sum(grid[i][i] for i in range(len(grid)))
   if diagonal_total != diagonal_sum:
       return False
   return True


def heuristic(grid, row_sum, col_sum, diagonal_sum):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of rows, columns, and diagonal and the target sums
   # This heuristic relaxes the constraint that each number can only be used once in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be made up by replacing 'x' with a number
   # It's consistent because the estimated cost of the next node is higher if 'x' is replaced with a number, or equal or less by at most the difference between the current and target sum, which is exactly the cost of reaching the successor node
   h = 0
   for i in range(len(grid)):
       row_diff = row_sum[i] - sum(grid[i]) if row_sum[i] != 'x' else 0
       col_total = sum(row[i] for row in grid)
       col_diff = col_sum[i] - col_total if col_sum[i] != 'x' else 0
       h += abs(row_diff) + abs(col_diff)
   diagonal_total = sum(grid[i][i] for i in range(len(grid)))
   diagonal_diff = diagonal_sum - diagonal_total
   h += abs(diagonal_diff)
   return h


print(a_star())
