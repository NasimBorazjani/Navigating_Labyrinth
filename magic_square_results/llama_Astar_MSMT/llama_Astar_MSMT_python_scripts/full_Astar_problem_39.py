
import heapq


def initialize():
   # Define the grid, encoding the given numbers as integers and unknown numbers as 'x'
   grid = [['x', 35, 'x', 'x'],
           [43, 'x', 41, 30],
           ['x', 46, 33, 'x'],
           ['x', 49, 'x', 'x']]


   # Encoding other variables of the problem
   num_rows = 4
   num_cols = 4
   row_sums = [None, 174, 158, None]
   col_sums = [None, 158, 131, None]
   diagonal_sum = 156


   visited_costs = {}
   visited_costs[grid] = 0


   # The information we must encode for each state includes the current grid, and the sum of all the numbers in the grid
   initial_state = (grid, 0)
   queue = [(0, 0, [], initial_state)]
  
   return grid, num_rows, num_cols, row_sums, col_sums, diagonal_sum, visited_costs, initial_state, queue


def a_star():
  
   grid, num_rows, num_cols, row_sums, col_sums, diagonal_sum, visited_costs, initial_state, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the sum of all the numbers in the grid is 0, and the sums of the rows, columns, and diagonal are as given, return the actions taken
       if state[1] == 0:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[0][row][col] == 'x':
                   for num in range(24, 51):
                       # Generate the new state
                       new_grid = [list(row[:]) for row in state[0]]
                       new_grid[row][col] = num
                       # Update the sum of all the numbers in the grid
                       new_grid_sum = state[1] + num
                       # Generate the new state
                       new_state = (tuple(tuple(row) for row in new_grid), new_grid_sum)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the grid with the given constraints
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # Check if the new state satisfies the given constraints
                           if (all(sum(row) == col_sums[i] for i, row in enumerate(new_grid)) and
                               all(sum(col) == row_sums[i] for i, col in enumerate(zip(*new_grid))) and
                               sum(new_grid[i][i] for i in range(num_rows)) - 2 * new_grid[1][1] == diagonal_sum):
                               heapq.heappush(queue, (new_cost + heuristic(state[1], new_grid_sum), g + 1, actions + [(row, col, num)], new_state))
   return None


def heuristic(current_sum, goal_sum):
   # An admissible and consistent heuristic for this problem is the difference between the current sum of all the numbers in the grid and the goal sum of all the numbers in the grid
   # This heuristic relaxes the constraint that the sum of all the numbers in the grid must be as low as possible, as it only estimates the cost to reach the goal
   # It is admissible because it never overestimates the cost to reach the goal, as each increase in the sum of all the numbers in the grid must be accompanied by a decrease in the heuristic cost of the successor node
   # It is consistent because the estimated cost of the next node is higher if the sum of all the numbers in the grid increases, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum amount of increase in the sum of all the numbers in the grid is by adding one to each number, which is exactly the cost of reaching the successor node
   return goal_sum - current_sum


print(a_star())
