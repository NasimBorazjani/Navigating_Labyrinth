
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('26', '38', '27', 'x'), ('x', 'x', 'x', '19'), ('x', '43', 'x', 'x'), ('42', 'x', '34', '20'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The sum of the numbers in the grid must be as low as possible, thus the numbers in the grid must be as low as possible, thus the numbers must be in the range 6 to 47
   available_numbers = set(range(6, 48))
   # The sum of the numbers in the specified rows, columns, and diagonal
   row_sums = [None, 94, 109, None]
   col_sums = [None, 128, 80, None]
   diagonal_sum = 99


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
       # The goal state is where all of the numbers in the grid are unique integers in the range 6 to 47, the sum of the numbers in the specified rows, columns, and diagonal equal the given amounts, and the sum of all of the numbers in the grid is as low as possible
       if all(cell != 'x' for row in state for cell in row) and all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') == diagonal_sum:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next x in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers present in the current state
           numbers_in_state = set(int(cell) for row in state for cell in row if cell != 'x')
           # Get the set of available numbers
           available_numbers = available_numbers - numbers_in_state
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = str(number)
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = g + number


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the current sum of the numbers in the specified rows, columns, and diagonal and the given amounts
   # This heuristic relaxes the constraints that the numbers in the grid must be unique and in the range 6 to 47, and that the sum of all of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the given sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of reaching a successor node is the number added to the grid, which is always greater than or equal to 6, the decrease in the difference between the current sum of the numbers in the specified rows, columns, and diagonal and the given amounts
   h = 0
   for row, row_sum in zip(state, row_sums):
       if row_sum is not None:
           h += abs(sum(int(cell) for cell in row if cell != 'x') - row_sum)
   for j, col_sum in enumerate(col_sums):
       if col_sum is not None:
           h += abs(sum(int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x') - col_sum)
   h += abs(sum(int(state[i][len(state) - 1 - i]) for i in range(len(state)) if state[i][len(state) - 1 - i] != 'x') - diagonal_sum)
   return h


print(a_star())
