
import heapq


def initialize():
   # Define the initial state of the grid, as a 2d list of integers and 'x'
   initial_grid = [['x', 'x', 'x'],
                   ['x', 'x', 'x'],
                   ['x', '32', 'x']]


   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 150
   goal_row_sum = 135
   goal_diag_sum = 119


   visited_costs = {}
   visited_costs[str(initial_grid)] = 0


   queue = [(0, 0, [], initial_grid)]
  
   return initial_grid, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_grid, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, grid = heapq.heappop(queue)


       # Check if the current grid satisfies the conditions of the problem
       if sum(grid[0]) == goal_row_sum and sum(grid[1]) == goal_row_sum and sum(grid[2]) == goal_row_sum and sum(grid[i][i] for i in range(num_rows)) == goal_diag_sum and sum(grid[i][num_rows - i - 1] for i in range(num_rows)) == goal_diag_sum:
           return actions


       # Generate all possible actions from the current grid, which includes replacing an 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if grid[row][col] == 'x':
                   for num in range(26, 66):
                       # Generate the new grid
                       new_grid = [list(row[:]) for row in grid]
                       new_grid[row][col] = num
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the grid
                       new_cost = g + 1


                       if new_grid not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                           visited_costs[str(new_grid)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_grid, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row, col, num)], new_grid))
   return None


def heuristic(grid, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must equal the goal sum
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the difference between the goal sum and the current sum, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(grid)):
       h += abs(sum(grid[i]) - goal_row_sum)
       h += abs(sum(grid[j][i] for j in range(len(grid))) - goal_col_sum)
   h += abs(sum(grid[i][i] for i in range(len(grid))) - goal_diag_sum)
   h += abs(sum(grid[i][len(grid) - i - 1] for i in range(len(grid))) - goal_diag_sum)
   return h


print(a_star())
