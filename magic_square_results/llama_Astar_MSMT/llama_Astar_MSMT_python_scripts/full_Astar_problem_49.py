
import heapq


def initialize():
   # Define the initial state of the grid, with numbers as integers and 'x' as None
   initial_grid = [[37, None, None, 56],
                   [52, None, None, None],
                   [None, 50, None, None],
                   [None, None, None, 46]]


   # Encoding other variables of the problem
   num_rows = 4
   num_cols = 4
   given_sums_cols = [None, 165, 155, None]
   given_sums_rows = [None, 169, 190, None]
   given_sum_diagonal = 201


   visited_costs = {}
   visited_costs[initial_grid] = 0


   # The information we must encode for each state includes the grid and the sum of all numbers in the grid
   # As the initial grid has not been modified yet, the sum of all numbers in the grid is the sum of the given numbers
   initial_state = (initial_grid, sum(sum(row) for row in initial_grid))
   # The priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the sum of all numbers in the grid (f) + the estimate remaining cost (h) to reach the goal
   queue = [(sum(sum(row) for row in initial_grid), 0, initial_grid)]
  
   return initial_state, num_rows, num_cols, given_sums_cols, given_sums_rows, given_sum_diagonal, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, given_sums_cols, given_sums_rows, given_sum_diagonal, visited_costs, queue = initialize()


   while queue:
       _, g, grid = heapq.heappop(queue)


       # If the grid satisfies all the given conditions, return the grid
       if all(sum(row) == given_sums_rows[i] or given_sums_rows[i] is None for i, row in enumerate(grid)) and all(sum(col) == given_sums_cols[j] or given_sums_cols[j] is None for j, col in enumerate(zip(*grid))) and sum(grid[i][i] for i in range(num_rows)) - (grid[1][1] if grid[1][1] is not None else 0) == given_sum_diagonal:
           return grid


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if grid[row_ind][col_ind] is None:
                   for num in range(34, 61):
                       new_grid = [list(row) for row in grid]
                       new_grid[row_ind][col_ind] = num
                       # The cost of the new state is the sum of all numbers in the new grid
                       new_cost = sum(sum(row) for row in new_grid)
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_grid not in visited_costs or new_cost < visited_costs[new_grid]:
                           visited_costs[new_grid] = new_cost
                           # The heuristic for this problem is the difference between the current sum of all numbers and the goal sum of all numbers, as the task is to minimize the sum of all numbers
                           heapq.heappush(queue, (new_cost + heuristic(grid, given_sums_rows, given_sums_cols, given_sum_diagonal), new_cost, new_grid))
   return None


def heuristic(grid, given_sums_rows, given_sums_cols, given_sum_diagonal):
   # The heuristic is the difference between the current sum of all numbers and the goal sum of all numbers
   goal_sum = sum(given_sum for given_sum in given_sums_rows + given_sums_cols + [given_sum_diagonal] if given_sum is not None)
   current_sum = sum(sum(row) for row in grid)
   return goal_sum - current_sum


print(a_star())
