
import heapq


def initialize():
   # Define the magic square grid, encoding the given numbers as integers and the missing numbers as 'x'
   grid = [['x', '51', '39', 'x'],
           ['x', 'x', '48', '37'],
           ['54', 'x', 'x', 'x'],
           ['x', 'x', 'x', '53']]


   # Encoding other variables given in the problem
   num_rows = 4
   num_cols = 4
   row_sums = [None, 212, 185, None]
   col_sums = [None, 180, 202, None]
   diagonal_sum = 193


   visited_costs = {}
   visited_costs[grid] = 0


   # The information we must encode for each state includes the grid, the sum of the numbers in the grid so far, and the total sum of the numbers in the grid
   initial_state = (grid, 0, 0)
   # The cost of the initial state is 0, as we have not replaced any 'x's with numbers yet
   queue = [(0, 0, [], initial_state)]
  
   return grid, num_rows, num_cols, row_sums, col_sums, diagonal_sum, visited_costs, initial_state, queue
  
def a_star():
  
   grid, num_rows, num_cols, row_sums, col_sums, diagonal_sum, visited_costs, initial_state, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in the current state
       grid, total_sum, _ = state


       # If the current grid satisfies all the given constraints, return the path taken to get to this grid
       if all(sum(row) == row_sums[i] for i, row in enumerate(grid)) and all(sum(col) == col_sums[i] for i, col in enumerate(zip(*grid))) and sum(grid[i][i] for i in range(num_rows)) == diagonal_sum:
           return path


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if grid[row_ind][col_ind] == 'x':
                   for num in range(35, 62):
                       # Check if the new number is valid, ie if replacing the 'x' with the number does not violate the constraints on the sums of the rows, columns, or diagonal
                       if all(sum(row) == row_sums[i] for i, row in enumerate(grid)) and all(sum(col) == col_sums[i] for i, col in enumerate(zip(*grid))) and sum(grid[i][i] for i in range(num_rows)) == diagonal_sum:
                           # Generate the new grid
                           new_grid = [list(row[:]) for row in grid]
                           new_grid[row_ind][col_ind] = num
                           # Calculate the new total sum of the numbers in the grid
                           new_total_sum = total_sum + num
                           # Generate the new state
                           new_state = (new_grid, new_total_sum)
                           # The cost of the new state is the total sum of the numbers in the grid
                           new_cost = new_total_sum


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action (replacing the 'x' with the number) must be added to the path
                               heapq.heappush(queue, (new_cost + heuristic(state, goal), new_cost, path + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the difference between the current total sum of the numbers in the grid and the goal total sum of the numbers in the grid
   # The heuristic relaxes the constraints that the sum of the numbers in the grid must be as low as possible, and that the numbers in the grid must be unique
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost is always less than or equal to the actual cost to reach the goal
   # The heuristic is consistent because moving a number from one position to another in the grid does not change the heuristic cost of the successor node
   _, total_sum = state
   _, goal_total_sum = goal
   return abs(total_sum - goal_total_sum)


print(a_star())
