
import heapq


def a_star():
   # Define the initial state of the grid, the range of numbers, and the sums of the rows, columns, and diagonal
   initial_state = (('70', 'x', '50', 'x'), ('x', '39', '46', 'x'), ('34', '60', 'x', '51'), ('x', 'x', 'x', '68'))
   num_range = set(range(30, 87))
   row_sums = [None, 183, 217, None]
   col_sums = [None, 260, 216, None]
   diag_sum = 214
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
       # The goal state is where all of the numbers in the grid are unique integers in the given range and the sums of the rows, columns, and diagonal equal the given amounts
       if all(cell != 'x' for row in state for cell in row) and all(sum(int(cell) for cell in row if cell != 'x') == row_sums[i] or row_sums[i] is None for i, row in enumerate(state)) and all(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') == col_sums[i] or col_sums[i] is None for i in range(num_cols)) and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for num in num_range - set(int(cell) for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + num


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diag_sum), new_cost, actions + [(i, j, num)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state, row_sums, col_sums, diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the current sums of the rows, columns, and diagonal and the goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sums of the rows, columns, and diagonal must equal the given amounts; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the difference between the current and goal sums
   h = 0
   num_rows = len(state)
   num_cols = len(state[0])
   for i in range(num_rows):
       if row_sums[i] is not None:
           h += abs(sum(int(cell) for cell in state[i] if cell != 'x') - row_sums[i])
   for i in range(num_cols):
       if col_sums[i] is not None:
           h += abs(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') - col_sums[i])
   h += abs(sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') - diag_sum)
   return h


print(a_star())
