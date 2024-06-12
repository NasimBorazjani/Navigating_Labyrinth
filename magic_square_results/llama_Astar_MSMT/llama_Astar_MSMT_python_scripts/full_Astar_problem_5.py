
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [22, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 82
   goal_row_sum = 82
   goal_diag_sum = 82


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the total sum of all the numbers in the grid
   initial_state_info = (initial_state, 0)
   # The initial state has already been visited with a cost of 0
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, (state, state_sum) = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state_sum == goal_col_sum * num_cols and state_sum == goal_row_sum * num_rows and state_sum == goal_diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in range(20, 40):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of numbers replaced, as the task is to minimize the number of numbers replaced
                       new_cost = g + 1
                       new_state_sum = state_sum + num


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row, col, num)], (new_state, new_state_sum)))
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must equal the goal sum
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted by at least 1
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's sum matches the goal sum for the new position but not in the old one), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += abs(sum(row) - goal_col_sum)
   for col in range(len(state[0])):
       h += abs(sum(state[row][col] for row in state) - goal_row_sum)
   h += abs(sum(state[i][i] for i in range(len(state))) - goal_diag_sum)
   return h


print(a_star())
