
import heapq


def initialize():
   # Define the magic square, encoding the given numbers as integers and the unknown numbers as 'x'
   magic_square = [['x', 77, 'x'],
                   [49, 'x', 'x'],
                   ['x', 'x', 'x']]

   # Encoding other variables of the problem
   num_rows = 3
   num_cols = 3
   goal_row_sums = [156, 'x', 127]
   goal_col_sums = [180, 'x', 'x']
   goal_diag_sum = 127

   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[magic_square] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], magic_square)]
  
   return magic_square, num_rows, num_cols, goal_row_sums, goal_col_sums, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   magic_square, num_rows, num_cols, goal_row_sums, goal_col_sums, goal_diag_sum, visited_costs, queue = initialize()

   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state
       # The goal state is when the sum of all rows, columns, and the diagonal equals the given amounts
       if all(sum(row) == goal_row_sums[i] for i, row in enumerate(state)) and all(sum(col) == goal_col_sums[i] for i, col in enumerate(zip(*state))) and sum(state[i][i] for i in range(num_rows)) == goal_diag_sum:
           return actions

       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer in the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(34, 79):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = num
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the magic square
                       new_cost = g + 1

                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(state, goal_row_sums, goal_col_sums, goal_diag_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal_row_sums, goal_col_sums, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that the numbers in the magic square must be unique and can be in the range from 34 to 78
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by at least one action
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved number is the only one that causes the sum to be incorrect), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       h += abs(sum(state[i]) - goal_row_sums[i])
       h += abs(sum(col[i] for col in zip(*state)) - goal_col_sums[i])
   h += abs(sum(state[i][i] for i in range(len(state))) - goal_diag_sum)
   return h


print(a_star())
