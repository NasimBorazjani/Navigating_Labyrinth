
import heapq


def a_star():
   # Define the initial grid, the goal sums for rows, columns, and diagonal, and the range of unique integers to fill the grid
   initial_grid = [['x', '42', 'x', 'x'],
                   ['x', '38', 'x', 'x'],
                   ['x', '36', '46', 'x'],
                   ['49', '25', '24', 'x']]
   goal_row_sums = [None, 133, 150, None]
   goal_col_sums = [None, 141, 134, None]
   goal_diagonal_sum = 155
   unique_integers = list(range(24, 51))


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
                       new_grid_str = str(new_grid)


                       if new_grid_str not in visited_costs or new_cost < visited_costs[new_grid_str]:
                           visited_costs[new_grid_str] = new_cost
                           heappush(queue, (new_cost + heuristic(new_grid, goal_row_sums, goal_col_sums, goal_diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))
   return None


def check_constraints(grid, goal_row_sums, goal_col_sums, goal_diagonal_sum):
   # Check if the sums of rows, columns, and diagonal in the grid match the goal sums
   for i in range(4):
       if goal_row_sums[i] is not None and sum(int(x) for x in grid[i] if x != 'x') != goal_row_sums[i]:
           return False
       if goal_col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4) if grid[j][i] != 'x') != goal_col_sums[i]
           return False
   if sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x') != goal_diagonal_sum:
       return False
   if sum(int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x') != goal_diagonal_sum:
       return False
   return True


def heuristic(grid, goal_row_sums, goal_col_sums, goal_diagonal_sum):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of rows, columns, and diagonal in the grid and the goal sums
   # The heuristic relaxes the constraint that the sum of the numbers in the grid must match the goal sums, presuming we can adjust the numbers to match the goal sums
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if the sum of rows, columns, and diagonal in the grid is further from the goal sums, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the grid is the difference between the current sum and the goal sum
   h = 0
   for i in range(4):
       if goal_row_sums[i] is not None:
           h += abs(sum(int(x) for x in grid[i] if x != 'x') - goal_row_sums[i])
       if goal_col_sums[i] is not None:
           h += abs(sum(int(grid[j][i]) for j in range(4) if grid[j][i] != 'x') - goal_col_sums[i])
   h += abs(sum(int(grid[i][i]) for i in range(4) if grid[i][i] != 'x') - goal_diagonal_sum)
   h += abs(sum(int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x') - goal_diagonal_sum)
   return h


print(a_star())
