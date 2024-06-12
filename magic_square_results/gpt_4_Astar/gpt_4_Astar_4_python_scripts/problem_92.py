
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the rows, columns, and diagonal
   initial_state = (('53', '57', 'x', 'x'), ('77', '78', 'x', '56'), ('51', '62', '88', 'x'), ('x', 'x', 'x', 'x'))
   unique_integers = set(str(i) for i in range(41, 93))
   row_sums = [None, 266, 261, None]
   col_sums = [None, 244, 295, None]
   diagonal_sum = 265
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
       # The goal state is where all of the 'x's in the grid have been replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row):
           # Check if the sums of the rows, columns, and diagonal in the current state match the given sums
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sums[i] or row_sums[i] is None for i, row in enumerate(state)) and all(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') == col_sums[i] or col_sums[i] is None for i in range(num_cols)) and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == diagonal_sum:
               return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of the available unique integers
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Generate the new state by replacing the 'x' with any of the available unique integers
                   for num in unique_integers - set(cell for row in state for cell in row if cell != 'x'):
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(num)


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, int(num))], new_state))
                   # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
                   return None
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the given sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of all of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the given sums
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current sums and the given sums
   h = 0
   num_rows = len(state)
   num_cols = len(state[0])
   for i, row in enumerate(state):
       if row_sums[i] is not None:
           h += abs(sum(int(cell) for cell in row if cell != 'x') - row_sums[i])
   for i in range(num_cols):
       if col_sums[i] is not None:
           h += abs(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') - col_sums[i])
   h += abs(sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') - diagonal_sum)
   return h


print(a_star())
