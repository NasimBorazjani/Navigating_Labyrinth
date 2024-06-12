
import heapq


def a_star():
   # Define the initial grid, the goal sums for each row, column, and diagonal, and the range of unique integers to fill in the grid
   initial_grid = [['x', 'x', 'x'],
                   ['x', 'x', 'x'],
                   [37, 'x', 'x']]
   goal_row_sum = 157
   goal_col_sum = 125
   goal_diag_sum = 138
   unique_integers = list(range(35, 60))


   visited_costs = {}
   visited_costs[str(initial_grid)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_grid))


   while queue:
       _, g, actions, grid = heappop(queue)


       # If the grid satisfies all the conditions, return the actions taken
       if is_goal_state(grid, goal_row_sum, goal_col_sum, goal_diag_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the grid
       for i in range(3):
           for j in range(3):
               if grid[i][j] == 'x':
                   for num in unique_integers:
                       new_grid = [row[:] for row in grid]
                       new_grid[i][j] = num
                       new_cost = g + num
                       # Encode the new grid as a string to store in the visited_costs dictionary
                       new_grid_str = str(new_grid)


                       if new_grid_str not in visited_costs or new_cost < visited_costs[new_grid_str]:
                           visited_costs[new_grid_str] = new_cost
                           heappush(queue, (new_cost + heuristic(new_grid, goal_row_sum, goal_col_sum, goal_diag_sum), new_cost, actions + [(i, j, num)], new_grid))
   return None


def is_goal_state(grid, goal_row_sum, goal_col_sum, goal_diag_sum):
   # Check if the sum of each row, column, and diagonal in the grid matches the goal sums
   row_sums = [sum(row) for row in grid]
   col_sums = [sum(col) for col in zip(*grid)]
   diag_sum1 = grid[0][2] + grid[1][1] + grid[2][0]
   diag_sum2 = grid[0][0] + grid[1][1] + grid[2][2]
   return all(row_sum == goal_row_sum for row_sum in row_sums) and all(col_sum == goal_col_sum for col_sum in col_sums) and diag_sum1 == goal_diag_sum and diag_sum2 == goal_diag_sum


def heuristic(grid, goal_row_sum, goal_col_sum, goal_diag_sum):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that each number must be unique and presumes we can fill the grid with any number in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences is always less than or equal to the actual cost to reach the goal
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with a different number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference in the heuristic is 1
   row_sums = [sum(row) for row in grid]
   col_sums = [sum(col) for col in zip(*grid)]
   diag_sum1 = grid[0][2] + grid[1][1] + grid[2][0]
   diag_sum2 = grid[0][0] + grid[1][1] + grid[2][2]
   h = sum(abs(row_sum - goal_row_sum) for row_sum in row_sums) + sum(abs(col_sum - goal_col_sum) for col_sum in col_sums)
   h += abs(diag_sum1 - goal_diag_sum) + abs(diag_sum2 - goal_diag_sum)
   return h


print(a_star())
