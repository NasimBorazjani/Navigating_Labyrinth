
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the specified rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 'x', 'x'), ('x', 'x', 'x'), ('x', 'x', 19))
   goal_sums = {'row_1': 82, 'col_1': 71, 'diag': 70}
   num_range = set(range(12, 47))
   num_rows = 3
   num_cols = 3


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
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for row in state for cell in row if cell != 'x') == sum(goal_sums.values()):
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of numbers that are currently in the grid
           current_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
           # Get the set of numbers that are available to replace the 'x's
           available_numbers = num_range - current_numbers
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = number
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and their goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of all of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums
   h = 0
   # Calculate the current sum of row 1
   row_1_sum = sum(int(cell) for cell in state[1] if cell != 'x')
   h += abs(row_1_sum - goal_sums['row_1'])
   # Calculate the current sum of column 1
   col_1_sum = sum(int(state[i][1]) for i in range(len(state)) if state[i][1] != 'x')
   h += abs(col_1_sum - goal_sums['col_1'])
   # Calculate the current sum of the diagonal from the top right to the bottom left corner of the grid
   diag_sum = sum(int(state[i][2 - i]) for i in range(len(state)) if state[i][2 - i] != 'x')
   h += abs(diag_sum - goal_sums['diag'])
   return h


print(a_star())
