
import heapq


def a_star():
   # Define the initial grid, the goal sums for rows, columns, and diagonal, and the range of unique integers to fill in the grid
   initial_grid = [['x', '69', 'x', 'x'],
                   ['x', '62', 'x', 'x'],
                   ['x', '82', '40', 'x'],
                   ['x', '87', '78', '80']]
   goal_row_sums = [None, 214, 240, None]
   goal_col_sums = [None, 300, 191, None]
   goal_diagonal_sum = 249
   unique_integers = list(range(36, 93))


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


       # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers in the range provided
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
   # Check if the grid satisfies all the constraints
   # Check row sums
   for i in range(1, 3):
       if sum(int(grid[i][j]) for j in range(4) if grid[i][j] != 'x') != goal_row_sums[i]:
           return False
   # Check column sums
   for j in range(1, 3):
       if sum(int(grid[i][j]) for i in range(4) if grid[i][j] != 'x') != goal_col_sums[j]:
           return False
   # Check diagonal sum
   if int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) != goal_diagonal_sum:
       return False
   return True


def heuristic(grid, goal_row_sums, goal_col_sums, goal_diagonal_sum):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be minimized, as it only considers the sums of rows, columns, and diagonal
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences can only decrease as we replace 'x' with unique integers
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference in the heuristic is 1
   h = 0
   # Calculate the heuristic based on row sums
   for i in range(1, 3):
       h += abs(sum(int(grid[i][j]) for j in range(4) if grid[i][j] != 'x') - goal_row_sums[i])
   # Calculate the heuristic based on column sums
   for j in range(1, 3):
       h += abs(sum(int(grid[i][j]) for i in range(4) if grid[i][j] != 'x') - goal_col_sums[j])
   # Calculate the heuristic based on diagonal sum
   h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - goal_diagonal_sum)
   return h


print(a_star())
