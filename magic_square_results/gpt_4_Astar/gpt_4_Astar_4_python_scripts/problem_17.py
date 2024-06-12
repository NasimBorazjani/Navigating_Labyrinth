
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the specified rows, columns, and diagonal, and the range of unique integers that can be used to replace 'x's
   initial_state = (('x', 52, 'x'), ('x', 'x', 'x'), ('x', 'x', 'x'))
   goal_sum_col_1 = 166
   goal_sum_row_1 = 192
   goal_sum_diag = 184
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's
   available_numbers = set(range(48, 78))


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
       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in state:
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers present in the current state
           numbers_in_state = {int(cell) for row in state for cell in row if cell != 'x'}
           # Get the set of available numbers to replace the next 'x' with
           available_numbers = available_numbers - numbers_in_state
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = number
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = g + number
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum_col_1, goal_sum_row_1, goal_sum_diag), new_cost, actions + [(x_row, x_col, number)], new_state))
       else:
           # If the current state is a goal state, return the actions taken to reach this state
           return actions
   return None


def heuristic(state, goal_sum_col_1, goal_sum_row_1, goal_sum_diag):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums and the goal sums of the specified rows, columns, and diagonal
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of all of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current sums and the goal sums
   h = 0
   # When calculating the sum of rows, columns, or diagonal of an intermediate state, first convert any element of the grid equal to 'x' to a 0, to avoid these error "ValueError: invalid literal for int() with base 10: 'x'" and "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
   h += abs(sum(int(cell) if cell != 'x' else 0 for cell in state[1]) - goal_sum_row_1)
   h += abs(sum(int(row[1]) if row[1] != 'x' else 0 for row in state) - goal_sum_col_1)
   h += abs(sum(int(state[i][2 - i]) if state[i][2 - i] != 'x' else 0 for i in range(3)) - goal_sum_diag)
   return h


print(a_star())
