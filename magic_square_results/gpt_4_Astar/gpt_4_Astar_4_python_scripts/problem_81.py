
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('61', 'x', '50', 'x'), ('x', 'x', 'x', 'x'), ('68', '40', '57', 'x'), ('x', '42', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   column_sums = [None, 188, 234, None]
   row_sums = [None, 247, 238, None]
   diagonal_sum = 215
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(range(35, 77))
   # Remove the numbers already present in the initial state from the set of available numbers
   for row in initial_state:
       for cell in row:
           if cell != 'x':
               available_numbers.remove(int(cell))


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
       # The goal state is where all 'x's in the grid have been replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row) and all(sum(int(cell) for cell in row if cell != 'x') == row_sums[i] if row_sums[i] is not None else True for i, row in enumerate(state)) and all(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') == column_sums[i] if column_sums[i] is not None else True for i in range(num_cols)) and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == diagonal_sum:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Generate the set of numbers that can be used to replace the 'x' at the current coordinate
           current_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
           possible_numbers = available_numbers - current_numbers
           for number in possible_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = str(number)
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, column_sums, diagonal_sum), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state, row_sums, column_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and their goal sums
   # The heuristic relaxes the constraints that each number in the grid must be unique and that the sum of all of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one state to an adjacent state is the number added to the grid, which is always greater than or equal to 1, the decrease in the absolute difference between the current sum and the goal sum
   h = 0
   num_rows = len(state)
   num_cols = len(state[0])
   for i, row in enumerate(state):
       if row_sums[i] is not None:
           h += abs(sum(int(cell) for cell in row if cell != 'x') - row_sums[i])
   for i in range(num_cols):
       if column_sums[i] is not None:
           h += abs(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') - column_sums[i])
   h += abs(sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') - diagonal_sum)
   return h


print(a_star())
