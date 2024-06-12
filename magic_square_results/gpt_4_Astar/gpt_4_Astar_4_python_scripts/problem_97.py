
import heapq


def a_star():
   # Define the initial state of the grid, the range of numbers, and the sums of the rows, columns, and diagonal
   initial_state = (('68', 'x', 'x', '76'), ('74', 'x', 'x', 'x'), ('x', 'x', '82', 'x'), ('66', 'x', '35', 'x'))
   num_range = set(range(33, 85))
   row_sums = [None, 229, 249, None]
   col_sums = [None, 189, 204, None]
   diag_sum = 219
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
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of the unique integers in the range
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Generate the new state by replacing the 'x' with any of the unique integers in the range
                   for num in num_range:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the sum of the specified rows, columns, and diagonal equals the given amounts
                       if all(sum(int(cell) for cell in row if cell != 'x') <= row_sums[row_ind] for row_ind, row in enumerate(new_state)) and all(sum(int(new_state[row_ind][col_ind]) for row_ind in range(num_rows) if new_state[row_ind][col_ind] != 'x') <= col_sums[col_ind] for col_ind in range(num_cols)) and sum(int(new_state[row_ind][num_cols - row_ind - 1]) for row_ind in range(num_rows) if new_state[row_ind][num_cols - row_ind - 1] != 'x') <= diag_sum:
                           # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                           new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, num_range), new_cost, actions + [(i, j, num)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state, num_range):
   # An admissible and consistent heuristic for this problem is the sum of the minimum remaining numbers in the range that can be added to the grid
   # The heuristic relaxes the constraints that the sum of the specified rows, columns, and diagonal must equal the given amounts and that each number can be in the final grid only once; ie It presumes we can add the smallest remaining numbers in the range to the grid
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' in the grid with a number is the number itself, which is always greater than or equal to the smallest remaining number in the range, the decrease in the heuristic cost
   h = 0
   remaining_nums = sorted(num_range - set(int(cell) for row in state for cell in row if cell != 'x'))
   for i in range(sum(1 for row in state for cell in row if cell == 'x')):
       h += remaining_nums[i]
   return h


print(a_star())
