
import heapq


def a_star():
   # Define the initial state of the grid, the range of numbers, and the sums of the rows, columns, and diagonal
   initial_state = (('36', '47', 'x', 'x'), ('x', '28', '40', 'x'), ('x', '33', 'x', 'x'), ('50', 'x', 'x', 'x'))
   num_range = set(range(28, 65))
   row_sums = [None, 152, 158, None]
   col_sums = [None, 156, 185, None]
   diagonal_sum = 165
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
       # The goal state is where all the 'x's in the grid are replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row) and all(sum(int(cell) for cell in row if cell != 'x') in [row_sums[i], sum(int(cell) for cell in row if cell != 'x')] for i, row in enumerate(state)) and all(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') in [col_sums[i], sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x')] for i in range(num_cols)) and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for num in num_range - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + num


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the current sum of each row, column, and diagonal and their goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one state to an adjacent state is the number added to the grid, which is always greater than or equal to 1, the decrease in the difference between the current sum and the goal sum
   h = 0
   for i in range(len(state)):
       if row_sums[i] is not None:
           h += row_sums[i] - sum(int(cell) for cell in state[i] if cell != 'x')
   for i in range(len(state[0])):
       if col_sums[i] is not None:
           h += col_sums[i] - sum(int(state[j][i]) for j in range(len(state)) if state[j][i] != 'x')
   h += diagonal_sum - sum(int(state[i][len(state) - i - 1]) for i in range(len(state)) if state[i][len(state) - i - 1] != 'x')
   return h


print(a_star())
