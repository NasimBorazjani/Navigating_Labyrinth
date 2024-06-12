
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the rows, columns, and diagonal
   initial_state = (('27', '48', 'x', 'x'), ('x', 'x', '63', 'x'), ('28', 'x', '33', '26'), ('x', 'x', 'x', '39'))
   unique_integers = set(str(i) for i in range(22, 69))
   row_sums = [None, 190, 154, None]
   col_sums = [None, 183, 202, None]
   diagonal_sum = 183
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
       if all(cell != 'x' for row in state for cell in row):
           # Check if the sums of the rows, columns, and diagonal in the current state match the given sums
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') == diagonal_sum:
               return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of the available unique integers
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # The available unique integers are all the numbers in the range that are not present in the current state
                   available_unique_integers = unique_integers - set(cell for row in state for cell in row if cell != 'x')
                   for number in available_unique_integers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(number)


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, int(number))], new_state))
                   # If the state has at least 1 remaining unknown number, ie 'x', break the loop after generating all possible actions from the current state
                   break
           else:
               continue
           break
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and their goal sums
   # The heuristic relaxes the constraints that each number in the grid must be unique and that the sum of all of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' in the grid with a number is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums
   h = 0
   num_rows = len(state)
   num_cols = len(state[0])
   for row, row_sum in zip(state, row_sums):
       if row_sum is not None:
           h += abs(sum(int(cell) for cell in row if cell != 'x') - row_sum)
   for j, col_sum in enumerate(col_sums):
       if col_sum is not None:
           h += abs(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') - col_sum)
   h += abs(sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') - diagonal_sum)
   return h


print(a_star())
