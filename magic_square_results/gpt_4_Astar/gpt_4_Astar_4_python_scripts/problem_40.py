
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the rows, columns, and diagonal
   initial_state = (('38', 'x', 'x', 'x'), ('x', 'x', 'x', 'x'), ('x', '39', '40', '27'), ('32', '46', 'x', '25'))
   unique_integers = set(str(i) for i in range(24, 51))
   row_sums = [None, 135, 130, None]
   col_sums = [None, 149, 178, None]
   diagonal_sum = 151
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all of the 'x's in the grid are replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row) and all(sum(int(cell) for cell in row if cell != 'x') == row_sum or row_sum is None for row, row_sum in zip(state, row_sums)) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum or col_sum is None for j, col_sum in enumerate(col_sums)) and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') == diagonal_sum:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of available unique integers
           available_numbers = unique_integers - set(cell for row in state for cell in row if cell != 'x')
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = number
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(x_row, x_col, int(number))], new_state))
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current and goal sums of the rows, columns, and diagonal
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be minimized, and presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of adding a number to the grid is the number itself, which is always greater than or equal to the decrease in the heuristic cost, as adding a number to the grid decreases the difference between the current and goal sums of the row, column, and diagonal that the number is in by at most the number itself. Thus h(n) can never be greater than c(n, n’)(equal to the number added to the grid) + h(n’)
   h = 0
   for i in range(len(state)):
       # Calculate the current sum of the row, column, and diagonal
       row_sum = sum(int(cell) for cell in state[i] if cell != 'x')
       col_sum = sum(int(state[j][i]) for j in range(len(state)) if state[j][i] != 'x')
       diagonal_sum_current = sum(int(state[j][len(state) - 1 - j]) for j in range(len(state)) if state[j][len(state) - 1 - j] != 'x')
       # Add the absolute difference between the current and goal sums to the heuristic cost
       if row_sums[i] is not None:
           h += abs(row_sum - row_sums[i])
       if col_sums[i] is not None:
           h += abs(col_sum - col_sums[i])
   h += abs(diagonal_sum_current - diagonal_sum)
   return h


print(a_star())
