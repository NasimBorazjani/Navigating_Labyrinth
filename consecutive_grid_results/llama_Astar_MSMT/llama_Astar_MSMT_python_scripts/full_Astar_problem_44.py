
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 58, None], [42, None, 70], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
  
   visited_costs = {}
   visited_costs[initial_state] = 0
  
   # The information we must encode for each state includes the current state of the grid and the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   initial_state_info = (initial_state, 58 + 70)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()
  
   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if all(row[0] is not None and row[-1] is not None and row[0] < row[1] < row[2] for row in state_info[0]):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state_info[0][row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state_info[0]]
                   # The new state must maintain the consecutive order in each row and column
                   for new_val in range(31, 85):
                       if all(31 <= new_state[row_ind][col_ind - 1] < new_val <= 84 for col_ind in range(1, num_cols) if new_state[row_ind][col_ind - 1] is not None) and all(31 <= new_state[row_ind - 1][col_ind] < new_val <= 84 for row_ind in range(1, num_rows) if new_state[row_ind - 1][col_ind] is not None):
                           new_state[row_ind][col_ind] = new_val
                           new_state_info = (tuple(tuple(row) for row in new_state), state_info[1] + new_val)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required to fill the grid
                           new_cost = g + 1


                           if new_state_info not in visited_costs or new_cost < visited_costs[new_state_info]:
                               visited_costs[new_state_info] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_info, new_state_info), g + 1, actions + [(row_ind, col_ind, new_val)], new_state_info))
   return None


def heuristic(current_state_info, goal_state_info):
   # The heuristic function can be the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner minus the current sum of the numbers in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each replacement must not result in the sum of the numbers in the grid exceeding the minimum possible sum
   # The heuristic is consistent because moving a number to a lower value or a higher value results in a decrease or an increase in the heuristic cost of the successor node by a max of 2 (if the moved number's value matches the current sum of the numbers in the grid), which is equal to the cost of reaching the successor node
   return goal_state_info[1] - current_state_info[1]


print(a_star())
