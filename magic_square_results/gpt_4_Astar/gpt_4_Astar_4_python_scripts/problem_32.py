
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the row, column, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 'x', 'x'), ('x', 'x', 'x'), ('41', 'x', 'x'))
   goal_row_1_sum = 134
   goal_col_1_sum = 135
   goal_diag_sum = 122
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to fill the grid
   available_numbers = set(range(31, 76))


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
       # The goal state is where all of the numbers in the grid are unique integers in the given range, and the sum of the specified row, column, and diagonal equal the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == goal_row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == goal_col_1_sum and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows)) == goal_diag_sum:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers present in the current state
           numbers_in_state = set(cell for row in state for cell in row if cell != 'x')
           # Get the set of available numbers to replace the 'x' with
           available_numbers_for_x = available_numbers - numbers_in_state
           for number in available_numbers_for_x:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = str(number)
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = g + int(number)


               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_row_1_sum, goal_col_1_sum, goal_diag_sum), new_cost, actions + [(x_row, x_col, int(number))], new_state))
   return None


def heuristic(state, goal_row_1_sum, goal_col_1_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified row, column, and diagonal and their goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of all of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums
   h = 0
   # When calculating the sum of the row, column, or diagonal, first convert any element of the grid equal to 'x' to a 0, to avoid these error "ValueError: invalid literal for int() with base 10: 'x'" and "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
   h += abs(sum(int(cell) if cell != 'x' else 0 for cell in state[1]) - goal_row_1_sum)
   h += abs(sum(int(state[i][1]) if state[i][1] != 'x' else 0 for i in range(len(state))) - goal_col_1_sum)
   h += abs(sum(int(state[i][len(state) - 1 - i]) if state[i][len(state) - 1 - i] != 'x' else 0 for i in range(len(state))) - goal_diag_sum)
   return h


print(a_star())
