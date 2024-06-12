
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '62'), ('x', 'x', 'x'), ('x', 'x', '56'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   col_1_sum = 212
   row_1_sum = 193
   diagonal_sum = 217
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(range(50, 85))


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
       # The goal state is where all the 'x's in the grid are replaced with unique integers such that the sum of column 1, row 1, and the diagonal from the top right to the bottom left corner of the grid equal the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == col_1_sum and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows)) == diagonal_sum:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers that are currently in the grid
           numbers_in_grid = set(int(cell) for row in state for cell in row if cell != 'x')
           # The set of numbers that can be used to replace the next 'x' in the grid is the set of all numbers in the range minus the set of numbers that are already in the grid
           numbers_to_replace_x = available_numbers - numbers_in_grid
           for number in numbers_to_replace_x:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = str(number)
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of all the numbers in the grid, as the task is to minimize the sum of all the numbers in the grid
               new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The action is a tuple of the coordinate of the 'x' replaced and the number used to replace it
                   # In the problem statement the grid is indexed starting from 1, thus must add 1 to the row and column indices
                   heapq.heappush(queue, (new_cost + heuristic(new_state, row_1_sum, col_1_sum, diagonal_sum), new_cost, actions + [(x_row+1, x_col+1, number)], new_state))
   return None


def heuristic(state, row_1_sum, col_1_sum, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of column 1, row 1, and the diagonal from the top right to the bottom left corner of the grid and their goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of all the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' in the grid with a number is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums of column 1, row 1, and the diagonal
   h = 0
   h += abs(sum(int(cell) for cell in state[1]) - row_1_sum)
   h += abs(sum(int(state[i][1]) for i in range(len(state))) - col_1_sum)
   h += abs(sum(int(state[i][len(state) - 1 - i]) for i in range(len(state))) - diagonal_sum)
   return h


print(a_star())
