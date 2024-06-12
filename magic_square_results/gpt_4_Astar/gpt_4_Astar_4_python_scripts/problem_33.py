
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
   initial_state = (('x', 'x', 'x'), ('x', 'x', 'x'), ('x', 'x', '55'))
   goal_sums = {'row1': 171, 'col1': 138, 'diag': 145}
   num_range = set(str(i) for i in range(31, 76))
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state has no 'x's, ie all of the numbers in the grid are known, and the sums of the specified rows, columns, and diagonal equal the goal sums, return the actions taken to reach this state
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == goal_sums['row1'] and sum(int(state[i][1]) for i in range(num_rows)) == goal_sums['col1'] and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows)) == goal_sums['diag']:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of available numbers
           available_nums = num_range - set(cell for row in state for cell in row if cell != 'x')
           for num in available_nums:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = num
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(x_row, x_col, int(num))], new_state))
   return None


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sums of the specified rows, columns, and diagonal must equal the goal sums; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums
   h = 0
   h += abs(sum(int(cell) for cell in state[1] if cell != 'x') - goal_sums['row1'])
   h += abs(sum(int(state[i][1]) for i in range(len(state)) if state[i][1] != 'x') - goal_sums['col1'])
   h += abs(sum(int(state[i][len(state) - i - 1]) for i in range(len(state)) if state[i][len(state) - i - 1] != 'x') - goal_sums['diag'])
   return h


print(a_star())
