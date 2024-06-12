
import heapq


def initialize():
   # Define the initial state of the grid, with the given numbers represented as integers and the unknown numbers represented as 'x'
   initial_state = [['62', '82', 'x'],
                    ['x', 'x', 'x'],
                    ['x', 'x', 'x']]


   # Encoding other variables given in the problem
   num_rows = 3
   num_cols = 3
   goal_col_sum = 233
   goal_row_sum = 207
   goal_diag_sum = 185


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the specified rows, columns, and diagonal equals the given amounts
       if sum(int(state[i][j]) for i in range(num_rows) for j in range(num_cols) if state[i][j] != 'x') == goal_col_sum + goal_row_sum + goal_diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in range(50, 85):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = str(num)
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of unique integers used, as the task is to minimize the number of unique integers used
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it does not take into account the uniqueness of the integers
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect integer must be replaced once
   # It's consistent because moving an integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer is not in the goal state), which is equal to the cost of reaching the successor node
   h = 0
   # Calculate the current sums of the specified rows, columns, and diagonal
   current_col_sum = sum(int(state[i][0]) for i in range(num_rows))
   current_row_sum = sum(int(state[0][j]) for j in range(num_cols))
   current_diag_sum = int(state[0][0]) + int(state[1][1]) + int(state[2][2])
   # Add the absolute differences between the current sums and the goal sums to the heuristic
   h += abs(current_col_sum - goal_col_sum) + abs(current_row_sum - goal_row_sum) + abs(current_diag_sum - goal_diag_sum)
   return h


print(a_star())
